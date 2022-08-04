
import csv

"""To write data into csv file"""
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction id", "product id", "price"])
    writer.writerow([1000, 1, 50])
    writer.writerow([1001, 2, 100])

"""To read data from csv file"""
# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)


# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["account no.", "username", "type", "amount"])
#     writer.writerow([1, "Roshan", "Savings", "15000"])
#     writer.writerow([2, "Yogesh", "Savings", "10000"])
#     writer.writerow([3, "Sachin", "Current", "12000"])
