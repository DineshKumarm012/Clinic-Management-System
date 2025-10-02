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

            