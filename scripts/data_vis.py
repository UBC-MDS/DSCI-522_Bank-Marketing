"""
data_exploratory-visualization.py

Created on 2018-11-23

by: Sabrina Tse

This scripts imports the cleaned version of the data 'bank_full.csv' file into a pandas dataframe
and summarize data through visualization. For categorical variable, seaborn catplot will be used.
For continuous variable, seaborn boxplot will be used for presentation.

It then exports the graph into a file(suggested: png or jpg file for the best presentation)

Dependencies: Python (argparse, pandas,matplotlib,seaborn)

Usage: python scripts/data_exploratory-visualization.py ./data/cleaned/bank_full.csv job ./results/imgs/job_signup.png

"""
# import modules required for visualization
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
import argparse

#va
parser = argparse.ArgumentParser(description='Please enter csv file name and variable for plotting. Read `readme` page for available variable names')
parser.add_argument('input_file')
parser.add_argument('variable',help="Please enter a variable to compare against `sign-up` ")
parser.add_argument('output_file')
args = parser.parse_args()

def main():

    #read data
    data = pd.read_csv(args.input_file)

    #plotting categorical variables vs continuous variables
    continous_variables=['age','campaign','previous']
    if args.variable in continous_variables:
        out = sns.boxplot(x="sign_up",y=args.variable,data=data)
        print(out)
    else:
        out = sns.catplot(x="sign_up",col=args.variable,col_wrap=4,data=data,kind="count",height=3)
        print(out)
    #save results
    plt.savefig(args.output_file)

if __name__ == "__main__":
    main()
