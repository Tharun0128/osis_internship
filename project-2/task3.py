import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# File path
file_path = r'C:\yazwin\internship\project-2\Online Retail.xlsx'

# Load dataset
data = pd.read_excel(file_path)

# Preview data
print("Dataset Preview:")
print(data.head())

# Feature Engineering: Create 'Total_Spending' and 'Frequency'
data['Total_Spending'] = data['Quantity'] * data['UnitPrice']  # Total Spending
customer_data = data.groupby('CustomerID').agg({
    'Total_Spending': 'sum',
    'InvoiceDate': 'count'  # Frequency of purchases
}).rename(columns={'InvoiceDate': 'Frequency'}).reset_index()

# Standardize the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_data[['Total_Spending', 'Frequency']])

# Determine the optimal number of clusters using Elbow Method
inertia = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o')
plt.title('Elbow Method to Determine Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.grid()
plt.show()

# Apply K-Means with the chosen number of clusters (e.g., 4)
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(scaled_features)

# Analyze Clusters
print("\nCluster Analysis:")
cluster_summary = customer_data.groupby('Cluster').agg({
    'Total_Spending': ['mean', 'sum'],
    'Frequency': ['mean', 'sum'],
    'CustomerID': 'count'
}).rename(columns={'CustomerID': 'Count'})
print(cluster_summary)

# Visualize Clusters
plt.figure(figsize=(10, 7))
sns.scatterplot(
    x=scaled_features[:, 0],
    y=scaled_features[:, 1],
    hue=customer_data['Cluster'],
    palette='viridis',
    s=100
)
plt.title('Customer Segmentation Based on Spending and Frequency')
plt.xlabel('Total Spending (Standardized)')
plt.ylabel('Frequency (Standardized)')
plt.legend(title='Cluster')
plt.grid()
plt.show()

# Save clustered data
output_path = r'C:\yazwin\customer_segmentation.csv'
customer_data.to_csv(output_path, index=False)
print(f"\nClustered data saved to {output_path}")
