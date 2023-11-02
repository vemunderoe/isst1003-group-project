import pandas as pd

# Antatt at du har renset data og lagret det i variabelen 'rensket_datasett'
rensket_datasett = pd.read_csv("data/lego.population.clean.csv", sep=",", encoding="latin1")

# Grupper datasettet etter kjønn
gruppert_datasett = rensket_datasett.groupby('Kjønn')

# Lagre hver gruppe til en separat fil
for kjønn, gruppe in gruppert_datasett:
    filnavn = f"data/lego.population.clean.{kjønn}.csv"
    gruppe.to_csv(filnavn, sep=",", encoding="latin1", index=False)
