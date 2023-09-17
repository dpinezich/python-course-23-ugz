import missingno as msno
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import matplotlib.pyplot as plt


collisions = pd.read_csv("https://raw.githubusercontent.com/ResidentMario/missingno-data/master/nyc_collision_factors.csv")
msno.matrix(collisions.sample(250))
msno.heatmap(collisions)

plt.show()
