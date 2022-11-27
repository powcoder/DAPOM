https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# solution 3.4
# author: Nick Szirbik
# date: 14 Sept 2020

import csv

with open("groningenRestaurants.csv") as handler_csv_file:
    raw_content_file = csv.reader(handler_csv_file)
    table = list(raw_content_file)

# check the lengths of the records - print all of them
for record in table:
    print(len(record))
# try to inspect the output visually

# pretty print the table
for record in table[1:]: #note the indexing, it skips the header
	address = record[1]
	geolocation = record[2]
	name = record[0]
	print("\nAt:", address, "\ncoord.:", geolocation, "\nis:", name)

# catch length errors automatically (alter the .csv file by hand)
expected_record_length = len(table[0])
consistent = True
for record in table[1:]:
    consistent = (len(record) == expected_record_length)
    if not consistent:
        print("ALERT, ALERT, ALERT")
        print(record, "has", len(record), "data points")
        break
    else:
        continue
# the above one catches only the first one
# if there are not problems, we should also indicate this to the user
if consistent:
    print("KEEP cool: all records have the same value")

# the code below catches all the bad lines
expected_record_length = len(table[0])
wrong_length_record_counter = 0
for record in table[1:]:
    if not len(record) == expected_record_length:
        wrong_length_record_counter += 1
        print("ALERT", record, "has", len(record), "data points")
print("In total", wrong_length_record_counter, "times, the record length is wrong")

# a more ellegant alternative to the code above

incorrect_records = []
expected_record_length = len(table[0])
for record in table[1:]:
    if not(len(record) == expected_record_length):
        incorrect_records.append(record)

print("In total", len(incorrect_records), "times, the record length is wrong")
# we have now the bad records stored separately, and we can print them
for bad_record in incorrect_records:
    print(bad_record, "bad length =", len(bad_record))

# the above also helps to delete the incorrect length records from the table
# we do it record by record iterating through the collected ones
for bad_record in incorrect_records:
    table.remove(bad_record)
    print("one record removed from the table")
