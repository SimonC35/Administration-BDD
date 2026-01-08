#!/usr/bin/env python3

import os
from dotenv import load_dotenv

from database import get_session
from menu import menu_principal, menu_crud
from crud.emprunt import (
    create_emprunt,
    read_emprunts,
    update_emprunt,
    delete_emprunt,
    read_emprunts_retard,
    read_emprunts_en_cours
)
from crud.etudiant import (
    create_etudiant,
    read_etudiants,
    update_etudiant,
    delete_etudiant
)
from crud.livre import (
    create_livre,
    read_livres,
    update_livre,
    delete_livre,
    afficher_stats_livres
)

def main():
    # Charger les variables d'environnement
    load_dotenv()

    role = input("Votre rôle (admin / bibliothecaire / etudiant) : ").lower()
    if role not in ("admin", "bibliothecaire", "etudiant"):
        print("Rôle invalide.")
        return

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    # print("Variables chargées depuis .env")
    print(f"Connexion à : {host}:{port}/{dbname}")

    session = get_session(role)

    while True:
        choix = menu_principal(role)

        # ===== ÉTUDIANT =====
        if role == "etudiant":
            if choix == "1":
                afficher_stats_livres(session)
            elif choix == "2":
                create_emprunt(session)
            elif choix == "0":
                print("Au revoir !")
                break
            else:
                print("Choix invalide")
            continue
        # ===== BIBLIOTHÉCAIRE =====
        if role == "bibliothecaire":
            if choix == "1":
                afficher_stats_livres(session)
            elif choix == "2":
                create_emprunt(session)
            elif choix == "3":
                update_emprunt(session)  # Retour de livre
            elif choix == "4":
                read_emprunts_en_cours(session)
            elif choix == "5":
                read_emprunts_retard(session)
            elif choix == "0":
                print("Au revoir !")
                break
            else:
                print("Choix invalide")
            continue

        # ===== ETUDIANTS =====
        if choix == "1":
            while True:
                action = menu_crud("Étudiants")
                if action == "1" and role in ("admin", "bibliothecaire"):
                    create_etudiant(session)
                elif action == "2":
                    read_etudiants(session)
                elif action == "3" and role in ("admin", "bibliothecaire"):
                    update_etudiant(session)
                elif action == "4" and role == "admin":
                    delete_etudiant(session)
                elif action == "0":
                    break
                else:
                    print("Action non autorisée")

        # ===== LIVRES =====
        elif choix == "2":
            while True:
                action = menu_crud("Livres")
                if action == "1":
                    create_livre(session)
                elif action == "2":
                    read_livres(session)
                elif action == "3":
                    update_livre(session)
                elif action == "4":
                    delete_livre(session)
                elif action == "0":
                    break
                else:
                    print("Action non autorisée")
        # ===== EMPRUNTS =====
        elif choix == "3":
            while True:
                action = menu_crud("Emprunts")
                if action == "1":
                    create_emprunt(session)
                elif action == "2":
                    read_emprunts(session)
                elif action == "3":
                    update_emprunt(session)
                elif action == "4":
                    delete_emprunt(session)
                elif action == "0":
                    break
                else:
                    print("Action non autorisée")

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide")

if __name__ == "__main__":
    main()
