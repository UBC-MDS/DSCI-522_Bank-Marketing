"""
create-decision-tree.py

Created on Nov 23, 2018

This scripts imports the cleaned data and performs cross validtion finding the
best hyperparameter value for maximum depth of the decision. It then creates a
decision treewith that hyperparameter value and finds the prediction accuracy.

Author: Brenden Everitt

Dependencies: argparse, pandas, numpy, matplotlib, graphviv, sklearn

Usage: python create-decision-tree.py ./data/cleaned/bank_data-clean.csv <>

"""
# Import Packages
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import graphviz

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import tree

# Read in arguments
parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()


def main():

    X_train, X_test, y_train, y_test = prep_data(args.input_file)
    Find_Best_Max_Depth(X_train, y_train)
    dec_tree = Create_Decision_Tree(6, X_train, y_train)

    # Write test accuracy of decision tree to file
    test_acc = dec_tree.score(X_test, y_test)
    file = open(args.output_file, 'w')
    file.write('Test Accuracy,' + str(test_acc)) #Give your csv text here.
    file.close()


def prep_data (data):
    "Reads in data file and prapres it for sklearn DecisionTreeClassifer"

    data_customer = pd.read_csv(data)

    # Drop variables we are not using
    data_customer = pd.get_dummies(data_customer, columns = ["job", "marital", "education", "default", "housing", "loan", "contact", "month", "day_of_week", "poutcome"])

    # Get feature variables, and target variables
    X_feat = data_customer.drop(["y"], axis = 1)
    y_targ = data_customer["y"]

    # Encode target variable numerically
    lab_encode = LabelEncoder()
    y_targ = lab_encode.fit_transform(y_targ)

    X_feat_train, X_feat_test, y_targ_train, y_targ_test = train_test_split(X_feat, y_targ, test_size = 0.2, random_state = 1234)

    return X_feat_train, X_feat_test, y_targ_train, y_targ_test

def Find_Best_Max_Depth (features, target):
    "Uses Cross Validation to find the best maximum depth hyperparameter"

    max_depths = [i for i in range(1,51)]
    k_folds = 10
    cv_acc = []

    dec_tree = tree.DecisionTreeClassifier()

    # Perform Cross Validation for all the different max depth values
    for depth in max_depths:
        dec_tree = tree.DecisionTreeClassifier(max_depth=depth)
        cv_acc.append(np.mean(cross_val_score(dec_tree, features, target, cv=k_folds)))

    plt.plot(max_depths, cv_acc, label = "Cross Validation Accuracy")
    plt.legend()
    plt.xlabel("Tree Depth")
    plt.ylabel("Test Accuracy")
    plt.savefig("./results/imgs/Cross-Validation-Scores.png")

def Create_Decision_Tree (depth, features, target):
    "Creates decision tree with the defined maximum depth"

    dec_tree = tree.DecisionTreeClassifier(max_depth= depth)
    dec_tree.fit(features,target)

    # Create visual of the best decision tree
    dot_data = tree.export_graphviz(dec_tree, out_file=None, feature_names=list(features.columns.values),
                                     class_names=["No", "Yes"], filled=True, rounded=True, special_characters=True)

    graph = graphviz.Source(dot_data)
    graph.render("./results/imgs/Decision-Tree", view=False)

    return dec_tree

if __name__ == "__main__":
    main()
