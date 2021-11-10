import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# This is a test comment
medals_df = pd.read_csv('medals2.csv')
coaches_df = pd.read_csv('coaches2.csv')
technical_officials_df = pd.read_csv('technical_officials2.csv')
athletes_df = pd.read_csv('athletes2.csv')
medals_total_df = pd.read_csv('medals_total2.csv')

print(medals_df)

i = 0

old = " "
list = []
check = False

for _ in medals_df['discipline']:
    if old == _:
        continue
    else:
        for i in list:
            if i == _:
                check = True
                break
        if check:
            check = False
            continue
        else:
            temparray = np.array(medals_df[medals_df['discipline']==_])
            print(temparray[0][11])
            old = _
            list.append(_)

    # [access row][access columns] 11='discipline'
# print(temparray[0][9])
# print(temparray[6][9])
# print(temparray[23][9]) #15


# for _ in medals_total_df['Country Code']:
#     temparray = np.array(medals_total_df[medals_total_df['Country Code']==_])
#     print(temparray[0][1])


# Plot the amount of gold medals won.
# plt.hist(medals_total_df['Gold Medal'], bins=medals_total_df.shape[0])
# plt.ylabel("Count")
# plt.title("Gold Medals")
# plt.show()