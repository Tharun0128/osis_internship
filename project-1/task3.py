import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the cleaned dataset
file_path = r'C:\Users\yazwi\Downloads\cleaned_pubg_stats.csv'  # Update the path if needed
df = pd.read_csv(file_path)

# Step 2: Check if there's a time-related column
print("\nColumns in the dataset:")
print(df.columns)

# Step 3: Parse time-related column (example: 'Time_Survived')
# Assuming 'Time_Survived' is a proxy for a time-related metric. Otherwise, adjust this step.
df['Time_Survived_Hours'] = df['Time_Survived'] / 3600  # Convert seconds to hours
df['Player_Index'] = range(1, len(df) + 1)  # Create a player index to simulate time progression

# Step 4: Plot a time-series trend
plt.figure(figsize=(12, 6))
plt.plot(df['Player_Index'], df['Time_Survived_Hours'], label='Time Survived (Hours)', color='blue', marker='o')
plt.title('Time-Series Analysis of Survival Time', fontsize=16)
plt.xlabel('Player Index (as a proxy for time)', fontsize=14)
plt.ylabel('Survival Time (Hours)', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()

# Step 5: Analyze trends over time
# Group by Rank and analyze average survival time
avg_time_by_rank = df.groupby('Rank')['Time_Survived_Hours'].mean()
print("\nAverage survival time by Rank:")
print(avg_time_by_rank)

# Optional: Save time-series insights
output_path = r'C:\Users\yazwi\Downloads\time_series_insights.csv'  # Update path as needed
avg_time_by_rank.to_csv(output_path, header=True)
print(f"\nTime-series insights saved as: {output_path}")

