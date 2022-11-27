https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# solution 3.6 with function definition
# author: Nick Szirbik
# date: 14 Sept 2020

import csv
# first, define a function that reads the datapoints for one restaurant
def readRestaurantData(header):
  record =[]
  for datapoint in header:
      value = input(datapoint + "= ")
      record.append(value)
  return record
# OBSERVE: this function works for any input file with any table header
# it has the main quality of a function - it can be reused again and again
# without changing it

# the rest of code is rather similar
with open("groningenRestaurants.csv") as handler_csv_file:
    raw_content_file = csv.reader(handler_csv_file)
    table = list(raw_content_file)

# use a while statement to repeat a statement block until y is inputted by the user
stop = False
while not stop:
    newRestaurant = readRestaurantData(table[0])
# the function gets the table header as argument and returns one full data records
# for one restaurant - if the header is longer than 3, it will work anyway
    if (input("stop? y/n") == 'y'):
        stop = True
    table.append(newRestaurant)

with open("groningenRestaurants_v2.csv", mode="w") as handler:
    file_writer = csv.writer(handler,
                             quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    for row in table:
        file_writer.writerow(row)
# this last line is always useful to know if the script terminated normally
print("finished")
