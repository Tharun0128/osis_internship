import pandas as pd

# Step 1: Load the cleaned dataset
file_path = r'C:\Users\yazwi\Downloads\cleaned_pubg_stats.csv'  # Adjust path if necessary
df = pd.read_csv(file_path)

# Step 2: Calculate basic statistics for numerical columns
numerical_columns = df.select_dtypes(include=['int64']).columns

print("Descriptive statistics for numerical columns:")
print(df[numerical_columns].describe())  # Includes count, mean, std, min, 25%, 50%, 75%, max

# Step 3: Calculate median and mode for numerical columns
print("\nMedian values for numerical columns:")
print(df[numerical_columns].median())

print("\nMode values for numerical columns:")
print(df[numerical_columns].mode().iloc[0])  # Take the first row since mode() may return multiple values

# Step 4: Calculate variance and standard deviation
print("\nVariance for numerical columns:")
print(df[numerical_columns].var())

print("\nStandard deviation for numerical columns:")
print(df[numerical_columns].std())

# Step 5: Analyze categorical data
categorical_columns = df.select_dtypes(include=['object']).columns

print("\nUnique values in categorical columns:")
for col in categorical_columns:
    print(f"{col}: {df[col].nunique()} unique values")

print("\nMost frequent values in categorical columns:")
for col in categorical_columns:
    print(f"{col}: {df[col].mode()[0]} (Mode)")

# Optional: Save the descriptive statistics to a CSV
output_path = r'C:\Users\yazwi\Downloads\descriptive_statistics.csv'  # Adjust path if necessary
stats = df[numerical_columns].describe().transpose()
stats['Median'] = df[numerical_columns].median()
stats['Variance'] = df[numerical_columns].var()
stats['Standard Deviation'] = df[numerical_columns].std()
stats.to_csv(output_path)

print(f"\nDescriptive statistics saved as: {output_path}")
