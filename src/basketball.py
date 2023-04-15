import pandas as pd
import matplotlib.pyplot as plt

# create a dictionary of basketball data
data = {
    'Player': ['LeBron James', 'Kevin Durant', 'Stephen Curry', 'Kawhi Leonard', 'Giannis Antetokounmpo'],
    'Points': [25.3, 27.1, 24.5, 26.8, 28.1],
    'Rebounds': [7.8, 7.1, 5.3, 6.5, 11.0],
    'Assists': [10.2, 5.9, 6.7, 5.0, 5.9],
    'Steals': [1.2, 0.7, 1.4, 1.8, 1.4]
}

# create a dataframe from the dictionary
df = pd.DataFrame(data)

print(df)

# plot the Points column on a bar chart
plt.bar(df['Player'], df['Points'])
plt.title('Basketball Points')
plt.xlabel('Player')
plt.ylabel('Points')
plt.show()

# plot the Rebounds and Assists columns on a scatter plot
plt.scatter(df['Rebounds'], df['Assists'])
plt.title('Basketball Rebounds vs. Assists')
plt.xlabel('Rebounds')
plt.ylabel('Assists')
plt.show()
