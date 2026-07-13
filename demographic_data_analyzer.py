import pandas as pd

columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "salary"
] 

df = pd.read_csv("adult.data", header=None, names=columns,skipinitialspace=True)

race_count = df["race"].value_counts()
print(race_count)

average_age_men = df[df["sex"] == "Male"]["age"].mean()
print(average_age_men)

percentage_bachelors = ((df['education'] == "Bachelors").sum() / len(df))*100
print(percentage_bachelors)

advanced = df[
    df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )
]

advanced_rich = advanced[
    advanced["salary"] == ">50K"
]

percentage = (
    len(advanced_rich)
    /
    len(advanced)
) * 100

print(percentage)

min_hours = df["hours-per-week"].min()

print(min_hours)

workers = df[
    df["hours-per-week"] == min_hours
]


rich_workers = workers[
    workers["salary"] == ">50K"
]

percentage = (
    len(rich_workers)
    /
    len(workers)
) * 100

print(percentage)

i awnna that data how can i download it

For the Demographic Data Analyzer project (freeCodeCamp), the dataset is the Adult Census Income dataset from the UCI Machine Learning Repository.

You can download it like this:

Option 1 (easiest): Download from GitHub
Open this link:
Adult Census Income dataset (GitHub mirror)
Click Download raw file (or Raw → Save As).
Save it in your project folder as:
adult.data.csv

Your project structure:

demographic-data-analyzer/
│
├── main.py
├── adult.data.csv
└── README.md
Option 2: Download directly from UCI

Go to the UCI repository:

UCI Machine Learning Repository - Adult Dataset

Download:

adult.data
adult.test

Rename:

adult.data → adult.data.csv
Then in VS Code:

Open your folder:

File → Open Folder → demographic-data-analyzer

Install pandas:

pip install pandas

Test:

import pandas as pd

df = pd.read_csv("adult.data.csv")
print(df.head())

If you see rows of data, you are ready.

Then you can create:

main.py

and start the freeCodeCamp project.

After finishing, push it to GitHub:

git init
git add .
git commit -m "Demographic Data Analyzer"
git branch -M main
git remote add origin YOUR_GITHUB_LINK
git push -u origin main

This is the normal VS Code + GitHub way; you don't need a paid environment.


Adult
Donated on 4/30/1996
Predict whether annual income of an individual exceeds $50K/yr based on census data. Also known as "Census Income" dataset.

Dataset Characteristics
Multivariate

Subject Area
Social Science

Associated Tasks
Classification

Feature Type
Categorical, Integer

# Instances
48842

# Features
14

Dataset Information
Additional Information

Extraction was done by Barry Becker from the 1994 Census database.  A set of reasonably clean records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0))

Prediction task is to determine whether a person's income is over $50,000 a year.

Has Missing Values?

Yes 

Variables Table
Variable Name	Role	Type	Demographic	Description	Units	Missing Values
age	Feature	Integer	Age	N/A		no
workclass	Feature	Categorical	Income	Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.		yes
fnlwgt	Feature	Integer				no
education	Feature	Categorical	Education Level	Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.		no
education-num	Feature	Integer	Education Level			no
marital-status	Feature	Categorical	Other	Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.		no
occupation	Feature	Categorical	Other	Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.		yes
relationship	Feature	Categorical	Other	Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.		no
race	Feature	Categorical	Race	White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.		no
sex	Feature	Binary	Sex	Female, Male.		no
Rows per page 
0 to 10 of 15

Additional Variable Information

Listing of attributes:

>50K, <=50K.

age: continuous.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
fnlwgt: continuous.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
education-num: continuous.
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
capital-gain: continuous.
capital-loss: continuous.
hours-per-week: continuous.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

Baseline Model Performance
Dataset Files
File	Size
adult.data	3.8 MB
adult.test	1.9 MB
adult.names	5.1 KB
old.adult.names	4.2 KB
Index	140 Bytes
Papers Citing this Dataset
Integrating Association Rules with Decision Trees in Object-Relational Databases
By Maruthi Ayyagari. 2019

Published in International Journal of Engineering Trends and Technology 67.3 (2019): 102-108.

Outis: Crypto-Assisted Differential Privacy on Untrusted Servers
By Amrita Chowdhury, Chenghong Wang, Xi He, Ashwin Machanavajjhala, Somesh Jha. 2019

Published in ArXiv.

Refining the Structure of Neural Networks Using Matrix Conditioning
By Roozbeh Yousefzadeh, Dianne O'Leary. 2019

Published in ArXiv.

Fair k-Center Clustering for Data Summarization
By Matthaus Kleindessner, Pranjal Awasthi, Jamie Morgenstern. 2019

Published in ArXiv.

Effectiveness of Equalized Odds for Fair Classification under Imperfect Group Information
By Pranjal Awasthi, Matthaus Kleindessner, Jamie Morgenstern. 2019

Published in ArXiv.

Rows per page 
0 to 5 of 257


Install the ucimlrepo package 
pip install ucimlrepo
Import the dataset into your code 
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
adult = fetch_ucirepo(id=2) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
# metadata 
print(adult.metadata) 
  
# variable information 
print(adult.variables) 
View the full documentation
257 citations
672732 views
Citation
Becker, B. & Kohavi, R. (1996). Adult [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20.
Style:
Keywords
census
Creators
Barry Becker

Silicon Graphics

Ronny Kohavi

ronnyk@live.com

Consultant/Stanford

DOI
10.24432/C5XW20
License
This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.

This allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given.

By using the UCI Machine Learning Repository, you acknowledge and accept the cookies and privacy practices used by the UCI Machine Learning Repository.

     is it this

Yes ✅ this is the correct dataset for the freeCodeCamp Demographic Data Analyzer project.

You need the file:

adult.data

(or adult.csv after renaming it)

You do not need:

❌ adult.names
❌ old.adult.names
❌ adult.test (unless you want extra testing data)
Download it:

On the UCI page you are on:

Scroll to Dataset Files
Click:
adult.data

Download it.

Put it in your VS Code project folder:
demographic-data-analyzer/
│
├── main.py
├── adult.data
└── README.md

You can rename it:

adult.data → adult.csv
Important: The dataset has no column names

The first row is data, so in Python you need to add the column names manually:

import pandas as pd

columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "salary"
]

df = pd.read_csv(
    "adult.csv",
    names=columns,
    skipinitialspace=True
)

print(df.head())

You should see:

   age workclass fnlwgt education ... native-country salary
0   39 State-gov 77516 Bachelors ... United-States <=50K
1   50 Self-emp 83311 Bachelors ... United-States <=50K
...

Then you can start solving the freeCodeCamp questions.

Your setup will be exactly like a real GitHub data science project:

Python
pandas
dataset
analysis
GitHub README

No paid environment needed.

i ama donloading an sdult.zip

Yes, that's also fine ✅

The adult.zip file is just a compressed folder containing the dataset files.

After downloading:

Open adult.zip
Extract it (Right click → Extract All)
You should see files like:
adult.data
adult.test
adult.names
old.adult.names

For the freeCodeCamp Demographic Data Analyzer, use only:

adult.data

Move it into your project folder:

demographic-data-analyzer/
│
├── main.py
├── adult.data
└── README.md

Then in Python you can load it:

import pandas as pd

df = pd.read_csv("adult.data", header=None)

print(df.head())

Later you will add the column names required by the project.

So yes — adult.zip from UCI is the correct download. 👍

well done know what is the required things to do expalin to me everthing am abiggener

Great 👍 Now you have the dataset. I will explain the Demographic Data Analyzer project from zero, like you are a beginner.

This project is a Data Analysis project using Python + pandas.

Your goal is:

Take census data about people and answer questions about age, education, race, income, work, etc.

You are not building an AI model here. You are learning how to clean, explore, and analyze data.

1) Create your project folder

Create a folder:

demographic-data-analyzer

Inside it:

demographic-data-analyzer/
│
├── main.py
├── adult.data
└── README.md

main.py = your Python code
adult.data = your dataset
README.md = explanation for GitHub

2) Install the tool you need

You need pandas.

Open VS Code terminal:

Terminal → New Terminal

Write:

pip install pandas

Pandas is a Python library that helps you work with tables.

Example:

A dataset looks like an Excel table:

age	education	salary
39	Bachelors	<=50K
50	Masters	>50K

Pandas lets Python read and analyze this.

3) Import the dataset

The dataset has no column names.

So first we give names to the columns.

Your main.py starts like this:

import pandas as pd


columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "salary"
]


df = pd.read_csv(
    "adult.data",
    names=columns,
    skipinitialspace=True
)


print(df.head())

Run:

python main.py

You should see the first 5 people.

4) Understand your data

The dataset has:

Rows

Each row = one person

Example:

39, State-gov, Bachelors, Male, <=50K

means:

A person:

age 39
works for government
has Bachelor's degree
male
earns <=50K
Columns

Each column is information about the person.

Examples:

age

Person's age:

39
50
28
education

Education level:

Bachelors
Masters
HS-grad
Doctorate
salary

The thing we want to analyze:

<=50K
>50K

Meaning:

Income less or equal than $50,000

or

Income above $50,000

5) The project questions

freeCodeCamp gives you questions.

You need to answer them using pandas.

Question 1
How many people of each race are represented?

Meaning:

Count people by race.

Example output:

White                 27816
Black                  3124
Asian-Pac-Islander     1039

You learn:

df["race"].value_counts()
Question 2
What is the average age of men?

Meaning:

Filter:

Only men

Then calculate average age.

Concepts:

Filtering

Example:

df[df["sex"] == "Male"]

Means:

"Give me only rows where sex is Male"

Average:

.mean()
Question 3
What percentage of people have a Bachelor's degree?

You need:

Count people with:

education = Bachelors

Divide by total people.

Formula:

percentage =
(number with bachelors / total people) * 100
Question 4
What percentage of people with advanced education earn >50K?

Advanced education means:

Bachelors
Masters
Doctorate

You filter:

People with these degrees

AND

salary >50K

Question 5
What is the minimum number of hours a person works per week?

Find:

hours-per-week

minimum value.

Function:

.min()
Question 6
Who earns >50K and works the minimum hours?

First:

Find minimum hours.

Then:

Find people who:

salary >50K
AND
hours = minimum
Question 7
What country has the highest percentage of people earning >50K?

Example:

United-States 25%
Canada 30%
India 20%

Find the highest.

Question 8
Identify the most popular occupation for people in India earning >50K

Filter:

Country:

India

Income:

>50K

Then count occupations.

6) Skills you learn from this project

After finishing, you will understand:

✅ Loading datasets
✅ Pandas DataFrames
✅ Selecting columns
✅ Filtering rows
✅ Counting values
✅ Calculating averages
✅ Percentages
✅ Grouping data
✅ Cleaning data
✅ Writing a data analysis report

These are real Data Analyst skills.

7) Your learning path while doing it

Don't copy everything immediately.

Do it like this:

Day 1
Download dataset
Load it
Understand rows and columns
Day 2
Learn:
head()
info()
describe()
Day 3
Solve first 3 questions
Day 4
Solve remaining questions
Day 5
Clean code
Add README
Push to GitHub

For a beginner, this is actually a very good first data science project. It teaches you the workflow used in real projects.

answear the questions and explain

Good. I will solve the Demographic Data Analyzer questions and explain the logic behind each one.

First, your main.py should have the dataset loaded:

import pandas as pd

columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "salary"
]

df = pd.read_csv(
    "adult.data",
    names=columns,
    skipinitialspace=True
)
1) How many people of each race are represented?
Question meaning:

"Count how many people belong to each race."

We use:

race_count = df["race"].value_counts()
print(race_count)
Explanation:

df["race"]

means:

Take only the race column.

Example:

White
Black
White
Asian-Pac-Islander
White

value_counts()

counts each category:

Output:

race
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
2) What is the average age of men?
Question meaning:

Only look at males, then calculate their average age.

Code:

average_age_men = df[df["sex"] == "Male"]["age"].mean()

print(average_age_men)
Explanation:

First:

df["sex"] == "Male"

creates a filter:

Male → keep
Female → remove

Then:

["age"]

takes their ages.

Then:

.mean()

calculates:

sum of ages / number of men

Example:

20 + 30 + 40 = 90

90 / 3 = 30
3) What percentage of people have a Bachelor's degree?
Meaning:

How many people have:

education = Bachelors

compared to everyone.

Code:

percentage_bachelors = (
    (df["education"] == "Bachelors").sum()
    / len(df)
) * 100

print(percentage_bachelors)
Explanation:

This:

df["education"] == "Bachelors"

creates:

True
False
True
False

Python counts True as 1:

True + True = 2

Then:

number of bachelors / total people × 100
4) Percentage of people with advanced education earning >50K

Advanced education:

Bachelors
Masters
Doctorate

Code:

advanced = df[
    df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )
]

advanced_rich = advanced[
    advanced["salary"] == ">50K"
]

percentage = (
    len(advanced_rich)
    /
    len(advanced)
) * 100

print(percentage)
Explanation:

First:

isin()

means:

"Is the education one of these?"

Example:

Bachelors → yes
HS-grad → no
Masters → yes

Then:

advanced people
        |
        ↓
who earn >50K

Then calculate percentage.

5) What is the minimum number of hours a person works per week?

Code:

min_hours = df["hours-per-week"].min()

print(min_hours)

Explanation:

The column:

hours-per-week

contains:

40
50
20
60

.min() finds the smallest:

20
6) What percentage of people who work minimum hours earn >50K?

First:

Find minimum hours:

min_hours = df["hours-per-week"].min()

Then:

People working those hours:

workers = df[
    df["hours-per-week"] == min_hours
]

People earning >50K:

rich_workers = workers[
    workers["salary"] == ">50K"
]

Percentage:

percentage = (
    len(rich_workers)
    /
    len(workers)
) * 100

print(percentage)

country_percentage = (
    df.groupby("native-country")["salary"]
    .apply(lambda x: (x == ">50K").mean() * 100)
)

print(country_percentage.idxmax())