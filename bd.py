import sqlite3

conn = sqlite3.connect('jaillist.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS jaillist (
    name TEXT,
    second_name TEXT,
    age INTEGER,
    article INTEGER,
    term INTEGER,
    release_date DATETIME  
)
''')

def add_prisoner(name, second_name, age,article, term, release_date):
    cursor.execute('''
    INSERT INTO jaillist (name, second_name, age, article, term, release_date) 
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, second_name, age, article, term, release_date))
    conn.commit()
    print(f"Prisoner '{name} {second_name}' added successfully.")

#add_prisoner("Bogdan","Vor",54,115,20,'2044-05-05')

def get_release_date(name, second_name):
    conn = sqlite3.connect('jaillist.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT release_date 
    FROM jaillist
    WHERE name = ? AND second_name = ? 
    ''', (name, second_name))

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return f"No prisoner found with given details."

print(get_release_date("Bogdan","Vor"))

