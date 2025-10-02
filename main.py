from doctor import Doctor
from medicine import Medicine
from appointment import Appointment

while True:
    print("Welcome to CMS !!!\n\nChoose any of the below option to proceed")
    userSelection = int(input('''1. Add Doctor\n2. Delete Doctor\n3. Print all doctors\n4. Add Medicine\n5. Edit Medicine\n6. Delete Medicine\n7. Print all Medicines\n8. Book Appointment\n9. Cancel Appointment\n10. Print all Appointment\n0. Quit\n\nEnter an option: '''))

    doctor = Doctor()
    medicine = Medicine()
    appointment = Appointment()

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

        case 8:
            appointment.bookAppointment()

        case 9:
            appointment.cancelAppointment()

        case 10:
            appointment.getBookedAppointments()

        case 0:
            print("Application terminated successfully")
            break
