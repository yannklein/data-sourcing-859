import csv

# FOR CSV WITHOUT HEADER
# with open("./data/addresses.csv") as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     for row in reader:
#         print(f'{row[0]} is living in {row[3]}.')

# FOR CSV WITH HEADER
with open("./data/biostats.csv") as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    # print(list(reader))
    for row in reader:
        print(f'{row["Name"]} is {row["Age"]} years-old.')