import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    add_phonebook_table(cur)
    add_initial_entries(cur)
    conn.commit()
    display_phonebook(cur)
    conn.close()

def add_phonebook_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Entries')
    cur.execute('''CREATE TABLE Entries 
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Name TEXT NOT NULL, 
                    PhoneNumber TEXT NOT NULL)''')

def add_initial_entries(cur):
    entries = [
        ('Tod Johnson', '565-6678-6794'),
        ('Bob Dylan', '679-5678-4567'),
        ('Issac Brown', '789-4565-4456'),
        ('Diana Pawn', '908-3444-6543'),
        ('Tony Jar', '115-6998-0848'),
        ('Suzy McSuze', '456-3498-9137'),
        ('Izzy Kol', '780-4164-2343'),
        ('Patty Pown', '304-6423-909'),
        ('John Binks', '205-5027-2947'),
        ('Patricia Scaredalot', '373-3030-3030'),
        ('Monty Python', '447-4747-3939')
    ]

    for entry in entries:
        cur.execute('''INSERT INTO Entries (Name, PhoneNumber) 
                       VALUES (?, ?)''', (entry[0], entry[1]))

def display_phonebook(cur):
    print('Contents of phonebook.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]}')

# Execute the main function.
if __name__ == '__main__':
    main()
