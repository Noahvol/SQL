import sqlite3
import pandas as pd


conn = sqlite3.connect('random.db')
c = conn.cursor()
data = pd.read_csv('SQL-1/randoms.csv')

def funccreatedatabase():
    c.execute('''CREATE TABLE IF NOT EXISTS userData (
        fname str,
        ename str,
        epost str,
        tlf int,
        postnummer int,
        priamry key (epost)
                )''')

def funcInsertData():
    # for loop for inserting everything from csv file in corect rows
    for index, row in data.iterrows():
        c.execute(
            """
            INSERT INTO userData (fname, ename, epost, tlf, postnummer)
            VALUES (?,?,?,?,?)
            """,
            (row['fname'], row['ename'], row['epost'], row['tlf'], row['postnummer'])
        )


def main():
    funccreate_database()
    funcInsertData()


if __name__ == '__main__':
    main()

conn.commit() 
conn.close()
