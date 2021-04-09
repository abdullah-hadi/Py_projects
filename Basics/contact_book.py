contactbook= {}
print("\\\-----welcome to neptune contactbook-----//")

while True:
    
    key=int(input("1.Add contact\n2.Find contact\n3.Full contactbook\n4.Delete contact\n5.Exit\n"))

    if key==1:
        name=input("enter name: ")
        
        number=input("enter number: ")
        contactbook[name.title()]=number
        print(f"Name: {name} Number: {number} successfully added\n")

    
    if key==2:
        name=input("enter contact name: ")
        
        if name.title() in contactbook:
            print(contactbook[name.title()],"\n")
        else:
            print("contact not found!\n")

    
    if key==3:
        print(contactbook,"\n")

    
    if key==4:
        name=input("enter contact name to delete: ")
        
        if name.title() in contactbook:
            del contactbook[name.title()]
            print(f"successfully deleted {name}\n")
        else:
            print("no contacts matched\n")

    
    if key==5:
        print("thank you for using neptune")
        quit()
        

