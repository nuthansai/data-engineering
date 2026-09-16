import csv


def write_to_csv(data, file_name, field_names):
    column_names = [i for i in field_names]
    print(column_names)
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)

        writer.writeheader()

        for key, values in data.items():
            writer.writerow({'page': key, 'clicks': values})



