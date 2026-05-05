# NFL 2024 Salary Analysis
# Author: Jakob Bichsel
# Tools: Python, pandas

import pandas as pd

# Step 1: Load the data
df = pd.read_csv('nfl_2024_performance.csv')

# Step 2: Look at the data
print(df.head())

# Step 3: Create a new column — salary in millions (easier to read)
df['salary_millions'] = df['cap_hit'] / 1_000_000

# Step 4: Create a value score — fantasy points per $1M spent
df['value_score'] = df['fantasy_points'] / df['salary_millions']

# Step 5: Sort by value score to find the best bargains
df_sorted = df.sort_values('value_score', ascending=False)

# Step 6: Show the top 10 best value players
print("\nTop 10 Best Value Players:")
print(df_sorted[['player_name', 'position', 'team', 'salary_millions', 'fantasy_points', 'value_score']].head(10))

# Step 7: Filter to just quarterbacks
qbs = df[df['position'] == 'QB']
print("\nQuarterbacks sorted by value:")
print(qbs.sort_values('value_score', ascending=False)[['player_name', 'team', 'salary_millions', 'fantasy_points', 'value_score']])

# Step 8: Find the average salary by position
print("\nAverage salary by position:")
print(df.groupby('position')['salary_millions'].mean().round(2))

# Step 9: Save a simple bar chart of top 10 value players
import matplotlib.pyplot as plt

top10 = df_sorted.head(10)
plt.figure(figsize=(10, 6))
plt.barh(top10['player_name'], top10['value_score'], color='steelblue')
plt.xlabel('Fantasy Points per $1M')
plt.title('NFL 2024 - Top 10 Best Value Players')
plt.tight_layout()
plt.savefig('nfl_value_players.png')
print("\nChart saved!")
