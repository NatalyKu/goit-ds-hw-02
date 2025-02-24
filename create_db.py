import sqlite3
"""#import os


def create_db():
# читаємо файл зі скриптом для створення БД
    #script_dir = os.path.dirname(__file__)  # Få katalogen til skriptet
    #os.chdir(script_dir)  # Endre arbeidskatalogen til skriptets katalog
    #print("Current working directory:", os.getcwd())
    with open('./ds-hw-02/tasks.sql', 'r') as f:
        sql = f.read()

# створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('./ds-hw-02/tasks.sql') as con:

        cur = con.cursor()
# виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)
        print("Database og tabeller opprettet vellykket")

if __name__ == "__main__":
    create_db()
"""

def create_db():
    # Les SQL-skriptet fra filen
    with open('tasks.sql', 'r') as f:
        sql = f.read()

    # Opprett eller koble til en SQLite-database
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        # Utfør SQL-skriptet for å opprette tabellene i databasen
        cur.executescript(sql)
        print("Database og tabeller opprettet vellykket")

if __name__ == "__main__":
    create_db()