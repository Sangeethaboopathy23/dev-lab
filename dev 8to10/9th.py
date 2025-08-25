# Ex. No: 8 - EDA Case Study on Wine Dataset
# Aim: Perform EDA and visualization on sklearn Wine dataset (no CSV needed)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

plt.close('all')

wine = load_wine(as_frame=True)
df = wine.frame.rename(columns={"target": "class"})
feature_cols = [c for c in df.columns if c != "class"]

print("\nShape:", df.shape)
print("\nHead:\n", df.head())
print("\nInfo:")
print(df.info())
print("\nDescribe (features):\n", df[feature_cols].describe())
print("\nMissing values per column:\n", df.isna().sum())
print("\nClass distribution:\n", df["class"].value_counts().sort_index())

corr = df[feature_cols].corr(numeric_only=True)
plt.figure(figsize=(11, 8))
sns.heatmap(corr, annot=False, cmap="coolwarm", center=0, square=False)
plt.title("Correlation Heatmap (Wine Features)")
plt.tight_layout()
plt.show()

df[feature_cols].hist(bins=15, figsize=(14, 10))
plt.suptitle("Univariate Distributions of Wine Features", y=1.02)
plt.tight_layout()
plt.show()

top_pairs = [("flavanoids", "class"),
             ("od280/od315_of_diluted_wines", "class"),
             ("color_intensity", "class"),
             ("proline", "class"),
             ("total_phenols", "class"),
             ("alcohol", "class")]

for feat, grp in top_pairs:
    plt.figure(figsize=(7, 4))
    sns.boxplot(data=df, x=grp, y=feat)
    sns.stripplot(data=df, x=grp, y=feat, size=3, alpha=0.45, color="k")
    plt.title(f"{feat} by {grp}")
    plt.tight_layout()
    plt.show()

pair_feats = ["flavanoids", "od280/od315_of_diluted_wines", "color_intensity", "proline", "alcohol"]
sns.pairplot(df[pair_feats + ["class"]], hue="class", diag_kind="hist", corner=True, plot_kws={"s": 25, "alpha": 0.8})
plt.suptitle("Pairwise Relationships of Top Features", y=1.02)
plt.show()

def iqr_outliers(s: pd.Series, k: float = 1.5):
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    lo, hi = q1 - k * iqr, q3 + k * iqr
    return ((s < lo) | (s > hi)).sum(), lo, hi

outlier_summary = []
for col in feature_cols:
    n_out, lo, hi = iqr_outliers(df[col])
    outlier_summary.append({"feature": col, "n_outliers": int(n_out), "lower_bound": lo, "upper_bound": hi})
outlier_df = pd.DataFrame(outlier_summary).sort_values("n_outliers", ascending=False)
print("\nPotential outliers (IQR rule):\n", outlier_df.head(10))

plt.figure(figsize=(9, 5))
sns.barplot(data=outlier_df, x="n_outliers", y="feature", orient="h")
plt.title("Outlier Counts per Feature (IQR rule)")
plt.xlabel("Count")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()
