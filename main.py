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

class comrade():
    def create_new():
        """Add a new comrade to the database"""
        conn = sqlite3.connect('comrade.db')
        cursor = conn.cursor()

        name = input('Name: ').capitalize()
        surname = input('Surname: ').capitalize()
        contact_number = input('Contact number (with international code): ')
        email = input('Email: ').lower()
        date_of_birth = input('Date of birth (YYYY-MM-DD): ')
        relation = input('Relation: ')
        location = input('Location: ')

        query = """
        INSERT INTO comrade (name, surname, contact_number, email, date_of_birth, relation, location)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (name, surname, contact_number, email, date_of_birth, relation, location))
        conn.commit()
        conn.close()

        print('New comrade added successfully!')

    def create_new_random():
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
        email = f"{name}{surname}{random.randint(10,1000)}@example.com".lower()
        date_of_birth = f"{random.randint(1950, 2006)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        relation = random.choice(["Friend", "Family Member", "Colleague"])
        location = random.choice(locations)

        query = """
        INSERT INTO comrade (name, surname, contact_number, email, date_of_birth, relation, location)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (name, surname, contact_number, email, date_of_birth, relation, location))
        conn.commit()
        conn.close()
        print("New random comrade added successfully!")

    def delete_comrade():
        """Delete a comrade from the database by ID"""
        connection = sqlite3.connect('comrade.db')
        cursor = connection.cursor()

        comrade_id = input("Enter the ID of the comrade to delete: ").strip()
        query = "DELETE FROM comrade WHERE id = ?"
        cursor.execute(query, (comrade_id,))
        connection.commit()
        connection.close()

        print("Comrade deleted successfully.")
            
    def view_all_comrades():
        """
        View all comrades in the database
        """
        connection = sqlite3.connect('comrade.db')
        cursor = connection.cursor()
        query = "SELECT * FROM comrade"
        cursor.execute(query)
        comrades = cursor.fetchall()

        table = PrettyTable([
            'ID',
            'Name',
            'Surname',
            'Contact Number',
            'Email',
            'Date of Birth',
            'Relation',
            'Location'
        ])
        table.align["ID"] = "l"
        table.align["Name"] = "l"
        table.align["Surname"] = "l"
        table.align["Contact Number"] = "l"
        table.align["Email"] = "l"
        table.align["Date of Birth"] = "l"
        table.align["Relation"] = "l"
        table.align["Location"] = "l"

        for comrade in comrades:
            table.add_row(comrade)

        print(table)
        connection.close()

class search():
    
    def by_name():
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

    def by_surname():
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

    def by_full_name():
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

    def by_date_of_birth():        
        date_of_birth = input("Search By Date of Birth: ").lower()
        name, surname = date_of_birth.split()

        conn = sqlite3.connect('comrade.db')
        cursor = conn.cursor()
        query = "SELECT * FROM comrade WHERE LOWER(name) = ?"
        cursor.execute(query, (date_of_birth))
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

    def by_email():
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

    def by_location():
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

    def by_relation():
        relation = input("Search By Relation: ")

        conn = sqlite3.connect('comrade.db')
        cursor = conn.cursor()
        query = "SELECT * FROM comrade WHERE LOWER(relation) LIKE LOWER(?)"
        cursor.execute(query, ('%' + relation.lower() + '%',))
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
def menu():
    while True:
        print("\nComrade Compendium")
        print("1. Create New Comrade")
        print("2. Create Random Comrade")
        print("3. View All Comrades")
        print("4. Search by Name")
        print("5. Search by Surname")
        print("6. Search by Full Name")
        print("7. Search by Date of Birth (YYYY-MM-DD)")
        print("8. Search by Email")
        print("9. Search by Relation")
        print("10. Search by Location")
        print("11. Delete Comrade")
        print("Q. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            comrade.create_new()
        elif choice == '2':
            comrade.create_new_random()
        elif choice == '3':
            comrade.view_all()
        elif choice == '4':
            search.by_name()
        elif choice == '5':
            search.by_surname()
        elif choice == '6':
            search.by_full_name()
        elif choice == '7':
            search.by_date_of_birth()
        elif choice == '8':
            search.by_email()
        elif choice == '9':
            search.by_relation()
        elif choice == '10':
            search.by_location()
        elif choice == '11':
            comrade.delete()
        elif choice == 'q':
            quit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
