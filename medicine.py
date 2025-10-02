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

    def editMedicine(self):
        global medicineRecordList

        medicineId = str(input("Enter Medicine Id to edit: "))
        for medicine in medicineRecordList:
            if medicine["id"] == medicineId:
                print(f"\nCurrent details: Name = {medicine['name']}, Count = {medicine['count']}")
                print("What do you want to update?")
                print("1. Name")
                print("2. Count")

                editSelection = int(input("Enter choice (1 or 2): "))

                match editSelection:
                    case 1:
                        newName = input("Enter new medicine name: ")
                        medicine["name"] = newName
                        print("Medicine name updated successfully.")
                        
                    case 2:
                        newCount = int(input("Enter new medicine count: "))
                        medicine["count"] = newCount
                        print("Medicine count updated successfully.")

        
        print("Medicine Id not found")


    def deleteMedicine(self):
        global medicineRecordList

        medicineId = str(input("Enter Medicine Id which want to delete: "))
        for medicine in medicineRecordList:
            if medicine["id"] == medicineId:
                medicineRecordList.remove(medicine)
                print("Medicine removed successfully\n\n")
                return

        print("Medicine id not found")

    def getAllPharmacyRecords(self):
        global medicineRecordList

        if len(medicineRecordList) == 0:
            print("Medicines not available") 
            return

        for medicine in medicineRecordList:
            print(f"Medicine ID: {medicine['id']}, Medicine name: {medicine['name']}, Medicine count: {medicine['count']}\n")


            