import pandas as pd

df = pd.read_csv("data/lego.population.csv", sep = ",", encoding = "latin1")

# Liste med variabler vi vil ha igjen
keep = ['Set_Name', 'Theme', 'Price']

# fjerner forklaringsvariabler vi ikke trenger
df2 = df[keep]

# fjerner observasjoner med manglende datapunkter
df2 = df2.dropna()

# gjør themes om til string og fjern alle tegn vi ikke vil ha med
df2['Theme'] = df2['Theme'].astype(str)
df2['Theme'] = df2['Theme'].str.replace(r'[^a-zA-Z0-9\s-]', '', regex = True)

# fjerner dollartegn og trademark-tegn fra datasettet
df2['Price'] = df2['Price'].str.replace('\$', '', regex = True)

# og gjør så prisen om til float
df2['Price'] = df2['Price'].astype(float)

df2.to_csv("data/lego.population.clean.csv", sep = ",", encoding = "latin1", index = False)