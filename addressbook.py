import os

ADDRESS_BOOK=os.path.join(os.getcwd(),"a1.txt")

def create_ab():
    global ADDRESS_BOOK
    name=input("Enter name of address book")
    try:
        fd=os.open(f"{name.strip()}.txt",os.O_CREAT)
        print(f"Address book with name:{name.strip()}.txt created.")
    except Exception as e:
        print("Address book could not be created")

def view_ab():
    name=input("Enter name")
    fd=os.open(ADDRESS_BOOK,os.O_RDONLY)
    ret=os.read(fd,os.stat(fd).st_size)
    content=ret.decode('utf-8')
    # matching_lines=[line for line in content.splitlines() if name.lower() in line.lower()]
    # for i in matching_lines:
    #     print(i)
    print(content)
    os.close(fd)

def new_contact():
    if os.path.exists(ADDRESS_BOOK):
        name=input("Enter name")
        contact=input("Enter contact")
        address=input("Enter address")
        email=input("Enter email")
        fd=os.open(ADDRESS_BOOK,os.O_APPEND | os.O_RDWR)
        line=f"Name: {name} | phone number: {contact} | Address: {address} | email: {email}\n"
        os.write(fd,line.encode('utf-8'))
        os.close(fd)

def delete():
    fd=os.open(ADDRESS_BOOK,os.O_RDONLY)
    ret=os.read(fd,os.stat(ADDRESS_BOOK).st_size)
    content=ret.decode('utf-8')
    name=input("Enter name")

    matching=[line for line in content.splitlines() if name.lower() in line]

    for i in range(len(matching)):
        print(f"index={i} || {matching[i]}")
    del_ind=int(input("Enter index to be deleted"))

    del_lines=matching[del_ind]
    new=''
    for line in content.splitlines():
        if not line == del_lines:
            new+=line+"\n"


    fdw=os.open(ADDRESS_BOOK,os.O_WRONLY | os.O_TRUNC)
    os.write(fdw,new.encode('utf-8'))
    os.close(fd)
    os.close(fdw)
    
def modify():
    fd=os.open(ADDRESS_BOOK,os.O_RDONLY)
    ret=os.read(fd,os.stat(ADDRESS_BOOK).st_size)
    content=ret.decode('utf-8')
    name=input("Enter your name to modify that record: ")
    lines=content.splitlines()
    line=""
    for i in lines:
        if name.lower() in i.lower():
            line=i
    print("line is: ",line)
    new=""
    for i in lines:
        if not i==line:
            new+=i+'\n'
    fdw=os.open(ADDRESS_BOOK,os.O_WRONLY | os.O_TRUNC)
    os.write(fdw,new.encode('utf-8'))
    os.close(fd)
    os.close(fdw)
    print("Enter new modified record")
    new_contact()
    

# create_ab()
# view_ab()
# new_contact()
# delete()
# modify()

while True:
    print("\n===== ADDRESS BOOK MENU =====")
    print("1. Create Address Book")
    print("2. View Address Book")
    print("3. Add New Contact")
    print("4. Delete Contact")
    print("5. Modify Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_ab()
    elif choice == '2':
        view_ab()
    elif choice == '3':
        new_contact()
    elif choice == '4':
        delete()
    elif choice == '5':
        modify()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
