import sqlite3
import random
from prettytable import PrettyTable

conn = sqlite3.connect('comrade.db')
cursor = conn.cursor()

# Check if table exists
cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='comrade';''')

if cursor.fetchone() is None:
    cursor.execute('''
        CREATE TABLE comrade (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            email TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            relation TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')

conn.commit()
conn.close()

def create_new():
    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()

    name = input("Input the Name: ").capitalize()
    surname = input("Input the Surname: ").capitalize()
    contact_number = input("Input the contact number with international code: ")
    email = input("Input the e-mail: ")
    date_of_birth = input("Input date of birth (YYYY-MM-DD): ")
    relation = input("What is the relation: ")
    location = input("Where do they live: ")

    # Insert data into database
    query = """
    INSERT INTO comrade (name, surname, contact_number, email, date_of_birth, relation, location)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (name, surname, contact_number, email, date_of_birth, relation, location))
    conn.commit()
    conn.close()

    print("New comrade added successfully!")

def create_random_comrade():
    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()

    names = [
        "Liam", "Emma", "Lucas", "Sophie", "Nicolas",
        "Vladimir", "Elena", "Mikhail", "Anastasia", "Mateusz",
        "Isabella", "Javier", "Francesca", "Dimitri", "Zara",
        "Petr", "Katarina", "Igor", "Svetlana", "Jarek",
        "Kwame", "Amina", "Ngozi", "Kofi", "Fatima",
        "Omar", "Layla", "Khalid", "Amira", "Yusuf",
        "Hiroshi", "Sakura", "Chen", "Ravi", "Ayesha",
        "Zainab", "Mohammed", "Chinedu", "Sunil", "Mei"
    ]

    surnames = [
        "Ivanov", "Nowak", "Kovacs", "Petrov", "Stoica",
        "Müller", "Dupont", "Martínez", "Rossi", "Smith",
        "Okafor", "Diop", "Banda", "Abebe", "Nguyen",
        "Al-Masri", "Hassan", "Rahman", "Farouk", "Nasser",
        "Tanaka", "Wang", "Kim", "Singh", "Li",
        "Mbatha", "Osei", "Khan", "Jiang", "Patel"
    ]

    locations = [
        "London, United Kingdom", "Paris, France", "Berlin, Germany", "Rome, Italy", "Madrid, Spain",
        "Moscow, Russia", "Warsaw, Poland", "Prague, Czech Republic", "Budapest, Hungary", "Bucharest, Romania",
        "Lagos, Nigeria", "Cairo, Egypt", "Johannesburg, South Africa", "Nairobi, Kenya", "Accra, Ghana",
        "Riyadh, Saudi Arabia", "Dubai, UAE", "Amman, Jordan", "Beirut, Lebanon", "Algiers, Algeria",
        "Tokyo, Japan", "Beijing, China", "Mumbai, India", "Seoul, South Korea", "Bangkok, Thailand",
        "Casablanca, Morocco", "Dakar, Senegal", "Tehran, Iran", "Hanoi, Vietnam", "Manila, Philippines"
    ]

    name = random.choice(names)
    surname = random.choice(surnames)
    contact_number = f"+{random.randint(1000000000, 9999999999)}"
    email = f"{name}{surname}{random.randint(10,1000)}@example.com"
    date_of_birth = f"{random.randint(1900, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    relation = random.choice(["Friend", "Family Member", "Colleague"])
    location = random.choice(locations)

    query = """
    INSERT INTO comrade (name, surname, contact_number, email, date_of_birth, relation, location)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (name, surname, contact_number, email, date_of_birth, relation, location))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()
    query = "SELECT * FROM comrade"
    cursor.execute(query)
    rows = cursor.fetchall()

    pt = PrettyTable(['ID', 'Name', 'Surname', 'Contact Number', 'Email', 'Date of Birth', 'Relation', 'Location'])
    pt.align["ID"] = "l"
    pt.align["Name"] = "l"
    pt.align["Surname"] = "l"
    pt.align["Contact Number"] = "l"
    pt.align["Email"] = "l"
    pt.align["Date of Birth"] = "l"
    pt.align["Relation"] = "l"
    pt.align["Location"] = "l"

    for row in rows:
        pt.add_row(row)

    print(pt)
    conn.close()

def search_by_name():
    name = input("Search By Name: ")

    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()
    query = "SELECT * FROM comrade WHERE LOWER(name) LIKE LOWER(?)"
    cursor.execute(query, ('%' + name.lower() + '%',))
    rows = cursor.fetchall()

    pt = PrettyTable(['ID', 'Name', 'Surname', 'Contact Number', 'Email', 'Date of Birth', 'Relation', 'Location'])
    pt.align["ID"] = "l"
    pt.align["Name"] = "l"
    pt.align["Surname"] = "l"
    pt.align["Contact Number"] = "l"
    pt.align["Email"] = "l"
    pt.align["Date of Birth"] = "l"
    pt.align["Relation"] = "l"
    pt.align["Location"] = "l"

    for row in rows:
        pt.add_row(row)

    print(pt)
    conn.close()

def search_by_surname():
    surname = input("Search By Surname: ")

    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()
    query = "SELECT * FROM comrade WHERE LOWER(surname) LIKE LOWER(?)"
    cursor.execute(query, ('%' + surname.lower() + '%',))
    rows = cursor.fetchall()

    pt = PrettyTable(['ID', 'Name', 'Surname', 'Contact Number', 'Email', 'Date of Birth', 'Relation', 'Location'])
    pt.align["ID"] = "l"
    pt.align["Name"] = "l"
    pt.align["Surname"] = "l"
    pt.align["Contact Number"] = "l"
    pt.align["Email"] = "l"
    pt.align["Date of Birth"] = "l"
    pt.align["Relation"] = "l"
    pt.align["Location"] = "l"

    for row in rows:
        pt.add_row(row)

    print(pt)
    conn.close()

def search_by_full_name():
    full_name = input("Search By Full Name: ").lower()
    name, surname = full_name.split()

    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()
    query = "SELECT * FROM comrade WHERE LOWER(name) = ? AND LOWER(surname) = ?"
    cursor.execute(query, (name, surname))
    rows = cursor.fetchall()

    pt = PrettyTable(['ID', 'Name', 'Surname', 'Contact Number', 'Email', 'Date of Birth', 'Relation', 'Location'])
    pt.align["ID"] = "l"
    pt.align["Name"] = "l"
    pt.align["Surname"] = "l"
    pt.align["Contact Number"] = "l"
    pt.align["Email"] = "l"
    pt.align["Date of Birth"] = "l"
    pt.align["Relation"] = "l"
    pt.align["Location"] = "l"

    for row in rows:
        pt.add_row(row)

    print(pt)
    conn.close()

def search_by_email():
    email = input("Search By Email: ")

    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()
    query = "SELECT * FROM comrade WHERE LOWER(email) LIKE LOWER(?)"
    cursor.execute(query, ('%' + email.lower() + '%',))
    rows = cursor.fetchall()

    pt = PrettyTable(['ID', 'Name', 'Surname', 'Contact Number', 'Email', 'Date of Birth', 'Relation', 'Location'])
    pt.align["ID"] = "l"
    pt.align["Name"] = "l"
    pt.align["Surname"] = "l"
    pt.align["Contact Number"] = "l"
    pt.align["Email"] = "l"
    pt.align["Date of Birth"] = "l"
    pt.align["Relation"] = "l"
    pt.align["Location"] = "l"

    for row in rows:
        pt.add_row(row)

    print(pt)
    conn.close()

def search_by_location():
    location = input("Search By Location: ")

    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()
    query = "SELECT * FROM comrade WHERE LOWER(location) LIKE LOWER(?)"
    cursor.execute(query, ('%' + location.lower() + '%',))
    rows = cursor.fetchall()

    pt = PrettyTable(['ID', 'Name', 'Surname', 'Contact Number', 'Email', 'Date of Birth', 'Relation', 'Location'])
    pt.align["ID"] = "l"
    pt.align["Name"] = "l"
    pt.align["Surname"] = "l"
    pt.align["Contact Number"] = "l"
    pt.align["Email"] = "l"
    pt.align["Date of Birth"] = "l"
    pt.align["Relation"] = "l"
    pt.align["Location"] = "l"

    for row in rows:
        pt.add_row(row)

    print(pt)
    conn.close()

def delete_comrade():
    conn = sqlite3.connect('comrade.db')
    cursor = conn.cursor()

    comrade_id = input("Enter the ID of the comrade to delete: ")
    query = "DELETE FROM comrade WHERE id = ?"
    cursor.execute(query, (comrade_id,))
    conn.commit()
    conn.close()

    print("Comrade deleted successfully!")

def menu():
    while True:
        print("\nComrade Compendium")
        print("1. Create New Comrade")
        print("2. Create Random Comrade")
        print("3. View All Comrades")
        print("4. Search by Name")
        print("5. Search by Surname")
        print("6. Search by Full Name")
        print("7. Search by Email")
        print("8. Search by Location")
        print("9. Delete Comrade")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_new()
        elif choice == '2':
            create_random_comrade()
        elif choice == '3':
            view_all()
        elif choice == '4':
            search_by_name()
        elif choice == '5':
            search_by_surname()
        elif choice == '6':
            search_by_full_name()
        elif choice == '7':
            search_by_email()
        elif choice == '8':
            search_by_location()
        elif choice == '9':
            delete_comrade()
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
