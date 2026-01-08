#!/usr/bin/env python3

def menu_principal(role):
    if role == "etudiant":
        print("\n=== MENU PRINCIPAL (Étudiant) ===")
        print("1 - Voir les Livres et Statistiques")
        print("2 - Emprunter un Livre")
        print("0 - Quitter")
        return input("Choix : ")
    if role == "bibliothecaire":
        print("\n=== MENU PRINCIPAL (Bibliothécaire) ===")
        print("1 - Voir les Livres et Statistiques")
        print("2 - Emprunter un livre")
        print("3 - Retour de livre")
        print("4 - Emprunts en retard")
        print("0 - Quitter")
        return input("Choix : ")

    if role == "admin":
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Gestion Étudiants")
        print("2 - Gestion Livres")
        print("3 - Gestion Emprunts")
        print("0 - Quitter")
        return input("Choix : ")

def menu_crud(entite):
    print(f"\n=== MENU {entite.upper()} ===")
    print("1 - Créer")
    print("2 - Lire")
    print("3 - Modifier")
    print("4 - Supprimer")
    print("0 - Retour")
    return input("Choix : ")