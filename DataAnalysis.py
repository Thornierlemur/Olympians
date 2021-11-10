import pandas as pd
import matplotlib.pyplot as plt

# This is a test comment
medals_df = pd.read_csv('medals2.csv')
coaches_df = pd.read_csv('coaches2.csv')
technical_officials_df = pd.read_csv('technical_officials2.csv')
athletes_df = pd.read_csv('athletes2.csv')
medals_total_df = pd.read_csv('medals_total2.csv')

print(medals_total_df.head(3))

# Plot the amount of gold medals won.
plt.hist(medals_total_df['Gold Medal'], bins=medals_total_df.shape[0])
plt.ylabel("Count")
plt.title("Gold Medals")
plt.show()