import pandas as pd

# Load the dataset from local path
file_path = r"C:\yazwin\internship\project-3\dataset_3.xlsx"

# Read the Excel file
df = pd.read_excel(file_path, sheet_name="AB_NYC_2019")

# Task 2: Data Cleaning

# Handle Missing Values (Updated to avoid FutureWarning)
df = df.assign(
    name=df['name'].fillna('Unknown'),
    host_name=df['host_name'].fillna('Unknown'),
    reviews_per_month=df['reviews_per_month'].fillna(0),
    last_review=df['last_review'].fillna('No Reviews')
)

# Detect and Handle Outliers
price_threshold = 1000  # Adjust based on domain knowledge
min_nights_threshold = 365  # Unlikely for short-term rentals

df = df[df['price'] <= price_threshold]
df = df[df['minimum_nights'] <= min_nights_threshold]

# Standardize Data Types
if df['last_review'].dtype == 'object' and 'No Reviews' not in df['last_review'].unique():
    df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

# Final Review of Cleaned Data
print("Cleaned Data Summary:")
print(df.info())
print("\nMissing Values After Cleaning:\n", df.isnull().sum())
print("\nFirst Few Rows of Cleaned Data:\n", df.head())

# Save Cleaned Dataset
cleaned_file_path = r"C:\yazwin\internship\project-3\cleaned_dataset.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved at: {cleaned_file_path}")
