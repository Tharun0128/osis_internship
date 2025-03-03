import pandas as pd

# File path for the dataset
file_path = r'C:\yazwin\internship\project-2\Online Retail.xlsx'

# Load the dataset
data = pd.read_excel(file_path)

# Display the first few rows to confirm loading
print("Dataset Preview:")
print(data.head())

# Generate descriptive statistics
print("\nDescriptive Statistics:")
descriptive_stats = data.describe(include='all')  # Include both numerical and categorical data
print(descriptive_stats)

# Save descriptive statistics to a CSV file
output_path = r'C:\yazwin\descriptive_statistics.csv'
descriptive_stats.to_csv(output_path, index=True)
print(f"\nDescriptive statistics saved to {output_path}")
