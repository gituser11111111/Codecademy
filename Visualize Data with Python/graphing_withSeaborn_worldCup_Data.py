import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
print(df.head())

#We want to visualize the total number of goals scored in each match
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())

#Create a bar chart visualizing how many goals were scored each year the World Cup was held between 1930-2014.
sns.set_style('whitegrid')
sns.set_context('poster', font_scale=0.8)
f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(data=df, x='Year', y='Total Goals')
ax.set_title('Goals every year')
plt.show()

df_goals = pd.read_csv('goals.csv')
print(df_goals.head())

#create a box plot so you can visualize the distribution of the goals data instead of just the average with a bar chart.
sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12, 7))
sns.color_palette('Spectral')
ax2 = sns.boxplot(data=df_goals, x='year', y='goals')
ax2.set_title('Goals per year')
plt.show()