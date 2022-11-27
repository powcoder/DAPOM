https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# solution 4.5
# author: Nick Szirbik
# date: 17 Sept 2020

import numpy as np
import pandas as pd
import re # this is a useful library for "regular expressions"

# we can create a DataFrame object directly from a file, like below:
restaurants = pd.read_csv("groningenRestaurants.csv")
# shorter and easier than the with, open, read, list() construct

# have a look first...
print(restaurants)

# sample is from pandas and not from statistics
random_selection = restaurants.sample(12)
print(random_selection[["restaurant","lonlat"]])

pd.set_option('display.max_rows', restaurants.shape[0])
pd.set_option('display.max_columns', restaurants.shape[1])
pd.set_option('display.width', 1000) #characters in one line width
print(restaurants)

# one of the many ways to search for substrings in a DataFrame
selected_df = restaurants[restaurants['restaurant'].str.contains('Pizz')
                          | restaurants['restaurant'].str.contains('pizz')]
# in pandas you have to use "|" instead of OR and "&" instead of AND
print(selected_df)

# or, by using regular expressions, note the switching parameter in contains()
selected_df = restaurants[restaurants['restaurant'].str.contains('Pizz|pizz',
                                                                 regex = True)]
print(selected_df)

# even easier
selected_df = restaurants[restaurants['restaurant'].str.contains('pizz',
                                flags = re.IGNORECASE, regex = True)]
print(selected_df)

# for multiple stringsa more elegant way
terms_for_search = ['noord', 'Noord', 'zuid', 'Zuid',
                    'oost', 'Oost', 'west', 'West']
selected_df1 = restaurants[restaurants[
    'address'].str.contains('|'.join(terms_for_search), regex = True)]
print(selected_df1)

# to have an AND condition you may also select succesively, to avoid big lines
selected_df2 = selected_df1[selected_df1['restaurant'].str.contains('eet|Eet',
                                                                    regex = True)]
print(selected_df2)
# if you write the name of a DataFrame as a Pythn code line, it will
# display the data in a tabular form with gridlines in the output area 
selected_df2
# end of code
