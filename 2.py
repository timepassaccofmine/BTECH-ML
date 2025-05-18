address_book = []

def create_address_book():
    global address_book
    address_book = []
    print("Address Book Created.")

def view_address_book():
    if not address_book:
        print("Address Book is empty.")
    else:
        for i, contact in enumerate(address_book):
            print(f"{i+1}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

def insert_record():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address_book.append([name, phone, email])
    print("Record inserted.")

def delete_record():
    name = input("Enter name to delete: ")
    for contact in address_book:
        if contact[0] == name:
            address_book.remove(contact)
            print("Record deleted.")
            return    #☝️☝️
    print("Record not found.")

def modify_record():
    name = input("Enter name to modify: ")
    for contact in address_book:
        if contact[0] == name:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contact[1] = phone
            contact[2] = email
            print("Record updated.")
            return       #☝️☝️
    print("Record not found.")

while True:
    print("\nMenu:")
    print("a) Create Address Book")
    print("b) View Address Book")
    print("c) Insert Record")
    print("d) Delete Record")
    print("e) Modify Record")
    print("f) Exit")

    choice = input("Enter your choice (a-f): ")

    if choice == 'a':
        create_address_book()
    elif choice == 'b':
        view_address_book()
    elif choice == 'c':
        insert_record()
    elif choice == 'd':
        delete_record()
    elif choice == 'e':
        modify_record()
    elif choice == 'f':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
