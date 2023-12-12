import table_operations
import csv_module
import pickle_module
import text_module
from table_operations import Table
import csv

table = Table.load_table_from_file('data.csv', 'csv')
print("get_rows_by_number:")
print(table.get_rows_by_number(1, 3, copy_table=True))
print()

# get_rows_by_index
print("get_rows_by_index:")
print(table.get_rows_by_index(1, 3, copy_table=True))
print()

# get_column_types
print("get_column_types:")
print(table.get_column_types())
print()


# set_column_types
column_types = {
    0: 'int',
    1: 'str',
    2: 'float',
    3: 'float',
}

print("set_column_types:") # не работает
print(table.set_column_types(column_types))

# get_values
print("get_values:")
print(table.get_values(1)) # получение списка значений по номеру столбца
print()

# get_value
print("get_value:")
print(table.get_value(1)) # одно значение из таблицы с 1 строкой
print()

# set_values
print("set_values:")
table.set_values([10, 24, 23, 46], 2)
print(table.get_values(2)) # изменяет значения в столбце таблицы
print()

# set_value
print("set_value:")
table.set_value(50000, 3)
print(table.get_value(3)) # аналог для таблицы с 1 строкой
print()

# print_table
print("print_table:")
table.print_table() # вывод измененной таблицы

age_greater_than_salary = table.gr(2, 3)
name_not_equal_jane = table.ne(1, ["Jane"] * (len(table.data) - 1))  # сравнения

print("Возраст больше, чем зарплата:", age_greater_than_salary)

print("Имя не Jane:", name_not_equal_jane)

filtered_table = table.filter_rows(name_not_equal_jane, copy_table=True) # Фильтрация и вывод отфильтрованной таблицы
print("\nОтфильтрованная таблица (имя не равно Jane):")
filtered_table.print_table()

eq_results = table.eq(2, 3)
print("Сравнение равенства возраста и зарплаты:", eq_results)

gr_results = table.gr(2, 3)
print("Больше ли возраст, чем зарплата:", gr_results)

ls_results = table.ls(2, 3)
print("Меньше ли возраст, чем зарплата:", ls_results)

ge_results = table.ge(2, 3)
print("Возраст больше или равен зарплате:", ge_results)

ne_results = table.ne(2, 3)
print("Не равен ли возраст зарплате:", ne_results)

le_results = table.le(2, 3)
print("Возраст меньше или равен зарплате:", le_results)


