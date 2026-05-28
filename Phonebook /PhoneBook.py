#CLI Phonebook Data persistence using local text files.
import  os

DATA_FILE="phone_textbook"
def crate_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE,'w',encoding="utf-8"):
            pass
def add_contact():
    name=input("enter the name ").strip()
    while True:
        phone=input("enter the number ").strip()    
        if not phone.isdigit():
            print("enter number for phone please!")
        else:
            break    

    if name and phone:
        with open(DATA_FILE,"a",encoding="utf-8") as f:
            f.write(f"{name}:{phone}\n")
            print(f"{name} is add ")
    else:
        print("please enter name and phone again")        
def list_contacts():
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) >0:
        print("NAME\tPHONE")
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            for line in f:
                name,phone=line.strip().split(":")
                print(f"{name}\t{phone}")  
    else:
        print("phonebook is empty")  
def search_contact():
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) >0:
        search_name=input("enter name to search ").lower().strip()
        found=False
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            for line in f:
                name,phone=line.strip().split(":")
                if search_name in name.lower():
                    print(f"{name} : {phone}")
                    found=True
        if not found:
            print(f"{search_name} is not in the list")
    else:
        print("phonebook is empty")
def main_menu():
    crate_file()
    while True:
        print("\n--- Phonebook Menu ---")
        print("1.adding contact")
        print("2.show all contacts")
        print("3.search contact")
        print("4.exit")
        
        choice = input("enter(1-4): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋BYE ")
            break
        else:
            print("enter valid number!!!")

if __name__ == "__main__":
    main_menu()

                