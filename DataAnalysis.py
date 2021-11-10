import pandas as pd
import matplotlib as plt

# This is a test comment
medal = pd.read_csv('medals2.csv')

# print(medal)

# print(medal['country'])

medal['country'].plot()
plt.show()