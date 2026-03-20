import json
import sys

def load_contacts() :
    try:
        with open("contacts.json","r") as file:
            return json.load(file)
    except:
        return{}
    
def save_contacts(contacts):
    with open("contacts.json","w") as file:
        json.dump(contacts,file,indent=4)

def add_contact() :
           name = input("Enter the name : ") # add a new contact
           no = input("Enter the number :")
           if (len(no) != 10) :
               print("INVALID ENTER AGAIN")
               no = input("Enter the number :")
           else :
               contacts.update({name:no})
               save_contacts(contacts)
               print("ADDED sucessfully\n")

def update_contact() :
          name = input("Enter the name : ")  # update a contact
          if name in contacts :
              num = input("Enter the number :")
              contacts[name]=num
              save_contacts(contacts)
              print("UPDATED sucessfully\n")

          else :
                print("Contact NOT FOUND\n")

def delete_contact() :
           name = input("Enter the name : ")  # delete a contact
           if name in contacts:                  
               contacts.pop(name)
               save_contacts(contacts)
               print("DELETED sucessfully\n")

           else :
                print("Contact NOT FOUND\n")

def search_contact() :
            name = input("Enter the name : ") # search contact
            if name in contacts:
              print(f"found with number :{contacts.get(name)}\n")
            else :
               print("NOT found\n")

def view_contacts() :
            print("\n----- CONTACT LIST -----\n")  # View Contacts
            for key,value in contacts.items():
                print(f"{key} : {value}")
            print("\n")

def sys_exit() :
     print("THANS FOR USING")
     sys.exit()

           


print("\n===== CONTACT MANAGEMENT SYSTEM =====\n")
print("A.Add a new contact")
print("B.Update a contact")
print("C.Delete a contact")
print("D.Search a contact")
print("E.To view all contacts")
print("F.Exit\n")

contacts = load_contacts()

while True:


    user = input("enter the option : ")

    match user :
        case'A' : add_contact() 
           
        case'B' : update_contact()
           
        case 'C' : delete_contact()

        case 'D' : search_contact()

        case 'E' : view_contacts()
        
        case 'F' : sys_exit()
              