import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../00-material/ogd_air_d/ugz_ogd_air_d1_2022.csv')
# print(df.describe())
# print(df)

stampf = df[(df.Standort == "Zch_Stampfenbachstrasse") & (df.Datum == "2022-01-01T00:00+0100") & (df.Einheit == "µg/m3")]
heub = df[(df.Standort == "Zch_Heubeeribüel") & (df.Datum == "2022-01-01T00:00+0100") & (df.Einheit == "µg/m3")]

frames = [stampf, heub]
data = pd.concat(frames)

sns.barplot(data=data, x="Parameter", y="Wert", hue="Standort")
sns.set_theme(style="darkgrid")

plt.show()

# @Todo Add Title
# @Todo remove PM10/PM2.5