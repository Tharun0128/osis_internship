import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
file_path = r"C:\yazwin\internship\project-3\cleaned_dataset.csv"
df = pd.read_csv(file_path)

# 1️⃣ Feature Engineering

# Extract year & month from 'last_review'
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
df['last_review_year'] = df['last_review'].dt.year
df['last_review_month'] = df['last_review'].dt.month

# Create price category
df['price_category'] = pd.cut(df['price'], bins=[0, 50, 200, 1000], labels=['Low', 'Medium', 'High'])

# Mark active & inactive hosts
df['host_status'] = df['reviews_per_month'].apply(lambda x: 'Active' if x > 0 else 'Inactive')

# 2️⃣ Exploratory Data Analysis (EDA)

# Top 5 neighborhoods with most listings
top_neighborhoods = df['neighbourhood'].value_counts().head(5)
print("\nTop 5 Neighborhoods with Most Listings:\n", top_neighborhoods)

# Most expensive neighborhoods (avg price)
expensive_neighborhoods = df.groupby('neighbourhood')['price'].mean().sort_values(ascending=False).head(5)
print("\nTop 5 Most Expensive Neighborhoods:\n", expensive_neighborhoods)

# Average price per room type
avg_price_room = df.groupby('room_type')['price'].mean()
print("\nAverage Price per Room Type:\n", avg_price_room)

# 3️⃣ Data Visualization

# Price distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Listings per room type
plt.figure(figsize=(8, 5))
sns.countplot(x='room_type', data=df, palette='coolwarm')
plt.title('Listings Per Room Type')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.show()

# 4️⃣ Save Transformed Data
transformed_file_path = r"C:\yazwin\internship\project-3\transformed_dataset.csv"
df.to_csv(transformed_file_path, index=False)
print(f"\nTransformed dataset saved at: {transformed_file_path}")
