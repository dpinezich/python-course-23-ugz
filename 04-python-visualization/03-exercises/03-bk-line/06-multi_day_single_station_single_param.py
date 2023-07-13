import pandas as pd
from bokeh.io import output_notebook, show
from bokeh.plotting import figure

df = pd.read_csv('../../00-material/ogd_air_d/ugz_ogd_air_d1_2022.csv')
# print(df.describe())
# print(df)

data = df[(df.Standort == "Zch_Stampfenbachstrasse") & (df.Parameter == "NO2")]

# create a new plot using figure
p = figure(width=400, height=400)

# add a square renderer with a size, color, alpha, and sizes
# size=[10, 15, 20, 25, 30]

#print(data['Wert'].values.tolist()[0:100])
counter = [*range(1, 101)]

p.square(counter, data['Wert'].values.tolist()[0:100], color="firebrick", alpha=0.6)

show(p) # show the results
