import pandas as pd

# Les inn data
datasett = pd.read_csv("data/lego.population.clean.csv", sep=",", encoding="latin1")

# Hent unike tema fra datasettet
unike_tema = datasett['Theme'].unique()

# Definer en liste over kjønn
kjønn = ["nøytralt", "gutt", "jente"]

for tema in unike_tema:
    # Be brukeren om kjønn for hvert tema til en gyldig verdi er gitt
    while True:
        try:
            kjønn_for_tema = input("Skriv inn kjønn for tema " + str(tema) + " (1 for gutt, 2 for jente, 0 for kjønnsnøytralt):")
            # Kontroller at inndata er en gyldig verdi (0, 1 eller 2)
            if kjønn_for_tema not in ['0', '1', '2']:
                raise ValueError
            break  # Avslutt løkken hvis inndata er gyldig
        except ValueError:
            print("Ugyldig inndata. Prøv igjen.")

    print("Tema " + str(tema) + " får kjønn: " + kjønn[int(kjønn_for_tema)])
    # Oppdater datasettet med kjønn for det aktuelle temaet
    datasett.loc[datasett['Theme'] == tema, 'Kjønn'] = kjønn[int(kjønn_for_tema)]

# Lagre det oppdaterte datasettet til en ny fil
datasett.to_csv("data/lego.population.clean.csv", sep=",", encoding="latin1", index=False)
