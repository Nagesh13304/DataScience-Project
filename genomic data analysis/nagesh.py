import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load genomic dataset (ensures the file exists before loading)
data_file = "genomic_data.csv"
if not os.path.exists(data_file):
    raise FileNotFoundError(f"The file '{data_file}' does not exist. Please provide the correct path.")

data = pd.read_csv(data_file)

# Display basic information about the dataset
print("Dataset Info:")
data.info()
print("\nFirst few rows of the dataset:")
print(data.head())

# Check for missing values
missing_values = data.isnull().sum()
print("\nMissing Values:")
print(missing_values[missing_values > 0])

# Summary statistics for numeric columns
print("\nSummary Statistics:")
print(data.describe())

# Plot distribution of numeric columns
numeric_cols = data.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(data[col], kde=True, bins=30)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

# Visualize correlation between numeric columns
plt.figure(figsize=(10, 8))
corr_matrix = data[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Check for categorical columns
categorical_cols = data.select_dtypes(include=["object", "category"]).columns
print("\nCategorical Columns:")
print(categorical_cols)

# Visualize distributions of categorical columns
for col in categorical_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(data[col], order=data[col].value_counts().index)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# Detect outliers using boxplots for numeric columns
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data[col])
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.show()

# Advanced visualization: Pairplot for numeric columns
if len(numeric_cols) > 1:
    sns.pairplot(data[numeric_cols], diag_kind="kde")
    plt.suptitle("Pairplot of Numeric Features", y=1.02)
    plt.show()

# Detecting skewness in numeric data
skewness = data[numeric_cols].skew()
print("\nSkewness of Numeric Columns:")
print(skewness)

# Example genomic-specific visualization: GC content analysis
if "GC_Content" in data.columns:
    plt.figure(figsize=(8, 4))
    sns.histplot(data["GC_Content"], kde=True, bins=30)
    plt.title("Distribution of GC Content")
    plt.xlabel("GC Content (%)")
    plt.ylabel("Frequency")
    plt.show()

# Save cleaned data (optional)
# Replace 'cleaned_genomic_data.csv' with your desired file name
# data.to_csv("cleaned_genomic_data.csv", index=False)

print("EDA completed.")
