import csv

with open("data.csv","r") as file :
    reader = csv.reader(file)
    for i in reader:
        print(i[0])