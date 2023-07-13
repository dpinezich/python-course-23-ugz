import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../00-material/ogd_air_d/ugz_ogd_air_d1_2022.csv')
# print(df.describe())
# print(df)

data = df[(df.Standort == "Zch_Stampfenbachstrasse") & (df.Einheit == "µg/m3")]
data = data[0:45]


# Initialize a grid of plots with an Axes for each walk
grid = sns.FacetGrid(data, col="Datum", hue="Datum", palette="tab20c",
                     col_wrap=4, height=1.5)

# Draw a horizontal line to show the starting point
grid.refline(y=0, linestyle=":")

# Draw a line plot to show the trajectory of each random walk
grid.map(plt.plot, "Parameter", "Wert", marker="o")

# Adjust the tick positions and labels
grid.set(xticks=np.arange(5), yticks=[-3, 3],
         xlim=(-.5, 4.5), ylim=(-3.5, 3.5))

# Adjust the arrangement of the plots
grid.fig.tight_layout(w_pad=1)

plt.show()

