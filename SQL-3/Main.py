import sqlite3
import pandas as pd
 
# Database navn
database_navn = "kundeliste.db"
 
# Koble til databasen
conn = sqlite3.connect(database_navn)
c = conn.cursor()
data = pd.read_excel('SQL-3/Kundeliste.xlsx')  # Leser data fra CSV-fil
data1 = pd.read_excel('SQL-3/Postnummer.xlsx')  # Leser data fra CSV-fil

# Funksjon for å opprette databasen og tabellen for kundeinformasjon
def funclag_database():
    c.execute('''CREATE TABLE IF NOT EXISTS kundeinfo (
        Kundenummer int,
        Fornavn str,
        Etternavn str,
        Epost varchar,
        Telefon int,
        Postnummer int,
        PRIMARY KEY (Kundenummer)
    )''')
    conn.commit()
 
# Funksjon for å fylle kundeinformasjon fra CSV-fil til databasen
def funcfyll_data():
    for index, row in data.iterrows():
        # Check if the Kundenummer already exists in the database
        c.execute("SELECT COUNT(*) FROM kundeinfo WHERE Kundenummer = ?", (row['Kundenummer'],))
        count = c.fetchone()[0]
        
        
        c.execute(
                """
                INSERT OR IGNORE INTO kundeinfo (Kundenummer, Fornavn, Etternavn, Epost, Telefon, Postnummer)
                VALUES (?,?,?,?,?,?)
                """,
                (row['Kundenummer'], row['Fornavn'], row['Etternavn'], row['Epost'], row['Telefon'], row['Postnummer'])
            )
        conn.commit()
        
 
# Funksjon for å opprette tabellen for postnummre
def funclag_postnummer_tabel():
    c.execute('''CREATE TABLE IF NOT EXISTS postnummer_tabell (
        Postnummer int,
        Poststed str,
        Kommunenummer int,
        Kommunenavn str,
        PRIMARY KEY (Postnummer)
    )''')
    conn.commit()

def funcfyll_postnummer():
    for index, row in data1.iterrows():
        c.execute(
            """
            INSERT OR IGNORE INTO postnummer_tabell (Postnummer, Poststed, Kommunenummer, Kommunenavn)
            VALUES (?,?,?,?)
            """,
            (row['Postnummer'], row['Poststed'], row['Kommunenummer'], row['Kommunenavn'])
        )
        conn.commit()

       
 
# Funksjon for å spørre brukeren om kundenummer og vise kundeinformasjon
def funcvis_kunde_info():
    kundenummer = input("Skriv inn kundenummer: ")
    c.execute("SELECT * FROM kundeinfo WHERE kundenummer=?", (kundenummer,))
    customer_data = c.fetchone()
    if customer_data:
        print("Kundeinformasjon:")
        print(f"Kundenummer: {customer_data[0]}")
        print(f"Fornavn: {customer_data[1]}")
        print(f"Etternavn: {customer_data[2]}")
        print(f"Epost: {customer_data[3]}")
        print(f"Telefon: {customer_data[4]}")
        print(f"Postnummer: {customer_data[5]}")
    else:
        print("Kunde ikke funnet.")
 
# Hovedfunksjonen
def main():
    funclag_database()            # Opprett kundeinfo-tabellen
    funcfyll_data()               # Fyll kundeinformasjon fra CSV-fil
    funclag_postnummer_tabel()    # Opprett postnummer_tabell
    funcvis_kunde_info()          # Vis kundeinformasjon basert på kundenummer
    funcfyll_postnummer()         # Fyll postnummer_tabell fra CSV-fil
 
    conn.close()
 
# Kjør hovedfunksjonen når dette skriptet blir kjørt
if __name__ == '__main__':
    main()
 