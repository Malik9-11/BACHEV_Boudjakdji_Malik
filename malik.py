# Boudjakdji Malik, BACHEV, 11/12/2025
# Bendeddouche Mohamed Youchae
# Abdeldjelil Siham
# Salhi Amira Nour El Houda
# Nordine Baya

import pandas as pd
data = {
    "Séquence": ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur": [11, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

df = pd.DataFrame(data)
print(df)
Longueur = df["Longueur"]
print(Longueur)

# Filtrer les séquences dont la longueur est supérieure à 10
print ("******** Séquences avec longueur > 10 ********")
# Filtrer les séquences avec une longueur supérieur à 10
filtered_df = df[df["Longueur"] > 10]
print(filtered_df, "\n")

# Calculer la moyenne du pourcentage de GC avec 3 chiffres après la virgule
print ("******** Calcul de la moyenne ********")
# Calculer la moyenne du pourcentage de GC
average_gc = df["Pourcentage GC"].mean()
print(f"\n Pourcentage moyen de GC : {average_gc:.3f}%")