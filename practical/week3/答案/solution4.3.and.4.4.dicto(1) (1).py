https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# solution 4.3 and 4.4
# author: Nick Szirbik
# date: 17 Sept 2020

import numpy as np
import pandas as pd
from statistics import mean

# define a dictionary directly in the code
# basically, this is a table, but dictionaries are versatile
# and can be used for other kinds of less structured datapoints
data_in_dict = { "year" : [
            1950, 1951, 1952,
            1953, 1954, 1955,
            1956, 1957, 1958, 1959
            ],
         "champ" : [
            "Farina", "Fangio", "Ascari", "Ascari",
            "Fangio", "Fangio", "Fangio", "Fangio",
            "Hawthorne", "Brabham"
            ],
         "wins" : [
            3, 3, 6, 5,
            6, 4, 3, 4, 1, 2
            ],
         "points" : [
            30, 31, 36, 34,
            42, 40, 30, 40, 42, 43
            ]
        }

# add new data (a new column, in this case) the dictionary above
# HINT: the notation ["m"] * 10 makes code writing easier than below...
data_in_dict["gender"] = ["m", "m", "m",
                  "m", "m", "m",
                  "m", "m", "m", "m"
                  ]
#print it ugly...
print("raw dictionary dump: \n", data_in_dict)

# ... and print it nicely, by making it first a Panda DataFrame object
formula_One = pd.DataFrame(data_in_dict, columns = [
    "year", "champ", "wins", "points", "gender"
    ])
print("printing as a pandas DataFrame object:")
print(formula_One)

# print the meta-information about the DataFrame
print("the size of the table is (rows * columns):")
print(formula_One.shape)
print("the rows are organized as:")
print(formula_One.columns)
print("the Python type of the values on the columns are:")
print(formula_One.dtypes)

# save the information in the DataFrame object to a .csv File
# this time, with a specialized method from the Pandas library
formula_One.to_csv("f1_fifties.csv")
print('data frame written to csv file f1_fifties.csv')
# open the "f1_fifties.csv" file and have a look...
#
# 4.4
team_wins = ["Alfa"] * 2 + ["Ferrari"] * 2 + ["Mercedes"
    ] * 2 + ["Ferrari", "Maserati", "Ferrari", "Cooper"]

formula_One["team"] = team_wins
print(formula_One)

# boy only club :-(
del(formula_One["gender"])
print(formula_One)

# print the first five and the last three
print(formula_One.head())
print(formula_One.tail(3))

# print the last four
print(formula_One["champ"][-4:])

# print only Ascari
print(formula_One[["champ", "year"]][2:4])

# make statistics
print("average point score in the fifties:", mean(formula_One["points"]))

# make a smaller DataFrame object, selecting from the big one
only_Maserati_seasons = formula_One[formula_One['team'] == 'Maserati']
print(type(only_Maserati_seasons))
print(only_Maserati_seasons)
# it was only one Maserati win, ever...

# selecting on two conditions
only_Fangio_seasons = formula_One[formula_One['champ'] == 'Fangio']
only_Fangio_driving_Ferrari_seasons = only_Fangio_seasons[
    only_Fangio_seasons['team'] == 'Ferrari']
print(only_Fangio_driving_Ferrari_seasons)
# Fangio won only once with Ferrari
# end of 4.4.
