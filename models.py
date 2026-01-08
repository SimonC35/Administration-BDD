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

class Livre(Base):
    __tablename__ = 'livre'  # Nom table Postgres
    
    isbn = Column(String, primary_key=True)  # Clé primaire
    titre = Column(String)
    editeur = Column(String)
    annee = Column(Integer)
    exemplaires_dispo = Column(Integer)

class Emprunt(Base):
    __tablename__ = 'emprunt'  # Nom table Postgres
    
    id_emprunt = Column(Integer, primary_key=True)  # Clé primaire
    id_etud = Column(Integer, ForeignKey('etudiant.id_etud'))
    isbn = Column(String, ForeignKey('livre.isbn'))
    date_emprunt = Column(Date)
    date_retour = Column(Date, nullable=True)  # Peut être NULL si pas encore retourné
    amende = Column(Float, default=0.0)
