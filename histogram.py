import pandas as pd
import matplotlib.pyplot as plt

datasett = pd.read_csv("data/lego.population.clean.csv", sep = ",", encoding = "latin1")

plt.hist(datasett['Price'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Pris i dollar [$]')
plt.ylabel('')
plt.gca().set_aspect(1)
plt.show()