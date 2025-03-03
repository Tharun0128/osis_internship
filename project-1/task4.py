import pandas as pd

# Step 1: Load the dataset
file_path = r'C:\Users\yazwi\Downloads\cleaned_pubg_stats.csv'  # Update path as necessary
df = pd.read_csv(file_path)

# Step 2: Inspect the dataset
print("Dataset Columns:", df.columns)

# Step 3: Analyze Player Behavior
# Most active players (by matches played)
most_active_players = df[['Player_Name', 'Matches_Played']].sort_values(by='Matches_Played', ascending=False).head(10)
print("\nTop 10 most active players (by matches played):")
print(most_active_players)

# Players with the highest survival time
top_survival_players = df[['Player_Name', 'Time_Survived']].sort_values(by='Time_Survived', ascending=False).head(10)
print("\nTop 10 players with the highest survival time:")
print(top_survival_players)

# Players with the most kills and assists
top_kills_players = df[['Player_Name', 'Kills']].sort_values(by='Kills', ascending=False).head(10)
print("\nTop 10 players with the most kills:")
print(top_kills_players)

top_assists_players = df[['Player_Name', 'Assists']].sort_values(by='Assists', ascending=False).head(10)
print("\nTop 10 players with the most assists:")
print(top_assists_players)

# Step 4: Analyze Gameplay Patterns
# Most kills by rank
kills_by_rank = df.groupby('Rank')['Kills'].sum().sort_values(ascending=False)
print("\nTotal kills by rank:")
print(kills_by_rank)

# Average damage dealt by rank
avg_damage_by_rank = df.groupby('Rank')['Damage_Dealt'].mean().sort_values(ascending=False)
print("\nAverage damage dealt by rank:")
print(avg_damage_by_rank)

# Top players by headshots, wins, and top 10 placements
top_headshots_players = df[['Player_Name', 'Headshots']].sort_values(by='Headshots', ascending=False).head(10)
print("\nTop 10 players with the most headshots:")
print(top_headshots_players)

top_wins_players = df[['Player_Name', 'Wins']].sort_values(by='Wins', ascending=False).head(10)
print("\nTop 10 players with the most wins:")
print(top_wins_players)

top_top10_players = df[['Player_Name', 'Top_10s']].sort_values(by='Top_10s', ascending=False).head(10)
print("\nTop 10 players with the most Top 10 placements:")
print(top_top10_players)

# Step 5: Save insights to CSV files (optional)
most_active_players.to_csv(r'C:\Users\yazwi\Downloads\most_active_players.csv', index=False)
top_survival_players.to_csv(r'C:\Users\yazwi\Downloads\top_survival_players.csv', index=False)
kills_by_rank.to_csv(r'C:\Users\yazwi\Downloads\kills_by_rank.csv')
avg_damage_by_rank.to_csv(r'C:\Users\yazwi\Downloads\avg_damage_by_rank.csv')
print("\nInsights saved to CSV files.")
