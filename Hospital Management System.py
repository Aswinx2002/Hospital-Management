import re
from datetime import datetime

login_credentials = {
    "Admin": "123",
    "Receptionist": "456",
    "Pharmacist": "789",
    "LabTechnician": "012"
}

staff_data = {}
patient_data = {}
medicine_data = {}
lab_tests_list = []

print("\n______Faith Hospital_____")

def login():
    print("\n______Login_____\n")
    import datetime

    def record_attempt(username, result):
        with open("Log.txt", "a") as file:
            file.write(f"{datetime.datetime.now()} - Login ID: {username} - Result: {result}\n")

    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in login_credentials and login_credentials[username] == password:
            record_attempt(username, "Success")
            print(f"\nWelcome {username}!")
            return username
        else:
            attempts += 1
            if attempts < max_attempts:
                print("\nInvalid username/password. Please correct.\n")
                record_attempt(username, "Failed = Invalid username/password")
            else:
                print("You have reached maximum attempt. Please try again.")
                record_attempt(username, "Failed = reached maximum attempt")
    return None

def main():
    user_role = login()
    if user_role:
        while True:
            if user_role == "Admin":
                print("\nAdmin Menu:")
                print("1. List All Staff")
                print("2. Add Staff")
                print("3. Search Staff")
                print("4. Edit Staff")
                print("5. Delete Staff")
                print("6. Logout")
                choice = input("Enter your choice: ")
                if choice == "1":
                    list_staff()
                elif choice == "2":
                    add_staff()
                elif choice == "3":
                    search_staff()
                elif choice == "4":
                    edit_staff()
                elif choice == "5":
                    delete_staff()
                elif choice == "6":
                    print("\nYou have logged out as Admin successfully")
                    break
                else:
                    print("Invalid choice.")

            elif user_role == "Receptionist":
                print("\nReceptionist Menu:")
                print("1. List All Patients")
                print("2. Add Patient")
                print("3. Search Patient")
                print("4. Edit Patient")
                print("5. Logout")
                choice = input("Enter your choice: ")
                if choice == "1":
                    list_patients()
                elif choice == "2":
                    add_patient()
                elif choice == "3":
                    search_patient()
                elif choice == "4":
                    edit_patient()
                elif choice == "5":
                    print("\nYou have logged out as Receptionist successfully")
                    login()
                    break
                else:
                    print("Invalid choice.")

            elif user_role == "Pharmacist":
                print("\nPharmacist Menu:")
                print("1. List All Medicines")
                print("2. Add Medicine")
                print("3. Search Medicine")
                print("4. Edit Medicine")
                print("5. Delete Medicine")
                print("6. Logout")
                choice = input("Enter your choice: ")
                if choice == "1":
                    list_medicines()
                elif choice == "2":
                    add_medicine()
                elif choice == "3":
                    search_medicine()
                elif choice == "4":
                    edit_medicine()
                elif choice == "5":
                    delete_medicine()
                elif choice == "6":
                    break
                else:
                    print("Invalid choice.")

            elif user_role == "LabTechnician":
                print("\nLab Technician Menu:")
                print("1. Add Lab Test")
                print("2. List Lab Tests")
                print("3. Search Lab Test by Code or Name")
                print("4. Edit Lab Test")
                print("5. Delete Lab Test")
                print("6. Logout")
                choice = input("Enter your choice: ")
                if choice == "1":
                    add_lab_test()
                elif choice == "2":
                    list_lab_tests()
                elif choice == "3":
                    search_lab_test()
                elif choice == "4":
                    edit_lab_test()
                elif choice == "5":
                    delete_lab_test()
                elif choice == "6":
                    print("\nYou have logged out as LabTechnician successfully")
                    login()
                    break
                else:
                    print("Invalid choice.")
            else:
                print("Invalid role.")
                break

# Function to add staff
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Function to calculate age based on date of birth
def calculate_age(dob):
    birth_date = datetime.datetime.strptime(dob, "%d/%m/%Y")
    today = datetime.datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Function to add staff
def add_staff():
    while True:
        staff_id = input("Enter staff ID: ").strip()
        if staff_id not in staff_data:
            break
        print("Error: Staff ID already exists. Please enter a unique ID.")

    while True:
        fullname = input("Enter full name: ").strip()
        if fullname.replace(" ", "").isalpha():
            break
        print("Error: Full name should contain only alphabetic characters and spaces.")

    while True:
        dob = input("Enter date of birth (dd/mm/yyyy): ").strip()
        if validate_date(dob) and calculate_age(dob) >= 18:
            break
        if not validate_date(dob):
            print("Error: Invalid date format. Use dd/mm/yyyy.")
        elif calculate_age(dob) < 18:
            print("Error: Staff member must be at least 18 years old.")

    while True:
        ph_no = input("Enter phone number: ").strip()
        if ph_no.isdigit() and len(ph_no) == 10:
            break
        print("Error: Phone number must be a 10-digit number.")

    while True:
        addr = input("Enter address: ").strip()
        if addr:
            break
        print("Error: Address cannot be empty.")

    while True:
        do_join = input("Enter date of joining (dd/mm/yyyy): ").strip()
        if validate_date(do_join):
            dob_date = datetime.datetime.strptime(dob, "%d/%m/%Y")
            join_date = datetime.datetime.strptime(do_join, "%d/%m/%Y")
            if (join_date - dob_date).days >= 18 * 365:
                break
            else:
                print("Error: Date of joining must be at least 18 years after the date of birth.")
        else:
            print("Error: Invalid date format. Use dd/mm/yyyy.")

    while True:
        salary = input("Enter salary: ").strip()
        if salary.replace(".", "").isdigit() and float(salary) > 0:
            break
        print("Error: Salary must be a positive number.")

    staff_data[staff_id] = {
        "Full Name": fullname,
        "DOB": dob,
        "Phone Number": ph_no,
        "Address": addr,
        "Date of Joining": do_join,
        "Salary": salary
    }
    print("Staff added successfully!")

# Function to search for staff
def search_staff():
    criteria = input("Search by (1 for Staff ID, 2 for Phone Number): ").strip()
    if criteria == "1":
        staff_id = input("Enter Staff ID: ").strip()
        if staff_id in staff_data:
            print(staff_data[staff_id])
        else:
            print("Staff not found.")
    elif criteria == "2":
        ph_no = input("Enter Phone Number: ").strip()
        found = False
        for staff in staff_data.values():
            if staff["Phone Number"] == ph_no:
                print(staff)
                found = True
                break
        if not found:
            print("Staff not found.")
    else:
        print("Invalid search criteria.")

# Function to list all staff
def list_staff():
    if not staff_data:
        print("\nNo Staff Available.")
        return
    for staff_id, details in staff_data.items():
        print(f"\nStaff ID: {staff_id}")
        for key, value in details.items():
            print(f"{key}: {value}")

# Function to edit staff details
def edit_staff():
    staff_id = input("Enter staff ID to edit: ").strip()
    if staff_id in staff_data:
        print("Leave field blank to keep current value.")
        fullname = input(f"Enter full name ({staff_data[staff_id]['Full Name']}): ").strip()
        dob = input(f"Enter date of birth ({staff_data[staff_id]['DOB']}): ").strip()
        ph_no = input(f"Enter phone number ({staff_data[staff_id]['Phone Number']}): ").strip()
        addr = input(f"Enter address ({staff_data[staff_id]['Address']}): ").strip()
        do_join = input(f"Enter date of joining ({staff_data[staff_id]['Date of Joining']}): ").strip()
        salary = input(f"Enter salary ({staff_data[staff_id]['Salary']}): ").strip()

        if fullname and fullname.replace(" ", "").isalpha():
            staff_data[staff_id]['Full Name'] = fullname
        if dob and validate_date(dob) and calculate_age(dob) >= 18:
            staff_data[staff_id]['DOB'] = dob
        if ph_no and ph_no.isdigit() and len(ph_no) == 10:
            staff_data[staff_id]['Phone Number'] = ph_no
        if addr:
            staff_data[staff_id]['Address'] = addr
        if do_join and validate_date(do_join):
            dob_date = datetime.datetime.strptime(staff_data[staff_id]['DOB'], "%d/%m/%Y")
            join_date = datetime.datetime.strptime(do_join, "%d/%m/%Y")
            if (join_date - dob_date).days >= 18 * 365:
                staff_data[staff_id]['Date of Joining'] = do_join
        if salary and salary.replace(".", "").isdigit() and float(salary) > 0:
            staff_data[staff_id]['Salary'] = salary

        print("Staff details updated successfully!")
    else:
        print("Staff not found.")

# Function to delete a staff member
def delete_staff():
    staff_id = input("Enter staff ID to delete: ").strip()
    if staff_id in staff_data:
        del staff_data[staff_id]
        print("Staff deleted successfully!")
    else:
        print("Staff not found.")









# Function to add patient
# Function to validate date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%d/%m/%Y")
        return True
    except ValueError:
        return False


# Function to add a new patient
def add_patient():
    while True:
        patient_id = input("Enter patient ID: ").strip()
        if patient_id and patient_id not in patient_data:
            break
        print("Error: Patient ID already exists or is invalid. Please enter a unique ID.")

    while True:
        patient_name = input("Enter patient name: ").strip()
        if patient_name.replace(" ", "").isalpha():
            break
        print("Error: Name should only contain alphabetic characters and spaces.")

    while True:
        dob = input("Enter date of birth (dd/mm/yyyy): ").strip()
        if validate_date(dob):
            break
        print("Error: Invalid date format. Use dd/mm/yyyy.")

    while True:
        ph_no = input("Enter phone number: ").strip()
        if ph_no.isdigit() and len(ph_no) == 10:
            break
        print("Error: Phone number must be a 10-digit number.")

    while True:
        addr = input("Enter address: ").strip()
        if addr:
            break
        print("Error: Address cannot be empty.")

    while True:
        date_of_visit = input("Enter date of visit (dd/mm/yyyy): ").strip()
        if validate_date(date_of_visit):
            # Check that the visit date is after the date of birth
            dob_date = datetime.strptime(dob, "%d/%m/%Y")
            visit_date = datetime.strptime(date_of_visit, "%d/%m/%Y")
            if visit_date > dob_date:
                break
            else:
                print("Error: Date of visit must be after the date of birth.")
        else:
            print("Error: Invalid date format. Use dd/mm/yyyy.")

    while True:
        fees = input("Enter fees: ").strip()
        if fees.replace(".", "").isdigit() and float(fees) >= 0:
            break
        print("Error: Fees must be a non-negative number.")

    patient_data[patient_id] = {
        "Patient Name": patient_name,
        "DOB": dob,
        "Phone Number": ph_no,
        "Address": addr,
        "Date of Visit": date_of_visit,
        "Fees": fees
    }
    print("\nPatient added successfully!\n")


# Function to list all patients
def list_patients():
    if not patient_data:
        print("\nNo patients available.\n")
        return

    for patient_id, details in patient_data.items():
        print(f"\nPatient ID: {patient_id}")
        for key, value in details.items():
            print(f"{key}: {value}")
    print()


# Function to search for a patient
def search_patient():
    print("\nSearch by:")
    print("1. Patient ID")
    print("2. Phone Number")

    while True:
        try:
            criteria = int(input("Select an option (1 or 2): ").strip())
            if criteria == 1:
                patient_id = input("Enter patient ID: ").strip()
                if patient_id in patient_data:
                    print(f"\nPatient Details: {patient_data[patient_id]}\n")
                else:
                    print("\nPatient not found.\n")
                break
            elif criteria == 2:
                ph_no = input("Enter phone number: ").strip()
                found = False
                for patient in patient_data.values():
                    if patient["Phone Number"] == ph_no:
                        print(f"\nPatient Details: {patient}\n")
                        found = True
                        break
                if not found:
                    print("\nPatient not found.\n")
                break
            else:
                print("\nInvalid option. Please select either 1 or 2.")
        except ValueError:
            print("\nInvalid input. Please enter a number (1 or 2).")


# Function to edit patient details
def edit_patient():
    patient_id = input("Enter patient ID to edit: ").strip()
    if patient_id in patient_data:
        print("Leave a field blank to keep the current value.")

        patient_name = input(f"Enter patient name ({patient_data[patient_id]['Patient Name']}): ").strip()
        dob = input(f"Enter date of birth ({patient_data[patient_id]['DOB']}): ").strip()
        ph_no = input(f"Enter phone number ({patient_data[patient_id]['Phone Number']}): ").strip()
        addr = input(f"Enter address ({patient_data[patient_id]['Address']}): ").strip()
        date_of_visit = input(f"Enter date of visit ({patient_data[patient_id]['Date of Visit']}): ").strip()
        fees = input(f"Enter fees ({patient_data[patient_id]['Fees']}): ").strip()

        if patient_name:
            if patient_name.replace(" ", "").isalpha():
                patient_data[patient_id]['Patient Name'] = patient_name
            else:
                print("Warning: Invalid name. Keeping current value.")

        if dob:
            if validate_date(dob):
                patient_data[patient_id]['DOB'] = dob
            else:
                print("Warning: Invalid date format. Keeping current value.")

        if ph_no:
            if ph_no.isdigit() and len(ph_no) == 10:
                patient_data[patient_id]['Phone Number'] = ph_no
            else:
                print("Warning: Invalid phone number. Keeping current value.")

        if addr:
            patient_data[patient_id]['Address'] = addr

        if date_of_visit:
            if validate_date(date_of_visit):
                patient_data[patient_id]['Date of Visit'] = date_of_visit
            else:
                print("Warning: Invalid date format. Keeping current value.")

        if fees:
            if fees.replace(".", "").isdigit() and float(fees) >= 0:
                patient_data[patient_id]['Fees'] = fees
            else:
                print("Warning: Invalid fees. Keeping current value.")

        print("\nPatient details updated successfully!\n")
    else:
        print("\nPatient not found.\n")









# Function to add medicine
# Function to validate date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%d/%m/%Y")
        return True
    except ValueError:
        return False


# Function to validate price
def validate_price(price):
    try:
        price = float(price)
        if price >= 0:
            return True
        return False
    except ValueError:
        return False


# Function to add a new medicine
def add_medicine():
    while True:
        medicine_id = input("Enter medicine ID: ").strip()
        if medicine_id and medicine_id not in medicine_data:
            break
        print("Error: Medicine ID already exists or is invalid. Please enter a unique ID.")

    medicine_name = input("Enter medicine name: ").strip()
    manufacturer = input("Enter manufacturer: ").strip()

    while True:
        mfg_date = input("Enter manufacturing date (dd/mm/yyyy): ").strip()
        if validate_date(mfg_date):
            break
        print("Error: Invalid date format. Use dd/mm/yyyy.")

    while True:
        exp_date = input("Enter expiry date (dd/mm/yyyy): ").strip()
        if validate_date(exp_date):
            break
        print("Error: Invalid date format. Use dd/mm/yyyy.")

    while True:
        price = input("Enter price: ").strip()
        if validate_price(price):
            break
        print("Error: Invalid price. It must be a non-negative number.")

    medicine_data[medicine_id] = {
        "Medicine Name": medicine_name,
        "Manufacturer": manufacturer,
        "Manufacturing Date": mfg_date,
        "Expiry Date": exp_date,
        "Price": price
    }
    print("Medicine added successfully!")


# Function to list all medicines
def list_medicines():
    if not medicine_data:
        print("\nNo medicines available.\n")
        return

    for medicine_id, details in medicine_data.items():
        print(f"\nMedicine ID: {medicine_id}")
        for key, value in details.items():
            print(f"{key}: {value}")
    print()


# Function to search for a medicine
def search_medicine():
    print("\nSearch by:")
    print("1. Medicine ID")
    print("2. Medicine Name")

    while True:
        try:
            criteria = int(input("Select an option (1 or 2): ").strip())
            if criteria == 1:
                medicine_id = input("Enter medicine ID: ").strip()
                if medicine_id in medicine_data:
                    print(f"\nMedicine Details: {medicine_data[medicine_id]}\n")
                else:
                    print("\nMedicine not found.\n")
                break
            elif criteria == 2:
                medicine_name = input("Enter medicine name: ").strip()
                found = False
                for medicine in medicine_data.values():
                    if medicine["Medicine Name"].lower() == medicine_name.lower():
                        print(f"\nMedicine Details: {medicine}\n")
                        found = True
                        break
                if not found:
                    print("\nMedicine not found.\n")
                break
            else:
                print("\nInvalid option. Please select either 1 or 2.")
        except ValueError:
            print("\nInvalid input. Please enter a number (1 or 2).")


# Function to edit medicine details
def edit_medicine():
    medicine_id = input("Enter medicine ID to edit: ").strip()
    if medicine_id in medicine_data:
        print("Leave field blank to keep current value.")

        medicine_name = input(f"Enter medicine name ({medicine_data[medicine_id]['Medicine Name']}): ").strip()
        manufacturer = input(f"Enter manufacturer ({medicine_data[medicine_id]['Manufacturer']}): ").strip()
        mfg_date = input(f"Enter manufacturing date ({medicine_data[medicine_id]['Manufacturing Date']}): ").strip()
        exp_date = input(f"Enter expiry date ({medicine_data[medicine_id]['Expiry Date']}): ").strip()
        price = input(f"Enter price ({medicine_data[medicine_id]['Price']}): ").strip()

        if medicine_name:
            medicine_data[medicine_id]['Medicine Name'] = medicine_name
        if manufacturer:
            medicine_data[medicine_id]['Manufacturer'] = manufacturer
        if mfg_date and validate_date(mfg_date):
            medicine_data[medicine_id]['Manufacturing Date'] = mfg_date
        if exp_date and validate_date(exp_date):
            medicine_data[medicine_id]['Expiry Date'] = exp_date
        if price and validate_price(price):
            medicine_data[medicine_id]['Price'] = price

        print("Medicine details updated successfully!")
    else:
        print("Medicine not found.")


# Function to delete medicine
def delete_medicine():
    medicine_id = input("Enter medicine ID to delete: ").strip()
    if medicine_id in medicine_data:
        del medicine_data[medicine_id]
        print("Medicine deleted successfully!")
    else:
        print("Medicine not found.")


# Function to add lab test
# Function to validate non-empty input
def validate_input(field_name, value):
    if not value.strip():
        print(f"Error: {field_name} cannot be empty.")
        return False
    return True


# Function to add a new lab test
def add_lab_test():
    while True:
        test_code = input("Enter lab test code: ").strip()
        if validate_input("Test Code", test_code):
            break

    while True:
        test_name = input("Enter lab test name: ").strip()
        if validate_input("Test Name", test_name):
            break

    description = input("Enter test description: ").strip()

    # Adding the lab test to the list
    lab_tests_list.append({
        "Test Code": test_code,
        "Test Name": test_name,
        "Description": description
    })
    print("Lab test added successfully!")


# Function to list all lab tests
def list_lab_tests():
    if lab_tests_list:
        for test in lab_tests_list:
            print(f"Test Code: {test['Test Code']}")
            print(f"Test Name: {test['Test Name']}")
            print(f"Description: {test['Description']}")
            print()
    else:
        print("No lab tests available.")


# Function to search for a lab test
def search_lab_test():
    print("\nSearch by:")
    print("1. Test Code")
    print("2. Test Name")

    while True:
        try:
            criteria = int(input("Select an option (1 or 2): ").strip())
            if criteria == 1:
                test_code = input("Enter lab test code: ").strip()
                found = False
                for test in lab_tests_list:
                    if test["Test Code"] == test_code:
                        print(f"\nTest Found: {test}\n")
                        found = True
                        break
                if not found:
                    print("\nLab test not found.\n")
                break
            elif criteria == 2:
                test_name = input("Enter lab test name: ").strip()
                found = False
                for test in lab_tests_list:
                    if test["Test Name"].lower() == test_name.lower():
                        print(f"\nTest Found: {test}\n")
                        found = True
                        break
                if not found:
                    print("\nLab test not found.\n")
                break
            else:
                print("\nInvalid option. Please select either 1 or 2.")
        except ValueError:
            print("\nInvalid input. Please enter a number (1 or 2).")


# Function to edit a lab test
def edit_lab_test():
    test_code = input("Enter lab test code to edit: ").strip()
    found = False
    for test in lab_tests_list:
        if test["Test Code"] == test_code:
            found = True
            print("Leave field blank to keep current value.")
            test_name = input(f"Enter lab test name ({test['Test Name']}): ").strip()
            description = input(f"Enter test description ({test['Description']}): ").strip()

            if test_name:
                test["Test Name"] = test_name
            if description:
                test["Description"] = description

            print("Lab test details updated successfully!")
            break
    if not found:
        print("Lab test not found.")


# Function to delete a lab test
def delete_lab_test():
    test_code = input("Enter lab test code to delete: ").strip()
    found = False
    for test in lab_tests_list:
        if test["Test Code"] == test_code:
            lab_tests_list.remove(test)
            print("Lab test deleted successfully!")
            found = True
            break
    if not found:
        print("Lab test not found.")
# Run the program
main()
