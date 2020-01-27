import csv
import json


def csv_writer(data, p):
    field_names = []
    for key in data:
        for k in key:
            if k not in field_names:
                field_names.append(k)
    with open(p, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


def json_reader(file):
    with open(file, 'r') as json_file:
        json_str = json_file.read()
        obj_data = json.loads(json_str)
        return obj_data


if __name__ == '__main__':
    path_csv = 'csv_file.csv'
    path_json = 'json_file.json'
    obj = json_reader(path_json)
    csv_writer(obj, path_csv)
