import pandas as pd

datasett = pd.read_csv("data/lego.population.csv", sep = ",", encoding = "latin1")

# Liste med variabler vi vil ha igjen
kolonner = ['Set_Name', 'Theme', 'Price']

# fjerner forklaringsvariabler vi ikke trenger
rensket_datasett = datasett[kolonner]

# fjerner observasjoner med manglende datapunkter
rensket_datasett = rensket_datasett.dropna()

# gjør themes om til string og fjern alle tegn vi ikke vil ha med
rensket_datasett['Theme'] = rensket_datasett['Theme'].astype(str)
rensket_datasett['Theme'] = rensket_datasett['Theme'].str.replace(r'[^a-zA-Z0-9\s-]', '', regex = True)

# fjerner dollartegn og trademark-tegn fra datasettet
rensket_datasett['Price'] = rensket_datasett['Price'].str.replace('\$', '', regex = True)

# og gjør så prisen om til float
rensket_datasett['Price'] = rensket_datasett['Price'].astype(float)

rensket_datasett.to_csv("data/lego.population.clean.csv", sep = ",", encoding = "latin1", index = False)