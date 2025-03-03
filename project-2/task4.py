import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\yazwin\internship\project-2\Online Retail.xlsx'
data = pd.read_excel(file_path)

# Add the Monetary column
data['Monetary'] = data['Quantity'] * data['UnitPrice']

# Visualize the Monetary distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Monetary'], kde=True, bins=30, color='blue')
plt.title('Distribution of Monetary Values')
plt.xlabel('Monetary Value')
plt.ylabel('Frequency')
plt.show()

# Visualize the Quantity distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Quantity'], kde=True, bins=30, color='green')
plt.title('Distribution of Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between Quantity and UnitPrice
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['Quantity'], y=data['UnitPrice'], alpha=0.5)
plt.title('Quantity vs. Unit Price')
plt.xlabel('Quantity')
plt.ylabel('Unit Price')
plt.show()

# Visualize the top 10 countries with the highest monetary value
top_countries = data.groupby('Country')['Monetary'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.index, y=top_countries.values, palette='viridis')
plt.title('Top 10 Countries by Total Monetary Value')
plt.xlabel('Country')
plt.ylabel('Total Monetary Value')
plt.xticks(rotation=45)
plt.show()

# Visualize the top 10 customers with the highest monetary value
top_customers = data.groupby('CustomerID')['Monetary'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_customers.index.astype(str), y=top_customers.values, palette='coolwarm')
plt.title('Top 10 Customers by Total Monetary Value')
plt.xlabel('Customer ID')
plt.ylabel('Total Monetary Value')
plt.xticks(rotation=45)
plt.show()
