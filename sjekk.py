import sqlite3

# Koble til databasen
conn = sqlite3.connect('tasks.db')
cur = conn.cursor()

# List alle tabeller
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()

# Skriv ut tabellene
print("Tabeller i databasen:", tables)

# Lukk tilkoblingen
conn.close()
