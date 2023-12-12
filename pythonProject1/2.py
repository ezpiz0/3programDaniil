import table_operations
import csv_module
import pickle_module
import text_module
from table_operations import Table
data = [["Index","Name","Age","Salary"],
        [1,"John",30,50000],
        [2,"Doe",25,70000],
        [3,"Jane",28,60000],
        [4,"Smith",40,80000]]
table =  Table(data)
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

# set_column_types не работает!!!!!!!!!!
print("set_column_types:")
tabl_types_dict = {1: "str", 2: "int", 3: "int"}
table.set_column_types(tabl_types_dict)
print(table.get_column_types())
print()

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
