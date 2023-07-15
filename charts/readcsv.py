import csv


def read_csv(path):
    with open(path, 'r', encoding='UTF-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)

        data = []
        for row in reader:
            data.append({key: value for key, value in zip(header, row)})

        return data
