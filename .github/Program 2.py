import sqlite3

def display_cities():
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM Cities')

        print("Contents of the Cities database:")
        for row in cur:
            print(row)

    except sqlite3.Error as e:
        print(f"An error has occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    display_cities()


# #Display a list of cities sorted by population, in ascending order.
# #Display a list of cities sorted by population, in descending order.
# #Display a list of cities sorted by name.
# #Display the total population of all the cities.
# #Display the average population of all the cities.
# #Display the city with the highest population.
# #Display the city with the lowest population.
#
# import sqlite3
#
# def main():
#     conn = sqlite3.connect('cities.db')
#     cur = conn.cursor()
#     add_cities_table(cur)
#     add_cities(cur)
#     conn.commit()
#     display_cities(cur)
#     conn.close()
#
#
# def add_cities_table(cur):
#     cur.execute('DROP TABLE IF EXISTS Cities')
#     cur.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
#                                         CityName TEXT,
#                                         Population REAL)''')
#
#
# # The add_cities function adds 20 rows to the Cities table.
# def add_cities(cur):
#     cities_pop = [(1, 'Tokyo', 38001000),
#                   (2, 'Delhi', 25703168),
#                   (3, 'Shanghai', 23740778),
#                   (4, 'Sao Paulo', 21066245),
#                   (5, 'Mumbai', 21042538),
#                   (6, 'Mexico City', 20998543),
#                   (7, 'Beijing', 20383994),
#                   (8, 'Osaka', 20237645),
#                   (9, 'Cairo', 18771769),
#                   (10, 'New York', 18593220),
#                   (11, 'Dhaka', 17598228),
#                   (12, 'Karachi', 16617644),
#                   (13, 'Buenos Aires', 15180176),
#                   (14, 'Kolkata', 14864919),
#                   (15, 'Istanbul', 14163989),
#                   (16, 'Chongqing', 13331579),
#                   (17, 'Lagos', 13122829),
#                   (18, 'Manila', 12946263),
#                   (19, 'Rio de Janeiro', 12902306),
#                   (20, 'Guangzhou', 12458130)]
#
#     for row in cities_pop:
#         cur.execute('''INSERT INTO Cities (CityID, CityName, Population)
#                        VALUES (?, ?, ?)''', (row[0], row[1], row[2]))
#
#
# # The display_cities function displays the contents of
# # the Cities table.
# def display_cities(cur):
#     print('Contents of cities.db/Cities table:')
#     cur.execute('SELECT * FROM Cities')
#     results = cur.fetchall()
#     for row in results:
#         print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')
#
#
# # Execute the main function.
# if __name__ == '__main__':
#     main()