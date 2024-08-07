#contact
# welcome to contact book
# book we have to add contact book,remove contact
#ask for name and phone number
#view an number by seaching 
contact_book= {}
# {"manas": {"phone": 3456789, "email": abc@domain.com}, }
def add_number():
    n = int(input("enter the number of contacts you want to add: "))
    for i in range(n):
        name = input("Enter the name of the person: ")
        phone_number= int(input("enter the number of the person: "))
        email = input("enter the email")
        contact_book[name] = {"phone_number": phone_number, "emai;": email}    
        print("The contact has added successfully. ")
def view_contactbook():
    #result = contact_book.items()
    #print(f"the full contact book is: {result}")
    for name, details in contact_book.items():
        print(f"name: {name}")
        for info_type, info_detail in details.items():
            print(f"\t{info_type} : {info_detail}")
    
def remove_contact():
    removed_contact = input("enter the name of the contact you want to remove: ")
    contact_book.pop(removed_contact)
    print("this contact has been removed")
    print(contact_book)
def search_contact():
    search_contact = input("enter the contact you want to search: ")
    result = contact_book[search_contact]
    print(result)
    
while True:
    print("WELCOME TO THE CONTACT BOOK")
    print("""what you want to do 
            1.Add Contact in the contact list
            2. View all contacts in contact list
            3.Remove the contact from the contact list
            4.Search the contact""")
    choice = input("Enter your choice via 1/2/3: ")
    if choice == '1':
        add_number()
    elif choice == '2':
        view_contactbook()
    elif choice == '3':
        remove_contact()
    elif choice == '4':
        search_contact()

    choice_2nd = input("do you want to continue the operations 'y' for yes 'n' for no: ")
    if choice_2nd == 'n':
        print("THANK YOU") 
        break   

    