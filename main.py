class Info:
    def __init__(self,sr,name,animal_type,breed,doctor,owner_name,phone):
        self.sr = sr
        self.name = name
        self.animal_type = animal_type
        self.breed = breed
        self.doctor = doctor
        self.owner_name = owner_name 
        self.phone = phone




def add_record():
    sr_number = int(input("please enter the serial number\n"))
    print("enter pet details\n\n")
    name = input("please enter the name of the pet\n")
    animal_type = input("please enter the type of animal\n")
    breed = input("please enter the breed of the animal\n")
    doctor = input("enter the name of the doctor assigned\n")
    print("enter owner details\n\n")
    owner_name = input("enter th eame of the owner\n")
    phone = input("enter the phone number\n")
    obj = Info(sr_number,name,animal_type,breed,doctor,owner_name,phone)
    list2 = [sr_number,name,animal_type,breed,doctor,owner_name,phone]
    f = open("records.txt","a")
    f.write(str(list2)+"\n")
    f.close()        

def modify_record():
    sr = int(input("please enter the serial number to modify pet card\n"))
    newlines = ''
    with open("records.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            l = list(line)
            if(l[1] != str(sr)):
                newlines = newlines + line

    with open("records.txt","w") as f:
        f.write(newlines)    
        sr_number = sr
        print("enter pet details\n\n")
        name = input("please enter the name of the pet\n")
        animal_type = input("please enter the type of animal\n")
        breed = input("please enter the breed of the animal\n")
        doctor = input("enter the name of the doctor assigned\n")
        print("enter owner details\n\n")
        owner_name = input("enter th eame of the owner\n")
        phone = input("enter the phone number\n")
        obj = Info(sr_number,name,animal_type,breed,doctor,owner_name,phone)
        list2 = [sr_number,name,animal_type,breed,doctor,owner_name,phone]
    with open("records.txt","a") as f:
        f.write(str(list2)+"\n")



def display():
    f = open("records.txt","r")
    lines = f.readlines()
    print(lines)
    f.close()


def delete(sr):    
    newlines = ''
    with open("records.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            l = list(line)
            if(l[1] != str(sr)):
                newlines = newlines + line
    with open("records.txt","w") as f:
        f.write(newlines)

        

if __name__ == "__main__":
    choice = str(input('\nChoose one option from the following\n\n1. Add a pet Record (add)\n2. Modify a pet record (mod)\n3. Display record (dis)\n4. Delete a record (del)\n'))
    match choice:
        case 'add':
            add_record()
        case 'mod':
            modify_record()
        case 'dis':
            display()
        case 'del':
            sr = int(input("enter the serial number of the record you want to delete\n"))
            delete(sr)
        case other:
            print("please enter a valid option\n")