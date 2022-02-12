import classes

def main():



    first_doctor = classes.Doctor("Jose" , "bubu" , "nutritionist" , 23)
    first_patient = classes.Patient("katy" , "kaka" , "+962777071631" , "Jose")

    print(first_doctor.name)
    print(first_patient.name)

    first_doctor.change_name("qais")
    print(first_doctor.name)

if __name__ == '__main__':
    main()





