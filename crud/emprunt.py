from sqlalchemy import text
from datetime import datetime
from models import Emprunt

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

def read_emprunts_en_cours(session):
    resultats = session.execute(
        text("SELECT * FROM v_emprunts_en_cours ORDER BY id_emprunt;")
    )

    print("\n=== EMPRUNTS EN COURS ===")
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
        date_retour_input = datetime.now().date().strftime("%Y-%m-%d")
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