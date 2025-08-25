import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "fixed acidity": [7.4, 7.8, 7.8, 11.2, 7.4, 7.4, 7.9, 7.3, 7.8, 7.5],
    "volatile acidity": [0.70, 0.88, 0.76, 0.28, 0.70, 0.66, 0.60, 0.65, 0.58, 0.50],
    "citric acid": [0.00, 0.00, 0.04, 0.56, 0.00, 0.00, 0.06, 0.00, 0.02, 0.36],
    "residual sugar": [1.9, 2.6, 2.3, 1.9, 1.9, 1.8, 1.6, 1.2, 2.0, 6.1],
    "chlorides": [0.076, 0.098, 0.092, 0.075, 0.076, 0.075, 0.069, 0.065, 0.073, 0.071],
    "free sulfur dioxide": [11, 25, 15, 17, 11, 13, 15, 15, 9, 17],
    "total sulfur dioxide": [34, 67, 54, 60, 34, 40, 59, 21, 18, 102],
    "density": [0.9978, 0.9968, 0.9970, 0.9980, 0.9978, 0.9978, 0.9964, 0.9956, 0.9968, 0.9978],
    "pH": [3.51, 3.20, 3.26, 3.16, 3.51, 3.51, 3.30, 3.39, 3.36, 3.35],
    "sulphates": [0.56, 0.68, 0.65, 0.58, 0.56, 0.56, 0.46, 0.54, 0.57, 0.80],
    "alcohol": [9.4, 9.8, 9.8, 9.8, 9.4, 9.4, 9.4, 10.0, 9.5, 10.5],
    "quality": [5, 5, 5, 6, 5, 5, 5, 7, 7, 5]
}

df = pd.DataFrame(data)

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.shape)
print(df['quality'].value_counts())

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

df.hist(bins=15, figsize=(15,10))
plt.suptitle("Feature Distributions")
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x="quality", y="alcohol", data=df)
plt.title("Alcohol vs Quality")
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x="quality", y="volatile acidity", data=df)
plt.title("Volatile Acidity vs Quality")
plt.show()
