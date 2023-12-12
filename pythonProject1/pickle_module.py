import pickle

def load_table(file_name):
    try:
        with open(file_name, 'rb') as file:
            table = pickle.load(file)
            return table
    except FileNotFoundError:
        raise Exception("Файл не найден")

def save_table(table, file_name):
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(table, file)
    except IOError:
        raise Exception("Ошибка сохранения таблицы в файл")