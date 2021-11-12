import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

# This is a test comment
medals_df = pd.read_csv('medals2.csv')
coaches_df = pd.read_csv('coaches2.csv')
technical_officials_df = pd.read_csv('technical_officials2.csv')
athletes_df = pd.read_csv('athletes2.csv')
medals_total_df = pd.read_csv('medals_total2.csv')

i = 0

old = " "
list = []
check = False

# This for loop is getting the data for each of the disciplines!
# I just need to make it so that i store them whenever I get it!
for _ in medals_df['discipline']:
    for i in list:
        if i == _:
            check = True
            break
    if check:
        check = False
        continue
    else:
        temparray = medals_df[medals_df['discipline']==_]
        #print(temparray)
        list.append(_)

    # [access row][access columns] 11='discipline' (this is when its in the np.array() format)
    # Now, store the discipline into a list of some sort, and then 

myArch = medals_df[medals_df['discipline']=='Archery']
Archarray = np.array(medals_df[medals_df['discipline']=='Archery'])



# This is a huge testing section where I drop certain columns
athleteArch = athletes_df[athletes_df['discipline'] == 'Archery']
athleteArch = athleteArch.drop(columns=['short_name', 'birth_place', 'birth_country', 'country', 'country_code', 'residence_place', "residence_country", "height_m/ft", "url"])
# Rename the 'name' column to 'athlete_name' for merging purposes
athleteArch = athleteArch.rename(columns={'name': 'athlete_name'})

result = pd.merge(myArch, athleteArch, how="inner", on='athlete_name')

Gold = result[result['medal_code']==1]
Silver = result[result['medal_code']==2]
Bronze = result[result['medal_code']==3]

dob = np.array(Bronze['birth_date'])
print(dob)

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
         (birthDate.month, birthDate.day))
 
    return age


for i in range(len(dob)):
    line = dob[i].split("-")
    print(calculateAge(date(int(line[0]), int(line[1]), int(line[2]))), "years")
    


# Plot the amount of gold medals won.
# plt.hist(medals_total_df['Gold Medal'], bins=medals_total_df.shape[0])
# plt.ylabel("Count")
# plt.title("Gold Medals")
# plt.show()