import os
import time
ADDRESS_BOOK = os.path.join(os.getcwd(),"a1.txt")

# # Init Function to load Selected Addressbook
# def init():
#     global ADDRESS_BOOK
#     fd = os.open('settings',os.O_RDONLY)
#     ADDRESS_BOOK = os.read(fd,os.stat('settings').st_size).decode('utf-8')

# Function to Create a Addressbook
def createAddressBook():
    name = input("Enter Name for Addressbook: ")
    try:
        fd = os.open(f"{name.strip()}.txt", os.O_CREAT)
        print(f"Addressbook with name: '{name.strip()}' is Created Succesfully.")
        global ADDRESS_BOOK
        ADDRESS_BOOK=f"{name.strip()}.txt"
    except Exception as e:
        print("Address Book Creation Failed, Enter Propper Name for Addressbook.")

# Create New Contact
def newContact():
    if not os.path.exists(ADDRESS_BOOK):
        print("File does not exist!")
        return
    fdw = os.open(ADDRESS_BOOK, os.O_RDWR | os.O_APPEND)
    name = input("Name: ")
    phn = input("Phone Number: ")
    address = input("Enter Address : ")
    email = input("Enter Email: ")
    data = f"Name: {name} | Phone Number: {phn} | Address: {address} | Email: {email}\n"
    os.write(fdw, data.encode('utf-8'))
    print("New Phone Number Saved!\n")
    os.close(fdw)

# Read certain Contact
def readContact():
    if not os.path.exists(ADDRESS_BOOK):
        print("File does not exist!")
        return
    name=input("Enter name: ")
    fd = os.open(ADDRESS_BOOK, os.O_RDWR | os.O_APPEND)
    ret = os.read(fd, os.stat(ADDRESS_BOOK).st_size)
    # print(ret.decode('utf-8'))
    content=ret.decode('utf-8')
    matching_lines=[line for line in content.splitlines() if name.lower() in line.lower()]
    for i in matching_lines:
        print(i)
    os.close(fd)

# Delete Contact
def deleteContact():
    if not os.path.exists(ADDRESS_BOOK):
        print("File does not exist!")
        return
    name = input("Enter Name/Contact/Address/Email of the contact to be deleted: ")
    fd = os.open(ADDRESS_BOOK, os.O_RDONLY)  
    file_size = os.stat(ADDRESS_BOOK).st_size
    content = os.read(fd, file_size).decode('utf-8')  
    os.close(fd) 
    
    n_content = [line for line in content.splitlines() if name.lower() in line.lower()]

    if len(n_content) == 0:
        print(f"No Contact found with content '{name}'.")
        return

    print("Choose Contact Index for Deletion.")
    for i in range(len(n_content)):
        print(f"[{i}] = {n_content}")

    index = int(input("Index: "))
    if not index >= len(n_content):
        deletionLine = n_content[index]
    else:
        print("Index Not Found! Try Again.")
        return

    new_content = "\n".join([line for line in content.splitlines() if not line == deletionLine])

    fdw = os.open(ADDRESS_BOOK, os.O_WRONLY | os.O_TRUNC) 
    os.write(fdw, new_content.encode())
    print(f"Contact '{name}' is deleted!\n")
    os.close(fdw)

# Modify Contact
def modify():
    if not os.path.exists(ADDRESS_BOOK):
        print("File does not exist!")
        return
    name = input("Enter the Name/Contact/Address/Email of the contact you want to modify: ")
    fd = os.open(ADDRESS_BOOK, os.O_RDWR)
    
    file_size = os.stat(ADDRESS_BOOK).st_size
    file_content = os.read(fd, file_size).decode('utf-8')
    
    lines = file_content.splitlines()
    
    modified = False
    for i in range(len(lines)):
        if name.lower() in lines[i].lower():
            print(f"Contact Found: {lines[i]}")
            parts = lines[i].split('|')
            
            new_name = input(f"Enter New Name (Keep Empty for Continue '{parts[0].split(':')[1].strip()}'): ")
            if len(new_name) > 1:
                parts[0] = f"Name : {new_name} "

            new_contact = input(f"Enter New Contact (Keep Empty for Continue '{parts[1].split(':')[1].strip()}'): ")
            if len(new_contact) > 1:
                parts[1] = f" Phone Number: {new_contact} "

            new_address = input(f"Enter New Address (Keep Empty for Continue '{parts[2].split(':')[1].strip()}'): ")
            if len(new_address) > 1:
                parts[2] = f" Address : {new_address} "

            new_email = input(f"Enter New Email (Keep Empty for Continue '{parts[3].split(':')[1].strip()}'): ")
            if len(new_email) > 1:
                parts[3] = f" Email : {new_email} "

            updated_contact = '|'.join(parts)
            lines[i] = updated_contact
            modified = True
            print(f"Contact updated: {updated_contact}")
            break
    
    if modified:
        os.open(ADDRESS_BOOK, os.O_WRONLY | os.O_TRUNC) 
        fd = os.open(ADDRESS_BOOK, os.O_WRONLY)
        os.write(fd, "\n".join(lines).encode('utf-8'))
        print("Contact has been modified successfully!")
    else:
        print("Contact not found!")
    os.close(fd)

# init()  # Load the default address book from 'settings' file

while True:
    print(f""" -------- [{ADDRESS_BOOK.replace('.txt','')}] --------
    1. Create New Addressbook
    2. Create New Contact
    3. Read certain Contacts
    4. Delete Contact
    5. Modify a Contact
    6. Exit
    """)
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        createAddressBook()
    elif choice == 2:
        newContact()
    elif choice == 3:
        readContact()
    elif choice == 4:
        deleteContact()
    elif choice == 5:
        modify()
    elif choice == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please choose a valid option.")
