import csv


class CSV_OP:
    def read_data(self, filename):
        with open(filename) as file:
            data = csv.reader(file)
            for item in data:
                print(item)
