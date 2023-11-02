import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np

datasett = pd.read_csv("data/lego.population.clean.nøytralt.csv", sep = ",", encoding = "latin1")

formel = 'Pages ~ Pieces'

modell = smf.ols(formel, data = datasett)
resultat = modell.fit()

print(resultat.summary())

print(resultat)

slope = resultat.params['Pieces']
intercept = resultat.params['Intercept']

regression_x = np.array(datasett['Pieces'])

regression_y = slope * regression_x + intercept

plt.scatter(datasett['Pieces'], datasett['Pages'], label='Data Points')
plt.plot(regression_x, regression_y, color='red', label='Regression Line')
plt.xlabel('Antall brikker')
plt.ylabel('Antall sider')
plt.title('Kryssplott med regresjonslinje (enkel LR)')
plt.legend()
plt.grid()
plt.show()