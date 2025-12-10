# --- Fix for NumPy bool8 removal ---
import numpy as np
if not hasattr(np, "bool8"):
    np.bool8 = np.bool_

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

# Load dataset
data = pd.read_csv("CREDITSCORE.csv")
print(data.head())
print(data.info())

# Features and target
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary", 
                   "Num_Bank_Accounts", "Num_Credit_Card", 
                   "Interest_Rate", "Num_of_Loan", 
                   "Delay_from_due_date", "Num_of_Delayed_Payment", 
                   "Credit_Mix", "Outstanding_Debt", 
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data["Credit_Score"])   # 1D array

# Train-test split
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.33, random_state=42)

# Train model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(xtrain, ytrain)

# Evaluate model
from sklearn.metrics import accuracy_score, classification_report
ypred = model.predict(xtest)
print("Model Accuracy:", accuracy_score(ytest, ypred))
print(classification_report(ytest, ypred))

# --- Prediction from user input ---
print("\nCredit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = int(input("Credit Mix (Bad: 0, Standard: 1, Good: 3): "))  # FIXED
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
print("Predicted Credit Score =", model.predict(features)[0])
