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
    f = open("records.txt","r")
    sr = int(input("please enter the serial number in the pet card\n"))    
    lines = f.readlines()
    #f.close()
    i = 0 
    for line in lines:
        print(line)
        i = i+1
        if (i == sr):
            sr_number = int(input("please enter the serial number\n"))
            print("enter pet details\n\n")
            name = input("please enter the name of the pet\n")
            animal_type = input("please enter the type of animal\n")
            breed = input("please enter the breed of the animal\n")
            doctor = input("enter the name of the doctor assigned\n")
            print("enter owner details\n\n")
            owner_name = input("enter th eame of the owner\n")
            phone = input("enter the phone number\n")
            list2 = [sr_number,name,animal_type,breed,doctor,owner_name,phone]
            l = str(list2)




def display():
    f = open("records.txt","r")
    lines = f.readlines()
    print(lines)
    f.close()


def delete():
    sr = input("enter the serial number of the record you want to delete\n")
    



    


#if __name__ == "__main__":
choice = str(input('\nChoose one option from the following\n\n1. Add a pet Record (add)\n2. Modify a pet record (mod)\n3. Display record (dis)\n4. Delete a record (del)\n'))
match choice:
    case 'add':
        add_record()
    case 'mod':
        modify_record()
    case 'dis':
        display()
    case 'del':
        delete()
    case other:
        print("please enter a valid option\n")