from sqlalchemy import text
from models import Livre

def afficher_stats_livres(session):
    resultats = session.execute(
        text("SELECT * FROM v_stats_livres ORDER BY titre;")
    )

    print("\n=== STATISTIQUES DES LIVRES ===")
    print("ISBN | Titre | Éditeur | Nb emprunts | % dispo")
    print("-" * 70)

    for row in resultats:
        print(
            f"{row.isbn} | {row.titre} | {row.editeur} | "
            f"{row.nb_emprunts} | {row.pourcentage_dispo}%"
        )

def create_livre(session):
    isbn = input("ISBN : ")
    titre = input("Titre : ")
    editeur = input("Éditeur : ")
    annee = int(input("Année : "))
    exemplaires_dispo = int(input("Exemplaires disponibles : "))
    
    livre = Livre(
        isbn=isbn,
        titre=titre,
        editeur=editeur,
        annee=annee,
        exemplaires_dispo=exemplaires_dispo
    )
    session.add(livre)
    session.commit()
    print(f" Livre créé (ISBN={livre.isbn})")

def read_livres(session):
    livres = session.query(Livre).all()
    for l in livres:
        print(f"{l.isbn} | {l.titre} | {l.editeur} | {l.annee} | {l.exemplaires_dispo}")

def update_livre(session):
    isbn = input("ISBN du livre : ")
    livre = session.get(Livre, isbn)
    if livre:
        livre.titre = input("Nouveau titre : ")
        session.commit()
        print(" Livre modifié")
    else:
        print(" Livre introuvable")

def delete_livre(session):
    isbn = input("ISBN du livre : ")
    livre = session.get(Livre, isbn)
    if livre:
        session.delete(livre)
        session.commit()
        print(" Livre supprimé")
    else:
        print(" Livre introuvable")