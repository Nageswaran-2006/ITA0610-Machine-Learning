import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Dataset
data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain'],
    'Temperature':['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild'],
    'Humidity':['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal'],
    'Wind':['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak'],
    'Play':['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes']
}

df = pd.DataFrame(data)

# Convert categorical values to numbers
df_encoded = df.apply(lambda col: pd.factorize(col)[0])

X = df_encoded.iloc[:, :-1]
y = df_encoded.iloc[:, -1]

model = DecisionTreeClassifier(criterion='entropy')  # ID3 uses entropy
model.fit(X, y)

print("Decision Tree built successfully!")

# Plot tree
plt.figure(figsize=(10,6))
plot_tree(model, feature_names=X.columns, filled=True)
plt.show()

# CLASSIFY NEW SAMPLE
new_sample = pd.DataFrame({
    'Outlook':['Sunny'],
    'Temperature':['Cool'],
    'Humidity':['High'],
    'Wind':['Weak']
})

new_sample_encoded = new_sample.apply(lambda col: pd.factorize(df[col.name])[0][0])
prediction = model.predict([new_sample_encoded])

print("New Sample Prediction:", "Play" if prediction[0] == 1 else "No")
