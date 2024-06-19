import csv

with open("C:/Users/Palak Jain/Downloads/sample.csv", mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
     print(lines)
