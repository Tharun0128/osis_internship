import pandas as pd

# Load the dataset
file_path = "C:\yazwin\internship\project-3\dataset_3.xlsx"
df = pd.read_excel(file_path, sheet_name="AB_NYC_2019")

# Step 1: Display basic information about the dataset
print("Dataset Information:")
df.info()
print("\nFirst 5 Rows:\n", df.head())

# Step 2: Check for duplicate records
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# Step 3: Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values Per Column:\n", missing_values)

# Step 4: Identify unique values in key categorical columns
print("\nUnique values in 'room_type':", df['room_type'].unique())
print("Unique values in 'neighbourhood_group':", df['neighbourhood_group'].unique())

# Step 5: Check for invalid values in numerical columns
print("\nSummary Statistics:")
print(df.describe())
