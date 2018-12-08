#Driver Script For Bank Markerting
#Sabrina Kakei Tse, Brenden Everitt
#UBC MDS
#2018-12-01

# This driver script activates altogether four steps to create a predictive analysis using
# ~45000 existing bank customers and their attributes.
#
# usage: make all

#run all analysis

all: documents/Bank-Marketing-Findings.md

# Import and clean data

./data/cleaned/bank_full.csv: ./data/raw-data/bank-additional-full.csv scripts/data_loading-cleaning.py
	python scripts/data_loading-cleaning.py ./data/raw-data/bank-additional-full.csv ./data/cleaned/bank_full.csv

# Create Exploratory Data Analysis
# create csv and graph

./results/imgs/age_stat.csv: ./data/cleaned/bank_full.csv $(age) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv age ./results/imgs/age.png


# Build Decision Tree Classifier
./results/decision-tree-output.csv: ./data/cleaned/bank_full.csv  scripts/create-decision-tree.py
	python scripts/create-decision-tree.py ./data/cleaned/bank_full.csv ./results/decision-tree-output.csv

# Generate the final report

documents/Bank-Marketing-Findings.md: ./documents/Bank-Marketing-Findings.Rmd ./results/imgs/age_stat.csv ./results/decision-tree-output.csv
	Rscript -e "rmarkdown::render('./documents/Bank-Marketing-Findings.Rmd')"

# Clean up intermediate files
clean:
# remove output from loading and cleaning stage
	rm -f ./data/cleaned/bank_full.csv
# remove output from EDA stage
	rm -f ./results/age-stat.csv
	rm -f ./results/imgs/job_age.png
	rm -f ./results/imgs/job*.png
	rm -f ./results/imgs/age*.png

# Remove images create by the decision tree
	rm -f ./results/imgs/Cross-Validation-Scores.png
	rm -f ./results/Feature_Importance.csv
	rm -f ./results/decision-tree-output.csv
	rm -f ./results/imgs/Decision-Tree-depth2.png

# clean final report rendered in html format
	rm -f documents/Bank-Marketing-Findings.html
