
import json

with open("D:/VS_code/json_data.json") as f:
    data = json.load(f)

removed_duplicates = []

def department_list(count):
    for i in data["doctors"]:
        if i["department"] not in removed_duplicates:
            removed_duplicates.append(i["department"])#deleting duplicate names of departments 

        
    for i in removed_duplicates:
        count = count + 1
        print("Dept №", count, "is",  i)
        

#picking the department number function2
def pick_department(department_number):

        oncology_docs = []
        cardiology_docs = []
        dermatology_docs = [] 
        ginecology_docs = []
        if department_number == 1:
            department_number = "oncology"
            for i in data["doctors"]:
                if i["department"] == department_number:
                    oncology_docs.append(i["name"])
                    #print("List of doctors in", department_number, "are: ", i["name"] )

            print("List of doctors in", department_number, "department: ", oncology_docs )
        elif department_number == 2:
            department_number = "cardiology"
            for i in data["doctors"]:
                if i["department"] == department_number:
                    cardiology_docs.append(i["name"])
                    
            print("List of doctors in", department_number, "department: ", cardiology_docs )
        elif department_number == 3:
            department_number = "dermatology"
            for i in data["doctors"]:
                if i["department"] == department_number:
                    dermatology_docs.append(i["name"])
                    
            print("List of doctors in", department_number, "department: ", dermatology_docs )
        elif department_number == 4:
            department_number = "ginecology"
            for i in data["doctors"]:
                if i["department"] == department_number:
                    ginecology_docs.append(i["name"])
            print("List of doctors in", department_number, "department: ", ginecology_docs )


def make_an_appointment(pick_a_doctor):
    free_time = []
    patients = []
    
    for i in data["doctors"]:
        if i["name"] == pick_a_doctor:
            free_time.append(i["free_time_slot"])
    print("This is the available time of doctor ", pick_a_doctor, ": ", free_time )

    appointment = input("Do you want to make an appointment?  yes/no: ")
    if appointment == "yes":
        slot = input("Pick a time slot suitable for you:")
        for i in free_time:
            if i == slot:
                free_time.remove(i)
        patient_name= input("Enter your first name: ")
        patient_surname = input("Enter your surname: ")
        date_of_birth = input("Enter your date of birth (HINT: 21.09.1997): " )
        ssn = int(input("Enter your social security number"))
        patient_info= { 
            "Name" : patient_name,
            "Surname": patient_surname,
            "Date of birth": date_of_birth,
            "Social security number": ssn
            }

        print("You have made an appointment with doctor: ", pick_a_doctor, " at: ", slot)

        with open("add_patients.txt", "w") as f:
            f.write(json.dumps(patient_info))
                

    



count = 0
department_list(count)
department_number = int(input("Type in the number of department that you want: "))
pick_department(department_number)
pick_a_doctor = input("Type in the name of the doctor and see his free slots: ")
make_an_appointment(pick_a_doctor)



#def doctor_database(department_num, ):
    

