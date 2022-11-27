https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# solutions 3.5 and 3.6
# author: Nick Szirbik
# date: 14 Sept 2020

import csv

with open("groningenRestaurants.csv") as handler_csv_file:
    raw_content_file = csv.reader(handler_csv_file)
    table = list(raw_content_file)
# selecting records conditionally
"""
for row in table[1:]:
    name = row[0]
    address = row[1]
    if name[0] == "D" and address[0] == "R":
        print("-selected on first criteria: ", row)

for row in table[1:]:
    name = row[0]
    if name.find("Pizz") != -1 or name.find("pizz") != -1:
        print("-selected on second criteria: ", row)

for row in table[1:]:
    name = row[0]
    if (name.find("Pizz") != -1 or name.find("pizz") != -1) or (name.find("Eet") != -1 or name.find("eet") != -1):
        print("-selected on third criteria: ", row)
#           change the "and" logical operator in the condition above with "or" and see what happens

# it is actually easier for this kind of check to convert the string that is
# checked into a lowercase only string, by using the function lower() as below

for row in table[1:]:
    address = row[1].lower()
    if (address.find("noord") != -1) or (address.find("zuid") != -1) or (address.find("oost") != -1) or (address.find("west") != - 1):
        print("-selected on the final criteria", row)
"""
# adding a new restaurant (this is partially from 3.6)

name = input("restaurant name is: ")
address = input("restaurant address is: ")
lonlat = input("coordinates are: ")
new_row = list((name, address, lonlat))
table.append(new_row)
print(table[-1])

with open("groningenRestaurants_v1.csv", mode="w") as handler:
    file_writer = csv.writer(handler,
                             quotechar = '"', quoting=csv.QUOTE_MINIMAL)
                    # necessary to put quotes when commas appear in a data point
                    # and have the same format with the rest of the existing file
    for row in table:
        file_writer.writerow(row)

print("finished")
