import os

# Dossier des images GIF uniquement
dossier_images_gif = '/home/etuinfo/samace/COURS/Réseau/SAE203/SAE203/images_gif_pokemon/'

# Fichier SQL à générer
fichier_sql = 'script.sql'
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
    nom_fichier_nouveau = f"{infos['nom']}.gif"
    chemin_original = os.path.join(dossier_gif, nom_fichier_original)
    chemin_nouveau = os.path.join(dossier_gif, nom_fichier_nouveau)
    if os.path.exists(chemin_original):
        os.rename(chemin_original, chemin_nouveau)
        print(f"Renommé : {nom_fichier_original} -> {nom_fichier_nouveau}")
    else:
        print(f"Fichier non trouvé : {nom_fichier_original}")

# Fonction pour insérer les images GIF avec nom Pokédex formaté
def inserer_images(dossier, fichier_sql_handle):
    for nom_fichier in os.listdir(dossier):
        chemin_fichier = os.path.join(dossier, nom_fichier)
        if os.path.isfile(chemin_fichier) and nom_fichier.lower().endswith('.gif'):
            base_nom = os.path.splitext(nom_fichier)[0]
            numero = base_nom.zfill(3)
            nouveau_nom = f"{numero}.gif"
            info = pokedex.get(numero)
        if info:
            nom = info["nom"]
            description = info["description"]
            donnee = f"{nom} : {description}"
            ligne_insert = (
                f"INSERT INTO images (nom, type, donnee) "
                f"VALUES ('{nouveau_nom}', 'gif', '{donnee}');\n"
            )
            fichier_sql_handle.write(ligne_insert)

# Création du script SQL
with open(fichier_sql, 'w') as f:
    f.write("DROP TABLE IF EXISTS images;\n")
    f.write("CREATE TABLE images (\n")
    f.write("    id INTEGER PRIMARY KEY AUTOINCREMENT,\n")
    f.write("    nom TEXT NOT NULL,\n")
    f.write("    type TEXT NOT NULL,\n")
    f.write("    donnee TEXT NOT NULL\n")
    f.write(");\n\n")

    # Ajouter uniquement les images GIF
    inserer_images(dossier_images_gif, f)

print(f"Script SQL généré avec succès dans : {fichier_sql}")