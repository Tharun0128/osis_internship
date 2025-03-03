import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
file_path = r'C:\Users\yazwi\Downloads\cleaned_pubg_stats.csv'
df = pd.read_csv(file_path)

# Step 2: Visualize most active players (matches played)
top_players = df[['Player_Name', 'Matches_Played']].sort_values(by='Matches_Played', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='Matches_Played', y='Player_Name', data=top_players, palette='viridis')
plt.title('Top 10 Most Active Players (Matches Played)', fontsize=16)
plt.xlabel('Matches Played', fontsize=12)
plt.ylabel('Player Name', fontsize=12)
plt.tight_layout()
plt.show()

# Step 3: Visualize players with the most kills
top_kills = df[['Player_Name', 'Kills']].sort_values(by='Kills', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='Kills', y='Player_Name', data=top_kills, palette='plasma')
plt.title('Top 10 Players with Most Kills', fontsize=16)
plt.xlabel('Number of Kills', fontsize=12)
plt.ylabel('Player Name', fontsize=12)
plt.tight_layout()
plt.show()

# Step 4: Pie chart for player rank distribution
rank_distribution = df['Rank'].value_counts()
plt.figure(figsize=(8, 8))
rank_distribution.plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=140)
plt.title('Player Rank Distribution', fontsize=16)
plt.ylabel('')  # Hide y-label
plt.tight_layout()
plt.show()

# Step 5: Line chart for average damage dealt by rank
avg_damage_by_rank = df.groupby('Rank')['Damage_Dealt'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
avg_damage_by_rank.plot(kind='line', marker='o', color='purple')
plt.title('Average Damage Dealt by Rank', fontsize=16)
plt.xlabel('Rank', fontsize=12)
plt.ylabel('Average Damage Dealt', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Scatter plot for kills vs. matches played
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Matches_Played', y='Kills', data=df, hue='Rank', palette='Set1', alpha=0.7)
plt.title('Kills vs. Matches Played', fontsize=16)
plt.xlabel('Matches Played', fontsize=12)
plt.ylabel('Kills', fontsize=12)
plt.legend(title='Rank')
plt.tight_layout()
plt.show()

# Step 7: Scatter plot for damage dealt vs. kills
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Damage_Dealt', y='Kills', data=df, hue='Rank', palette='cool', alpha=0.7)
plt.title('Damage Dealt vs. Kills', fontsize=16)
plt.xlabel('Damage Dealt', fontsize=12)
plt.ylabel('Kills', fontsize=12)
plt.legend(title='Rank')
plt.tight_layout()
plt.show()
