🚢 Data-Driven Survival Intelligence
Titanic – Analytical Investigation Using NumPy & Pandas
📌 Project Overview

This project analyzes the Titanic – Machine Learning from Disaster dataset to uncover survival patterns using:

✅ Python Lists

✅ NumPy

✅ Pandas

❌ No AutoML

❌ No direct ML libraries

The objective was to build:

Actionable insights

Feature engineering logic

A reproducible analytical workflow

A handcrafted survival scoring model

This project emphasizes data understanding over black-box modeling.

📂 Dataset

Dataset: Titanic – Machine Learning from Disaster

Source: Kaggle

Files Used:

train.csv

test.csv

gender_submission.csv

🧠 Project Structure
titanic-survival-intelligence/
│
├── notebook.ipynb
├── train.csv
├── test.csv
├── gender_submission.csv
├── report.pdf
└── README.md
🔍 Part 1 – Raw Data Exploration (Lists + NumPy Only)

✔ Loaded CSV manually using csv module
✔ Converted Age column into Python list
✔ Removed missing values manually
✔ Computed:

Mean age

Median age

Standard deviation

✔ Created NumPy Fare array
✔ Identified:

Top 10% fare passengers

Bottom 10% fare passengers

✔ Computed survival rates for:

Age < 15

Age 15–60

Age > 60

📊 Key Insight

Age is not linearly related to survival.
Children show significantly higher survival probability.

⚙️ Part 2 – Advanced Pandas Engineering
🔧 Missing Value Handling

Age → Median by Passenger Class

Embarked → Mode

🏗 Feature Engineering

FamilySize = SibSp + Parch + 1

IsAlone

FarePerPerson

🗂 Categorical Binning

AgeGroup → Child / Adult / Senior

FareGroup → Low / Medium / High

📊 Analysis

Survival by Gender & Class

Survival by FareGroup & Embarked

Correlation Matrix

🏆 Top Survival Influencers

Gender

Pclass

Fare

Family Size

Age

💡 Insight

Gender dominates wealth as a survival predictor.
Women survival probability exceeded wealthy male passengers.

🤖 Part 3 – NumPy-Based Survival Score (No ML Library)

A manual scoring formula was created:

SurvivalScore =
0.4 * Gender +
0.2 * Pclass +
0.1 * Age +
0.2 * Fare +
0.1 * FamilySize

✔ Numeric normalization using NumPy
✔ Threshold-based classification
✔ Manual evaluation metrics calculation

📈 Evaluation

Accuracy

Precision

Recall

Confusion Matrix (computed manually)

The handcrafted model significantly outperformed random guessing (50% baseline).

🧭 Part 4 – Executive Insights
🚑 Rescue Priority Model

If Titanic happened today, priority should be:

Women

Children

First-class passengers

⚖ Ethical Concerns

Gender bias

Wealth-based prioritization

Algorithmic fairness in life-critical decisions

🏦 Insurance Use Case

If applied to underwriting:

Remove sensitive attributes

Use probabilistic risk modeling

Focus on fairness-aware scoring

🎯 Bonus Challenge

✔ Vectorized NumPy-only survival grouping
✔ No loops used
✔ Custom predict_survival() function implemented

🛠 Technologies Used

Python 3.x

NumPy

Pandas

Jupyter Notebook

📊 Key Learning Outcomes

Manual statistical reasoning

Feature engineering logic

Bias interpretation

Model evaluation without ML libraries

Business-style interpretation of data

🚀 How to Run
pip install numpy pandas
jupyter notebook

📬 Author

Zenil Roy
Data & AI Enthusiast
Focused on building interpretable AI systems
