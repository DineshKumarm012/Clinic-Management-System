medicineRecordList = []

class Medicine:

    def addMedicine(self):
        global medicineRecordList

        medicineId = str(input("Enter Medicine Id: "))
        medicineName = str(input("Enter Medicine Name: "))
        medicineCount = int(input("Enter Medicine package count: "))

        medicineRecordList.append(
            {
                "id": medicineId,
                "name": medicineName,
                "count": medicineCount
            }
        )
        print(f"Medicine added successfully\n\n")

