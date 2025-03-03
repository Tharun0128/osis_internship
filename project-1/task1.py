import pandas as pd

# Step 1: Load the dataset
file_path = r'C:\Users\yazwi\Downloads\archive\Pubg_Stats.csv'  # Update if the file name is different
df = pd.read_csv(file_path)

# Step 2: Preview the dataset
print("Preview of the dataset:")
print(df.head())

# Step 3: Check the dataset structure
print("\nDataset structure:")
df.info()

# Step 4: Check for missing values
print("\nMissing values in each column:")
missing_values = df.isnull().sum()
print(missing_values)

# Optionally: Percentage of missing values
print("\nPercentage of missing values:")
print((missing_values / len(df)) * 100)

# Step 5: Remove unnecessary columns
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
    print("\nDropped 'Unnamed: 0' column.")

# Step 6: Check for duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicate rows removed.")

# Step 7: Check and convert data types if necessary
print("\nUpdated data types:")
print(df.dtypes)

# Step 8: Save the cleaned dataset
output_path = r'C:\Users\yazwi\Downloads\cleaned_pubg_stats.csv'  # Update the path if needed
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset saved as: {output_path}")
