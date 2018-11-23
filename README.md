# Bank Marketing
----------------------------------
### Team members:

* Brenden Everitt (github id : everittb)

* Sabrina Kakei Tse (github id: sabrinatkk)

--------------------------------------------------
## Proposal Outline:

### 1. Dataset:

Source: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing

[Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014

#### Inputs = 16 attributes of existing bank customers and datatype

1. age: numeric
2. job : categorical
3. marital :categorical
4. education: categorical
5. default: has credit in default? - binary
6. balance: numeric
7. housing: has housing loan? binary
8. loan: has personal loan? binary

_related with the last contact of the current campaign_

9. contact: categorical
10. day: numeric
11. month: categorical
12. duration: numeric

_other attributes_

13. campaign: numeric
14. pdays: numeric
15. previous: numeric
16. poutcome:  categorical

_social and economic attributes_(not included in this study)
17. ~~emp.var.rate:numeric~~
18. ~~cons.price.idx: numeric~~
19. ~~cons.conf.idx: numeric~~
20. ~~euribor3m:numeric~~
21. ~~nr.employed: numeric~~



source:https://archive.ics.uci.edu/ml/datasets/Bank+Marketing


### 2. Question
**Type:** Predictive

_Will an existing bank customer subscribe to a new term deposit through a direct marketing campaign?_

### 3. Script

**Summary of the data:**

![](./results/imgs/data_loaded.jpg)  

The dataset was generated by a phone marketing campaign run by a Portuguese bank . The campaign aimed to encourage the bank's existing customers to sign up for a new term deposit. The dataset contains ~45,000 examples with both quantitative and qualitative data on 20 features for each customer.  The dataset also includes the final result of the campaign that indicates the successful sign-ups.  


**Language:** Python
  - **Dependencies:**
    1. Pandas

### 4. Plan

We are going to build a Decision Tree Classifier to identify which characteristics of the clientele will lead to subscription to the new bank product.

1. **Importing and cleaning data**- For variables, we will only consider the 16 customers' attributes, and drop the social and economic attributes because they are macro-economic factors that are not directly related to the customers that we want to study.


2. **Hyperparameter for Decision Tree** - we will use k-fold cross-validation to pick the maximum depth of the tree.


### 5. Presentation:

- [ ] Decision Tree Model to predict whether or not an existing customer will sign up for a new bank product through the new marketing campaign. We will provide:

  - The full tree in pdf as a reference
  - The top three layers of the tree
  - Present the prediction result for 2-3 customers
  - Test accuracy for the final model  


- [ ] Table to summarize the features selected by the classifier

  - This table ranks all of the customer features used in the model by Gini importance
