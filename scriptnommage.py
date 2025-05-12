import os

# Chemin vers le dossier contenant les fichiers GIF
dossier_gif = "/home/etuinfo/samace/COURS/Réseau/SAE203/SAE203/images_gif_test/"
pokedex = {
    "001": {"nom": "Bulbizarre", "description": "Un Pokémon de type Plante et Poison."},
    "002": {"nom": "Herbizarre", "description": "L’évolution de Bulbizarre."},
    "003": {"nom": "Florizarre", "description": "Il possède une fleur massive sur le dos."},
    # ... jusqu’à "151"
}

for numero, infos in pokedex.items():
    nom_fichier_original = f"{numero:03}.gif"
    nom_fichier_nouveau = f"{infos['nom_fr']}.gif"
    chemin_original = os.path.join(dossier_gif, nom_fichier_original)
    chemin_nouveau = os.path.join(dossier_gif, nom_fichier_nouveau)
    if os.path.exists(chemin_original):
        os.rename(chemin_original, chemin_nouveau)
        print(f"Renommé : {nom_fichier_original} -> {nom_fichier_nouveau}")
    else:
        print(f"Fichier non trouvé : {nom_fichier_original}")
