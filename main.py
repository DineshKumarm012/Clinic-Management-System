from doctor import Doctor

while True:
    print("Welcome to CMS !!!\n\nChoose any of the below option to proceed")
    userSelection = int(input('''1. Add Doctor\n2. Delete Doctor\n3. Print all doctors\n0. Quit\n\nEnter an option: '''))

    doctor = Doctor()
    match userSelection:
        case 1:
            doctor.addDoctor()

        case 2:
            doctor.deleteDoctor()

        case 3:
            doctor.getAllDoctorInfo()

        case 0:
            print("Application terminated successfully")
            break
