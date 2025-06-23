import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("titanic")
print(df.head())
sns.set(style="darkgrid")

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='sex', hue='survived', palette='Set1')
plt.title('Survivors by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='pclass', y='survived', palette='Set2')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='pclass', y='age', palette='Set3')
plt.title('Age Distribution by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()

plt.figure(figsize=(6, 4))
sns.violinplot(data=df, x='sex', y='age', hue='survived', split=True, palette='Pastel1')
plt.title('Age Distribution and Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

selected_features = df[['survived', 'age', 'fare', 'pclass']]
sns.pairplot(selected_features, hue='survived', palette='husl')
plt.suptitle("Pair Plot of Age, Fare, Pclass & Survival", y=1.02)
plt.show()
