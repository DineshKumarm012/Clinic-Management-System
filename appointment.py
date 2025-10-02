appointmentList = []

class Appointment:

    def bookAppointment(self):
        global appointmentList

        bookingId = str(input("Enter Booking Id: "))
        patientName = str(input("Enter patient Name: "))
        reason = str(input("Reason for visit: "))

        appointmentList.append(
            {
                "id": bookingId,
                "patient_name": patientName,
                "reason": reason
            }
        )
        print(f"Appointment booked successfully. Booking Id: {bookingId}\n\n")

            
    def cancelAppointment(self):
        global appointmentList

        bookingId = str(input("Enter booking Id which want to cancel: "))
        for appointment in appointmentList:
            if appointment["id"] == bookingId:
                appointmentList.remove(appointment)
                print("Appointment canceled successfully\n\n")
                return

        print("Booking id not found")

    def getBookedAppointments(self):
        global appointmentList

        if len(appointmentList) == 0:
            print("Appointments not booked")
            return

        for appointment in appointmentList:
            print(f"Booking ID: {appointment['id']}, Patient name: {appointment['patient_name']}, Reason for visit: {appointment['reason']}\n")

