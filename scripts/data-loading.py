# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:19:48 2018

This scripts imports the 'bank-additional-full.csv' file into a pandas dataframe.

Brenden Everitt, Sabrina Tse
"""

# import pandas module

import pandas as pd

# Read in data

data_customer = pd.read_csv("./data/raw data/bank-additional-full.csv", delimiter=";")

print(data_customer.head(10))



