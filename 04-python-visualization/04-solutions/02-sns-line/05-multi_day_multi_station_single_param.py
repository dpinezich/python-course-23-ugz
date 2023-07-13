import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../00-material/ogd_air_d/ugz_ogd_air_d1_2022.csv')
# print(df.describe())
# print(df)

data = df[(df.Standort == "Zch_Stampfenbachstrasse") & (df.Parameter == "NO2")]
data2 = df[(df.Standort == "Zch_Schimmelstrasse") & (df.Parameter == "NO2")]

data['Datum'] = df['Datum'].str.slice(5,9)
data2['Datum'] = df['Datum'].str.slice(5,9)

#show also other slices like 0,3 or 0,6 and so on


frames = [data, data2]
data = pd.concat(frames)

sns.lineplot(data=data, x="Datum", y="Wert", hue="Standort")

plt.show()


# @Todo add Title
# @Todo Format Date to be more read
# @Todo add another station (hint: hue)