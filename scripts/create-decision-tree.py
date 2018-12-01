"""
create-decision-tree.py

Created on Nov 23, 2018

This scripts imports the cleaned data and performs cross validtion finding the
best hyperparameter value for maximum depth of the decision. It then creates a
decision treewith that hyperparameter value and finds the prediction accuracy.

Author: Brenden Everitt

Dependencies: argparse, pandas, numpy, matplotlib, graphviv, sklearn

Usage: python scripts/create-decision-tree.py ./data/cleaned/bank_full.csv ./results/decision-tree-output.csv


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
parser = argparse.ArgumentParser(description='Please enter the csv file name containing the bank customer data and an output file name to write the results to.')
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()


def main():

    X_train, X_test, y_train, y_test = prep_data(args.input_file)
    Find_Best_Max_Depth(X_train, y_train)
    dec_tree = Create_Decision_Tree(4, X_train, y_train)
    feat_imp = dec_tree.feature_importances_

    # Write outputs from the Decision Tree Classifier to file
    test_acc = dec_tree.score(X_test, y_test)
    file = open(args.output_file, 'w')
    file.write('Test Accuracy \n')
    file.write(str(test_acc) + '\n')
    file.close()

    file2 = open("./results/Feature_Importance.csv", 'w')
    file2.write('Feature, Feature-Importance \n')
    for i in range(len(feat_imp)):
        file2.write(str(list(X_train.columns.values)[i]) + ',' + str(feat_imp[i]) + '\n')
    file.close()


def prep_data (data):
    "Reads in a data file and prepares it for sklearns' DecisionTreeClassifer."

    data_customer = pd.read_csv(data)

    # Create dummy variables
    data_customer = pd.get_dummies(data_customer, columns = ["job", "marital", "education", "default", "housing", "loan", "contact", "month", "day_of_week", "poutcome"])

    # Get feature variables, and target variables
    X_feat = data_customer.drop(["sign_up"], axis = 1)
    y_targ = data_customer["sign_up"]

    # Encode target variable numerically
    lab_encode = LabelEncoder()
    y_targ = lab_encode.fit_transform(y_targ)

    X_feat_train, X_feat_test, y_targ_train, y_targ_test = train_test_split(X_feat, y_targ, test_size = 0.2, random_state = 1234)

    return X_feat_train, X_feat_test, y_targ_train, y_targ_test

def Find_Best_Max_Depth (features, target):
    "Uses Cross Validation to compare different maximum depth hyperparameter values."

    max_depths = [i for i in range(1,51 )]
    k_folds = 5
    cv_acc = []

    # Perform Cross Validation for all the different max depth values
    for depth in max_depths:
        dec_tree = tree.DecisionTreeClassifier(max_depth=depth, class_weight="balanced", random_state = 1234)
        cv_acc.append(np.mean(cross_val_score(dec_tree, features, target, cv=k_folds)))

    plt.plot(max_depths, cv_acc, label = "Cross Validation Accuracy")
    plt.legend()
    plt.xlabel("Tree Depth")
    plt.ylabel("Test Accuracy")
    plt.savefig("./results/imgs/Cross-Validation-Scores.png")

def Create_Decision_Tree (depth, features, target):
    "Creates a decision tree with the defined maximum depth."

    dec_tree = tree.DecisionTreeClassifier(max_depth= depth, class_weight="balanced", random_state = 1234)
    dec_tree.fit(features,target)

    # Create visual of the best decision tree
    # Full Tree
    dot_data = tree.export_graphviz(dec_tree, out_file=None, feature_names=list(features.columns.values),
                                     class_names=["No", "Yes"], filled=True, rounded=True, special_characters=True)

    graph = graphviz.Source(dot_data)
    graph.format = 'png'
    graph.render("./results/imgs/Decision-Tree-full", view=False)

    # First 3 layers of tree
    dot_data1 = tree.export_graphviz(dec_tree, out_file=None, feature_names=list(features.columns.values),
                                     class_names=["No", "Yes"], filled=True, rounded=True, special_characters=True,
                                     max_depth = 2)

    graph1 = graphviz.Source(dot_data1)
    graph1.format = 'png'
    graph1.render("./results/imgs/Decision-Tree-depth2", view=False)

    return dec_tree

if __name__ == "__main__":
    main()
