from doctor import Doctor
from medicine import Medicine

while True:
    print("Welcome to CMS !!!\n\nChoose any of the below option to proceed")
    userSelection = int(input('''1. Add Doctor\n2. Delete Doctor\n3. Print all doctors\n4. Add Medicine\n5. Edit Medicine\n6. Delete Medicine\n7. Print all Medicines\n0. Quit\n\nEnter an option: '''))

    doctor = Doctor()
    medicine = Medicine()

    match userSelection:
        case 1:
            doctor.addDoctor()

        case 2:
            doctor.deleteDoctor()

        case 3:
            doctor.getAllDoctorInfo()

        case 4:
            medicine.addMedicine()

        case 5:
            medicine.editMedicine()

        case 6:
            medicine.deleteMedicine()

        case 7:
            medicine.getAllPharmacyRecords()

        case 0:
            print("Application terminated successfully")
            break
