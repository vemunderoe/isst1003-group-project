import pandas as pd

datasett = pd.read_csv("data/lego.population.csv", sep = ",", encoding = "latin1")

unique_themes = datasett['Theme'].unique()

for theme in unique_themes:
    print(theme)
