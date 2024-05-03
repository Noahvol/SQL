import sqlite3
import csv

def create_database_connection(database_name):
    # Create a connection to the SQLite database
    return sqlite3.connect(database_name)

def create_postnummer_table(cursor):
    # Create a table for postnummer
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Postnummer (
        postnummer TEXT PRIMARY KEY,
        "by" TEXT,
        kommune TEXT,
        fylke TEXT
    )
    """
    cursor.execute(create_table_query)

def import_postnummer_data(cursor, csv_file):
    # Read data from the CSV file and import into the Postnummer table
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            cursor.execute("INSERT INTO Postnummer (postnummer, \"by\", kommune, fylke) VALUES (?,?,?,?)", row)

def reset_postnummer_table(cursor):
    # Reset the Postnummer table
    cursor.execute("DELETE FROM Postnummer")
    # Optionally, you can also reset the auto-incrementing ID
    cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'Postnummer'")

def main():
    database_name = "min_database.db"
    csv_postnummer_file = "SQL-2/Postnummerregister-Excel.csv"

    # Create a connection to the SQLite database
    connection = create_database_connection(database_name)
    cursor = connection.cursor()

    # Create the Postnummer table if it doesn't exist
    create_postnummer_table(cursor)

    # Import data into the Postnummer table
    import_postnummer_data(cursor, csv_postnummer_file)

    # Reset the Postnummer table (optional)
    reset_postnummer_table(cursor)

    # Commit the changes and close the database connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()