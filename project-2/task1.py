import pandas as pd

# File path
file_path = r'C:\yazwin\internship\project-2\Online Retail.xlsx'
# Step 1: Load the dataset
data = pd.read_excel(file_path)

# Step 2: Inspect the dataset
print("Dataset Info:")
print(data.info())
print("\nMissing Values:")
print(data.isnull().sum())
print("\nColumn Names:")
print(data.columns)

# Step 3: Handle missing values
data_cleaned = data.dropna()
print(f"\nRows removed due to missing values: {len(data) - len(data_cleaned)}")

# Step 4: Check and remove duplicates
print(f"Duplicate rows before cleaning: {data_cleaned.duplicated().sum()}")
data_cleaned = data_cleaned.drop_duplicates()
print(f"Duplicate rows after cleaning: {data_cleaned.duplicated().sum()}")

# Step 5: Convert data types (e.g., InvoiceDate)
data_cleaned['InvoiceDate'] = pd.to_datetime(data_cleaned['InvoiceDate'])
print("\nUpdated Data Types:")
print(data_cleaned.dtypes)

# Step 6: Save the cleaned dataset
cleaned_file_path = r'C:\Users\yazwi\Downloads\Online_Retail_Cleaned.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned dataset saved to: {cleaned_file_path}")
