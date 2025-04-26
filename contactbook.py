contact={}
while True:
    print("\n1.Add contacts")
    print("2.View contacts")
    print("3.Exit")

    choice=input("enter your choice (1/2/3):")

    if choice=='1':
        name=input("enter a name")
        phoneno=int(input("enter a number"))
        contact[name]=phoneno
        print("contact is saved")

    elif choice=='2':
        if contact:
            print("contacts")
            for name, phone in contact.items():
                print(name+":"+ str(phone))
        else:
            print("no contacts found")
    elif choice=='3':
        print("no contact saved")
        break
    else:
        print("Good bye")
        
