https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# solution 3.3
# author: Nick Szirbik
# date: 14 Sept 2020

import csv
# open and read the content of the comma separated values file
with open("groningenRestaurants.csv") as handler_csv_file:
    raw_content_file = csv.reader(handler_csv_file)
#       raw_content_file is a mere collection of characters

    table = list(raw_content_file)
#       forcing (typecasting) the character collection into a list of list
print("total number of data records =", len(table))
print("table header = ", table[0])
print("last record in the table = ", table[-1])

print("name in the last record in the table = ", table[-1][0])
print("data points in a record =", len(table[0]))
