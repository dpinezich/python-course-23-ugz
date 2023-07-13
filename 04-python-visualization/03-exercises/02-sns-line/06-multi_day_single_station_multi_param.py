import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../00-material/ogd_air_d/ugz_ogd_air_d1_2022.csv')
# print(df.describe())
# print(df)

data = df[(df.Standort == "Zch_Stampfenbachstrasse") & (df.Parameter == "NO2")]

sns.lineplot(data=data, x="Datum", y="Wert")

plt.show()


# @Todo add Title
# @Todo Format Date to be more read
# @Todo can you see something special about the data?
# @Todo add more lines for data