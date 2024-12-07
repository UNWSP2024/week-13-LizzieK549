import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    #creating a while true statement so users can choose what they would like to do
    while True:
        print("Main Menu:")
        print("1. Display all entries")
        print("2. Look up a person's phone number")
        print("3. Update a person's phone number")
        print("4. Delete an entry")
        print("0. Exit")

        UserInput = input("please enter the corresponding number to your command: ")

        if UserInput == '1':
            DisplayEntries(cur)
        elif UserInput == '2':
            name = input("Enter name of user to look up: ")
            PhoneNumberLookup(cur, name)
        elif UserInput == '3':
            name = input("Enter name of user: ")
            ReplacePhoneNumber = input("Enter new phone number: ")
            UpdatePhoneNumber(cur, name, ReplacePhoneNumber)
        elif UserInput == '4':
            name = input("Enter name to delete: ")
            DeleteEntry(cur, name)
        elif UserInput == '0':
            break
        else:
            print("invalid UserInput- choose again")

    conn.commit()    #make sure changes were added
    conn.close()


def DisplayEntries(cur):
    cur.execute('SELECT * from Entries')
    rows = cur.fetchall()
    print("Here is the table:")
    for row in rows:
        print(row)

def PhoneNumberLookup(cur, name):
    cur.execute('SELECT PhoneNumber FROM Entries WHERE Name = ?', (name,))
    phone_number = cur.fetchone()
    if phone_number:
        print(f"{name}'s phone number is {phone_number[0]}")
    else:
        print(f"No entry found for {name}")

def UpdatePhoneNumber(cur, name, ReplacePhoneNumber):
    cur.execute('UPDATE Entries SET PhoneNumber = ? WHERE Name = ?', (ReplacePhoneNumber, name))
    print(f"Updated {name}'s phone number to {ReplacePhoneNumber}")

def DeleteEntry(cur, name):
    cur.execute('DELETE FROM Entries WHERE Name = ?', (name,))
    print(f" {name} deleted from database")



if __name__ == '__main__':
    main()

