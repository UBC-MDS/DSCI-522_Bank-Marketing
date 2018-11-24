# -*- coding: utf-8 -*-
"""
data_loading-clean.py

Created on Nov 16, 2018

This scripts imports the 'bank-additional-full.csv' file into a pandas dataframe
and performs some data cleaning/manipulation in order to prepare it
for sklearns' DecisionTreeClassifer() and visualization. It then exports the data
into a new csv file.

Authors: Brenden Everitt, Sabrina Tse

Dependencies: argparse, pandas

Usage: python data_loading-cleaning.py bank-additional-full.csv bank_data-clean.csv
"""

# import pandas module

import pandas as pd
import argparse

# Read in arguments
parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

# Read in data

def main():

    data_customer = pd.read_csv(args.input_file, delimiter=";")
    data_customer.columns.values[-1]="sign-up"
    data_customer = data_customer.drop(["duration", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"], axis=1)
    data_customer.to_csv(args.output_file, index = False)

if __name__ == "__main__":
    main()
