import sqlite3

def main():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor

    cur.execute('select * from cities.db')
    rows = cur.fetchall()

    print("Here is the table:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == '__main__':
    main()

