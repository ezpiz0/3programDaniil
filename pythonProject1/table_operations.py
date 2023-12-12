from csv_module import load_table as load_table_csv
from pickle_module import load_table as load_table_pickle
class Table:
    def __init__(self, data):
        self.data = data

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        if stop is None:
            stop = start + 1
        if copy_table:
            return [row[:] for row in self.data[start:stop]]
        else:
            self.data = self.data[start:stop]
            return self.data

    def get_rows_by_index(self, *values, copy_table=False):
        new_table = [row for row in self.data if row[0] in values]
        if copy_table:
            return [row[:] for row in new_table]
        else:
            self.data = new_table
            return self.data

    def _get_column_type(self, column):
        types = set()
        for row in self.data[1:]:
            value = row[column]

            if value is None or value == '':
                continue

            if isinstance(value, str):
                if value.isdigit():
                    value = int(value)
                else:
                    try:
                        value = float(value)
                    except ValueError:
                        pass

            types.add(type(value))

        types.discard(int) if float in types else None

        if len(types) > 1:
            raise Exception(f"Несколько несовместимых типов данных в столбце {column}: {types}")

        return types.pop().__name__ if types else 'str'

    def get_column_types(self):
        types = []
        for i in range(len(self.data[0])):
            column_type = self._get_column_type(i)
            types.append(column_type)
        return types

    def get_values(self, column=0):
        column_data = [row[column] for row in self.data[1:]]
        column_type = self._get_column_type(column)
        return [self._convert_value(value, column_type) for value in column_data]

    def get_value(self, column=0):
        value = self.data[1][column]
        column_type = self._get_column_type(column)
        return self._convert_value(value, column_type)

    def set_values(self, values, column=0):
        if len(values) != len(self.data) - 1:
            raise Exception("Количество значений не соответствует количеству строк в таблице")

        column_data = [self._convert_value(value if value is not None else '',
                                           self._get_column_type(column))
                       for value in values]
        for i, row in enumerate(self.data[1:]):
            row[column] = column_data[i]

    def set_value(self, value, column=0):
        self.data[1][column] = self._convert_value(value if value is not None else '',
                                                   self._get_column_type(column))

    def print_table(self):
        for row in self.data:
            print('\t'.join(str(cell) if cell is not None else 'None' for cell in row))

    def _validate_column_type(self, column, column_type):
        data_type = type(self.data[1][column])
        if column_type == 'int' and data_type is not int:
            raise Exception("Invalid column type")
        elif column_type == 'float' and data_type is not float:
            raise Exception("Invalid column type")
        elif column_type == 'bool' and data_type is not bool:
            raise Exception("Invalid column type")
        elif column_type == 'str' and data_type is not str:
            raise Exception("Invalid column type")

    def _convert_value(self, value, column_type):
        if value == '' or value is None:
            return None
        if column_type == 'int':
            return int(value)
        elif column_type == 'float':
            return float(value)
        elif column_type == 'bool':
            return bool(int(value))
        elif column_type == 'str':
            return str(value)

    def set_column_types(self, types_dict):
        for column, column_type in types_dict.items():
            for row in self.data[1:]:
                row[column] = self._convert_value(row[column], column_type)

        for column, column_type in types_dict.items():
            self._validate_column_type(column, column_type)

    def _safe_compare(self, op, column1, column2):
        results = []
        col1_data = self._extract_column(column1)
        col2_data = self._extract_column(column2)
        for a, b in zip(col1_data, col2_data):
            try:
                a = float(a) if isinstance(a, str) and a.replace('.', '', 1).isdigit() else a
                b = float(b) if isinstance(b, str) and b.replace('.', '', 1).isdigit() else b
            except ValueError:
                pass

            if isinstance(a, type(b)) or isinstance(b, type(a)):
                result = op(a, b)
            else:
                result = False

            results.append(result)
        return results

    def eq(self, column1, column2):
        return self._safe_compare(lambda a, b: a == b, column1, column2)

    def gr(self, column1, column2):
        def compare(a, b):
            try:
                return int(a) > int(b)
            except ValueError:
                pass
            except TypeError:
                pass

        return self._safe_compare(compare, column1, column2)

    def ls(self, column1, column2):
        return self._safe_compare(lambda a, b: a < b, column1, column2)

    def ge(self, column1, column2):
        return self._safe_compare(lambda a, b: a >= b, column1, column2)

    def le(self, column1, column2):
        return self._safe_compare(lambda a, b: a <= b, column1, column2)

    def ne(self, column1, value_or_column):
        if isinstance(value_or_column, list):
            return [a != b for a, b in zip(self._extract_column(column1), value_or_column)]
        else:
            return self._safe_compare(lambda a, b: a != b, column1, value_or_column)

    def filter_rows(self, bool_list, copy_table=False):
        if len(bool_list) != len(self.data) - 1:
            raise ValueError("Длина логического списка должна быть равна количеству строк данных")

        filtered_data = [self.data[0]]
        filtered_data.extend(row for row, include in zip(self.data[1:], bool_list) if include)

        if copy_table:
            return Table(filtered_data)
        else:
            self.data = filtered_data
            return self

    def load_table_from_file(file_name, file_type):
        if file_type == 'csv':
            data = load_table_csv(file_name)
        elif file_type == 'pickle':
            data = load_table_pickle(file_name)
        else:
            raise ValueError("Неизвестный тип файла")

        return Table(data)

    def _extract_column(self, column_index):
        return [row[column_index] for row in self.data[1:]]


