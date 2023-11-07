# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np

# Load your dataset
datasett = pd.read_csv("data/lego.population.clean.csv", sep=",", encoding="utf-8")

# Adjust the model formula to use 'Gender' as a categorical variable instead of 'Theme'
modell3_mlr = smf.ols('Pages ~ Pieces + C(Gender)', data=datasett)

# Fit the model
model_fit = modell3_mlr.fit()

# Print the summary of the model
print(model_fit.summary())

# Store the parameters for plotting
intercept = model_fit.params['Intercept']
slope = model_fit.params['Pieces']
gender_coefficients = {gender: model_fit.params[f'C(Gender)[T.{gender}]'] for gender in datasett['Gender'].unique() if gender != 'gutt'}  # Assuming 'gutt' is the reference category

# Plotting
plt.figure(figsize=(10, 8))
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

# Plot each gender
for idx, (gender, coefficient) in enumerate(gender_coefficients.items()):
    # Subset the dataset by gender
    gender_subset = datasett[datasett['Gender'] == gender]
    
    # Calculate the regression values
    regression_x = np.array(gender_subset['Pieces'])
    regression_y = slope * regression_x + intercept + coefficient
    
    # Scatter plot
    plt.scatter(gender_subset['Pieces'], gender_subset['Pages'], color=colors[idx % len(colors)], label=gender)
    
    # Regression line
    plt.plot(regression_x, regression_y, color=colors[idx % len(colors)])

# Plot for the reference category (assuming 'gutt' is the reference category)
gender_subset = datasett[datasett['Gender'] == 'gutt']
regression_x = np.array(gender_subset['Pieces'])
regression_y = slope * regression_x + intercept
plt.scatter(gender_subset['Pieces'], gender_subset['Pages'], color='orange', label='gutt')
plt.plot(regression_x, regression_y, color='orange')

# Labels and Legend
plt.xlabel('Number of Pieces')
plt.ylabel('Antall sider')
plt.title('Antall sider av antall brikker og kjønn')
plt.legend()
plt.grid(True)
plt.show()
