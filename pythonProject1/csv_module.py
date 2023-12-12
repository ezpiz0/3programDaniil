import csv

def load_table(file_name):
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            table = []
            for row in reader:
                new_row = []
                for item in row:
                    if item == '':
                        new_row.append(None)
                    else:
                        try:
                            new_row.append(float(item))
                            if new_row[-1].is_integer():
                                new_row[-1] = int(new_row[-1])
                        except ValueError:
                            new_row.append(item)
                table.append(new_row)
            return table
    except FileNotFoundError:
        raise Exception("Файл не найден")

def save_table(table, file_name):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(table)
    except IOError:
        raise Exception("Ошибка сохранения таблицы в файл")
data = [
    ["Index", "Name", "Age", "Salary"],
    [1, "John", 30, 50000],
    [2, "Doe", None, 70000],
    [3, "Jane", 28, None],
    [4, "Smith", 40, 80000]
]

filename = "data.csv"

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerows(data)