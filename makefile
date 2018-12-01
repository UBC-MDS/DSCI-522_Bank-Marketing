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

#Create Exploratory Data Analysis
#plot all variables
./results/imgs/age.png: ./data/cleaned/bank_full.csv $(age) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv age ./results/imgs/age.png

./results/imgs/job.png: ./data/cleaned/bank_full.csv $(job) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv job ./results/imgs/job.png

./results/imgs/marital.png: ./data/cleaned/bank_full.csv $(marital) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv marital ./results/imgs/marital.png

./results/imgs/education.png: ./data/cleaned/bank_full.csv $(education) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv education ./results/imgs/education.png

./results/imgs/default.png: ./data/cleaned/bank_full.csv $(default) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv default ./results/imgs/default.png

./results/imgs/housing.png: ./data/cleaned/bank_full.csv $(housing) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv housing ./results/imgs/housing.png

./results/imgs/loan.png: ./data/cleaned/bank_full.csv $(loan) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv loan ./results/imgs/loading.png

./results/imgs/contact.png: ./data/cleaned/bank_full.csv $(contact) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv contact ./results/imgs/contact.png

./results/imgs/month.png: ./data/cleaned/bank_full.csv $(month) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv month ./results/imgs/month.png

./results/imgs/day_of_week.png: ./data/cleaned/bank_full.csv $(day_of_week) scripts/data_vis.py)
	python scripts/data_vis.py ./data/cleaned/bank_full.csv day_of_week ./results/imgs/day_of_week.png

./results/imgs/pdays.png: ./data/cleaned/bank_full.csv $(pdays) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv campaign ./results/imgs/pdays.png

./results/imgs/previous.png: ./data/cleaned/bank_full.csv $(previous) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv previous ./results/imgs/previous.png

./results/imgs/campaign.png: ./data/cleaned/bank_full.csv $(campaign) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv campaign ./results/imgs/campaign.png

./results/imgs/poutcome.png: ./data/cleaned/bank_full.csv $(poutcome) scripts/data_vis.py
	python scripts/data_vis.py ./data/cleaned/bank_full.csv poutcome ./results/imgs/poutcome.png


# Build Decision Tree Classifier
./results/decision-tree-output.csv: ./data/cleaned/bank_full.csv  scripts/create-decision-tree.py
	python scripts/create-decision-tree.py ./data/cleaned/bank_full.csv ./results/decision-tree-output.csv

# Generate the final report

documents/Bank-Marketing-Findings.md: ./documents/Bank-Marketing-Findings.Rmd ./results/imgs/Cross-Validation-Scores.png ./results/imgs/Decision-Tree-depth2.png ./results/Feature_Importance.csv ./results/decision-tree-output.csv
	Rscript -e "rmarkdown::render('./documents/Bank-Marketing-Findings.Rmd')"

#Clean up intermediate files
clean:
#remove output from loading and cleaning stage
	rm -f ./data/cleaned/bank_full.csv
#remove output from EDA stage
	rm -f ./results/imgs/*.png

#clean final report rendered in html format
	rm -f documents/Bank-Marketing-Findings.html
