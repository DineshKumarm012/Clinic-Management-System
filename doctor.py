doctorList = []

class Doctor:

    def addDoctor(self):
        global doctorList

        doctorId = str(input("Enter Doctor Id: "))
        doctorName = str(input("Enter Doctor Name: "))
        doctorMobileNumber = str(input("Enter Doctor Mobile Number: "))
        doctorSpeciality = str(input("Enter Doctor Speciality: "))

        doctorList.append(
            {
                "id": doctorId,
                "name": doctorName,
                "mobile_number": doctorMobileNumber,
                "speciality": doctorSpeciality
            }
        )
        print(f"Doctor added successfully\n\n")

    def deleteDoctor(self):
        global doctorList

        doctorId = str(input("Enter Doctor Id which want to delete: "))
        for doctor in doctorList:
            if doctor["id"] == doctorId:
                doctorList.remove(doctor)
                print("Doctor removed successfully\n\n")
                return

        print("Doctor id not found")

    def getAllDoctorInfo(self):
        global doctorList

        if len(doctorList) == 0:
            print("Doctors not found")
            return

        for doctor in doctorList:
            print(f"Doctor ID: {doctor['id']}, Doctor name: {doctor['name']}\n")

