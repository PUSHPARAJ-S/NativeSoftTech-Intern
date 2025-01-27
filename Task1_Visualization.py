# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
# Replace 'your_dataset.csv' with the path to your dataset
try:
    data = pd.read_csv('your_dataset.csv')  # Example: 'data/sample.csv'
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Dataset not found. Please check the file path.")
    exit()

# Step 2: Inspect the Data
print("\n--- Dataset Overview ---")
print(data.head())
print("\n--- Dataset Info ---")
print(data.info())
print("\n--- Statistical Summary ---")
print(data.describe())

# Step 3: Data Cleaning
# Handle missing values
print("\n--- Checking for Missing Values ---")
print(data.isnull().sum())

# Drop rows with missing values
data_cleaned = data.dropna()
print("\nRows with missing values have been dropped.")

# Step 4: Data Manipulation
# Example: Filter rows where a numeric column is greater than a threshold
# Replace 'numeric_column' and 'threshold_value' with actual column name and value
filtered_data = data_cleaned[data_cleaned['numeric_column'] > 10]

# Example: Group by a categorical column and calculate the mean of a numeric column
# Replace 'category_column' and 'numeric_column' with actual column names
grouped_data = data_cleaned.groupby('category_column')['numeric_column'].mean()
print("\n--- Grouped Data ---")
print(grouped_data)

# Add a new column based on existing data
# Replace 'existing_column' and 'new_column' with actual column names
data_cleaned['new_column'] = data_cleaned['existing_column'] * 1.2

# Step 5: Data Visualization
# Plot 1: Histogram
plt.figure(figsize=(8, 5))
data_cleaned['numeric_column'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Numeric Column', fontsize=16)
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig('histogram.png')  # Save the plot as a PNG file
plt.show()

# Plot 2: Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x='category_column', y='numeric_column', data=data_cleaned)
plt.title('Boxplot of Numeric Column by Category', fontsize=16)
plt.savefig('boxplot.png')  # Save the plot as a PNG file
plt.show()

# Plot 3: Line Plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='time_column', y='value_column', data=data_cleaned)
plt.title('Trend Over Time', fontsize=16)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.savefig('lineplot.png')  # Save the plot as a PNG file
plt.show()

# Step 6: Save the Cleaned Data
# Save cleaned data to a new CSV file
data_cleaned.to_csv('cleaned_dataset.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_dataset.csv'.")
