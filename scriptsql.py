import sqlite3
import os

# Connexion à la base SQLite (ou MySQL avec adaptation)
conn = sqlite3.connect('images.db')
cursor = conn.cursor()

# Création de la table
cursor.execute('''
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    donnees BLOB
)
''')

# Dossier contenant les images
dossier_images = '/chemin/vers/images'

# Parcours et insertion
for nom_fichier in os.listdir(dossier_images):
    chemin_fichier = os.path.join(dossier_images, nom_fichier)

    if os.path.isfile(chemin_fichier):
        with open(chemin_fichier, 'rb') as f:
            donnees = f.read()
            cursor.execute("INSERT INTO images (nom, donnees) VALUES (?, ?)", (nom_fichier, donnees))

conn.commit()
conn.close()
