import pandas as pd
import matplotlib.pyplot as plt

datasett = pd.read_csv("data/lego.population.clean.csv", sep = ",", encoding = "latin1")

plt.scatter(datasett['Pieces'], datasett['Price'])
plt.xlabel('Antall brikker')
plt.ylabel('Pris i dollar [$]')
plt.gca().set_aspect(5)
plt.show()