#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import host, port, dbname, user, password
import psycopg2  # pip install psycopg2-binary

try:
    connexion = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

    curseur = connexion.cursor()

    curseur.execute("SELECT version();")
    # print("SUCCESS")
    # print(f"PostgreSQL : {curseur.fetchone()}")

    # curseur.execute("SELECT COUNT(*) FROM etudiant;")
    # print(f"{curseur.fetchone()[0]} étudiants chargés")

    curseur.close()
    connexion.close()

except psycopg2.OperationalError as erreur:
    print("Erreur connexion : vérifie .env/PostgreSQL")
    print(erreur)

engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
)

Session = sessionmaker(bind=engine)
session = Session()

def get_session(role):
    return Session()