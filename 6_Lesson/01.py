import csv
import json

"""The program converts data from a .json file to a .csv file."""


def csv_writer(data, p):
    field_names = []
    for key in data:  # Получаем имена колонок
        for k in key:
            if k not in field_names:
                field_names.append(k)
    with open(p, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


def json_reader(file):  # Метод для считывания данных из .json файла
    with open(file, 'r') as json_file:
        json_str = json_file.read()  # Сохраняем данные json в строке
        obj_data = json.loads(json_str)  # Десериализуем данные
        return obj_data  # Возвращаем полученные данные


if __name__ == '__main__':
    path_csv = 'csv_file.csv'  # Путь к csv файлу
    path_json = 'json_file.json'  # Путь к json файлу
    obj = json_reader(path_json)
    csv_writer(obj, path_csv)
    print(__doc__)
