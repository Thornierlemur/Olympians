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

        MedalList = [Gold, Silver, Bronze]

        count = 1
        for j in MedalList:
            dob = np.array(j['birth_date'])
            print(dob)

            # Calculate the ages of the people!
            ages = []
            for m in range(len(dob)):
                line = dob[m].split("-")
                ages.append(calculateAge(date(int(line[0]), int(line[1]), int(line[2]))))

            ages.sort()
            print(ages)

            # Gets rid of the duplicates in the array
            resultA = []
            for z in ages:
                if z not in resultA:
                    resultA.append(z)
            print(resultA)

            plt.hist(ages, bins=np.arange(resultA[0] - 0.5, resultA[-1]+1+0.5), edgecolor='white', linewidth=1, align='mid')
            if count == 1:
                plt.title("Gold in " + _)
            elif count == 2:
                plt.title("Silver in " + _)
            else:
                plt.title("Bronze in " + _)
            plt.xlabel("Ages")
            plt.ylabel("Count of Medals")
            plt.xticks(ages)
            plt.show()
            count = count + 1
