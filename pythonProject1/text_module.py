def save_table(table, file_name):
    try:
        with open(file_name, 'w') as file:
            for row in table:
                file.write('\t'.join(str(cell) for cell in row))
                file.write('\n')
    except IOError:
        raise Exception("Ошибка сохранения таблицы в файл")