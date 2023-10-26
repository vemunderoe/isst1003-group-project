import pandas as pd

datasett = pd.read_csv("data/lego.population.clean.csv", sep = ",", encoding = "latin1")

unique_themes = datasett['Theme'].unique()

for theme in unique_themes:
    print(theme)

chosen_theme = input("Choose a theme (Type exit to close): ")
while chosen_theme:
    if chosen_theme.lower() == "exit":
        break
    if chosen_theme in unique_themes:
        # Vis alle Set_Name i temaet uten å vise indeks
        settNavnIValgtTema = datasett.loc[datasett['Theme'] == chosen_theme, 'Set_Name'].values
        for settNavn in settNavnIValgtTema:
            print(settNavn)
    else:
        print("Theme not found. Try again.")
    chosen_theme = input("Choose a theme (Type exit to close): ")