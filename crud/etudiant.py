from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, text
from datetime import datetime
from models import Etudiant

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