#!/usr/bin/env python3

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, text
from datetime import datetime

Base = declarative_base()

class Etudiant(Base):
    __tablename__ = 'etudiant'  # Nom table Postgres
    
    id_etud = Column(Integer, primary_key=True)  # Clé primaire
    nom = Column(String)
    prenom = Column(String)
    email = Column(String)
    date_inscription = Column(Date)
    solde_amende = Column(Float)

def create_etudiant(session):
    nom = input("Nom : ").upper()
    prenom = input("Prénom : ")
    email = input("Email : ")
    
    etu = Etudiant(
        nom=nom,
        prenom=prenom,
        email=email,
        date_inscription=datetime.now().date(),
        solde_amende=0.0
    )
    session.add(etu)
    session.commit()
    print(f" Étudiant créé (ID={etu.id_etud})")


def read_etudiants(session):
    etudiants = session.query(Etudiant).all()
    for e in etudiants:
        print(f"{e.id_etud} | {e.prenom} {e.nom} | {e.email}")


def update_etudiant(session):
    id_etu = int(input("ID étudiant : "))
    etu = session.get(Etudiant, id_etu)
    if etu:
        etu.prenom = input("Nouveau prénom : ")
        session.commit()
        print(" Étudiant modifié")
    else:
        print(" Étudiant introuvable")


def delete_etudiant(session):
    id_etu = int(input("ID étudiant : "))
    etu = session.get(Etudiant, id_etu)
    if etu:
        session.delete(etu)
        session.commit()
        print(" Étudiant supprimé")
    else:
        print(" Étudiant introuvable")

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


class Livre(Base):
    __tablename__ = 'livre'  # Nom table Postgres
    
    isbn = Column(String, primary_key=True)  # Clé primaire
    titre = Column(String)
    editeur = Column(String)
    annee = Column(Integer)
    exemplaires_dispo = Column(Integer)

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


class Emprunt(Base):
    __tablename__ = 'emprunt'  # Nom table Postgres
    
    id_emprunt = Column(Integer, primary_key=True)  # Clé primaire
    id_etud = Column(Integer, ForeignKey('etudiant.id_etud'))
    isbn = Column(String, ForeignKey('livre.isbn'))
    date_emprunt = Column(Date)
    date_retour = Column(Date, nullable=True)  # Peut être NULL si pas encore retourné
    amende = Column(Float, default=0.0)

def create_emprunt(session):
    id_etud = int(input("ID étudiant : "))
    isbn = input("ISBN du livre : ")
    
    emprunt = Emprunt(
        id_etud=id_etud,
        isbn=isbn,
        date_emprunt=datetime.now().date(),
        date_retour=None,
        amende=0.0
    )
    session.add(emprunt)
    session.commit()
    print(f" Emprunt créé (ID={emprunt.id_emprunt})")

def read_emprunts(session):
    emprunts = session.query(Emprunt).all()
    for emp in emprunts:
        retour = emp.date_retour if emp.date_retour else "Non retourné"
        print(f"{emp.id_emprunt} | Étudiant ID: {emp.id_etud} | Livre ISBN: {emp.isbn} | Emprunté le: {emp.date_emprunt} | Retour: {retour} | Amende: {emp.amende}")

def read_emprunts_retard(session):
    resultats = session.execute(
        text("SELECT * FROM v_emprunts_retard ORDER BY date_retour;")
    )

    print("\n=== EMPRUNTS EN RETARD ===")
    print("ID | Étudiant | ISBN | Emprunt | Retour | Amende")
    print("-" * 80)

    for row in resultats:
        print(
            f"{row.id_emprunt} | "
            f"{row.prenom} {row.nom} | "
            f"{row.isbn} | "
            f"{row.date_emprunt} | "
            f"{row.date_retour} | "
            f"{row.amende}€"
        )

def update_emprunt(session):
    id_emprunt = int(input("ID emprunt : "))
    emprunt = session.get(Emprunt, id_emprunt)
    if emprunt:
        date_retour_input = input("Date de retour (YYYY-MM-DD) ou laisser vide si pas encore retourné : ")
        if date_retour_input:
            emprunt.date_retour = datetime.strptime(date_retour_input, "%Y-%m-%d").date()
        session.commit()
        print(" Emprunt modifié")
    else:
        print(" Emprunt introuvable")

def delete_emprunt(session):
    id_emprunt = int(input("ID emprunt : "))
    emprunt = session.get(Emprunt, id_emprunt)
    if emprunt:
        session.delete(emprunt)
        session.commit()
        print(" Emprunt supprimé")
    else:
        print(" Emprunt introuvable")