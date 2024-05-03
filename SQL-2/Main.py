import sqlite3  # Import the SQLite3 module for database operations
import csv      # Import the CSV module for reading CSV files

# Define a function to create the 'Post' table in the database if it doesn't exist
def create_postnummer_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Post (
        postnummer TEXT PRIMARY KEY,
        "by" TEXT,
        kommune TEXT,
        fylke TEXT,
        kategori TEXT
    )
    """)

# Define a function to import data from a CSV file into the 'Post' table
def import_postnummer_data(cursor, csv_fil, encoding='utf-8'):
    # Open the CSV file with specified encoding
    with open(csv_fil, 'r', encoding=encoding) as fil:
        # Create a CSV reader object with ';' as delimiter
        csv_leser = csv.reader(fil, delimiter=';')
        next(csv_leser)  # Skip the header row
        # Iterate over each row in the CSV file
        for rad in csv_leser:
            # Execute SQL query to insert data into the 'Post' table
            cursor.execute("INSERT INTO Post (postnummer, \"by\", kommune, fylke, kategori) VALUES (?, ?, ?, ?, ?)", rad)

# Define a function to reset the 'Post' table by deleting all rows
def reset_postnummer(cursor):
    cursor.execute("DELETE FROM Post")

# Define the main function to execute database operations
def main():
    database_navn = "min_database.db"                    # Database file name
    csv_postnummer_fil = "SQL-2/Postnummerregister-Excel.csv"  # CSV file path

    # Connect to the SQLite database using a context manager
    with sqlite3.connect(database_navn) as tilkobling:
        cursor = tilkobling.cursor()  # Obtain a cursor object for executing SQL queries

        create_postnummer_table(cursor)  # Create the 'Post' table if it doesn't exist
        import_postnummer_data(cursor, csv_postnummer_fil)  # Import data from CSV into the 'Post' table
        # reset_postnummer(cursor) 

    print("Database operation completed successfully.")  # Print a success message

# Execute the main function if this script is run as the main program
if __name__ == "__main__":
    main()
