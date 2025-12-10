# Future Sales Prediction using Linear Regression

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 2. Load dataset
data = pd.read_csv("futuresale prediction.csv")
print("Dataset shape:", data.shape)
print(data.head())

# 3. Check for missing values
print("\nMissing values:\n", data.isnull().sum())

# 4. Correlation analysis
plt.figure(figsize=(8,6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 5. Features and target
X = data.drop("Sales", axis=1)   # predictors: TV, Radio, Newspaper
y = data["Sales"]                # target: Sales

# 6. Train-test split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Train Linear Regression model
model = LinearRegression()
model.fit(xtrain, ytrain)

# 8. Predictions
y_pred = model.predict(xtest)

# 9. Evaluation
mae = mean_absolute_error(ytest, y_pred)
rmse = np.sqrt(mean_squared_error(ytest, y_pred))
r2 = r2_score(ytest, y_pred)

print("\nModel Performance:")
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R² Score:", r2)

# 10. Predict future sales for new advertising spend
new_features = np.array([[230.1, 37.8, 69.2]])  # Example: TV, Radio, Newspaper
future_sales = model.predict(new_features)
print("\nPredicted Future Sales for [TV=230.1, Radio=37.8, Newspaper=69.2]:", future_sales[0])
