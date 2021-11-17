import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
         (birthDate.month, birthDate.day))
 
    return age

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

        # myArch = medals_df[medals_df['discipline']=='Archery']
        Archarray = np.array(medals_df[medals_df['discipline']==_])

        # This is a huge testing section where I drop certain columns
        athleteArch = athletes_df[athletes_df['discipline'] == _]
        athleteArch = athleteArch.drop(columns=['short_name', 'birth_place', 'birth_country', 'country', 'country_code', 'residence_place', "residence_country", "height_m/ft", "url"])
        # Rename the 'name' column to 'athlete_name' for merging purposes
        athleteArch = athleteArch.rename(columns={'name': 'athlete_name'})

        result = pd.merge(temparray, athleteArch, how="inner", on='athlete_name') # temparray before was myArch! (Just a Note to Isaac from himself)

        Gold = result[result['medal_code']==1]
        Silver = result[result['medal_code']==2]
        Bronze = result[result['medal_code']==3]

        dob = np.array(Gold['birth_date'])
        dob1 = np.array(Silver['birth_date'])
        dob2 = np.array(Bronze['birth_date'])

        # Calculate the ages of the people!
        ages = []
        for m in range(len(dob)):
            line = dob[m].split("-")
            ages.append(calculateAge(date(int(line[0]), int(line[1]), int(line[2]))))
        ages.sort()

        ages1 = []
        for m in range(len(dob1)):
            line = dob1[m].split("-")
            ages1.append(calculateAge(date(int(line[0]), int(line[1]), int(line[2]))))
        ages1.sort()

        ages2 = []
        for m in range(len(dob2)):
            line = dob2[m].split("-")
            ages2.append(calculateAge(date(int(line[0]), int(line[1]), int(line[2]))))
        ages2.sort()

        # Gets rid of the duplicates in the array
        resultA = []
        for z in ages:
            if z not in resultA:
                resultA.append(z)
        
        # Gets rid of the duplicates in the array
        resultA1 = []
        for z in ages1:
            if z not in resultA1:
                resultA1.append(z)
        
        # Gets rid of the duplicates in the array
        resultA2 = []
        for z in ages2:
            if z not in resultA2:
                resultA2.append(z)

        # Create 3 plots to plot the data for Gold, Silver, and Bronze
        fig, axs = plt.subplots(3)

        axs[0].hist(ages, bins=np.arange(resultA[0] - 0.5, resultA[-1]+1+0.5), edgecolor='white', linewidth=1, align='mid')
        axs[0].title.set_text("Gold in " + _)
        axs[0].set_xlabel("Ages")
        axs[0].set_ylabel("Count of Medals")
        axs[0].set_xticks(ages)

        axs[1].hist(ages1, bins=np.arange(resultA1[0] - 0.5, resultA1[-1]+1+0.5), edgecolor='white', linewidth=1, align='mid')
        axs[1].title.set_text("Silver in " + _)
        axs[1].set_xlabel("Ages")
        axs[1].set_ylabel("Count of Medals")
        axs[1].set_xticks(ages1)

        axs[2].hist(ages2, bins=np.arange(resultA2[0] - 0.5, resultA2[-1]+1+0.5), edgecolor='white', linewidth=1, align='mid')
        axs[2].title.set_text("Bronze in " + _)
        axs[2].set_xlabel("Ages")
        axs[2].set_ylabel("Count of Medals")
        axs[2].set_xticks(ages2)

        # plt.xticks(ages)
        plt.tight_layout(pad=1.0)
        plt.show()
