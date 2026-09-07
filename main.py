#GROUP 10
# VICTORIA UNIVERSITY HOSTEL ROOM BOOKING AND FEES MANAGEMENT SYSTEM

import json
import os

# (a) Data setup:
# Stores The records of Registered students,Payment record and Room allocation
DATA_FILE = "hostel_data.json"
#creates a default hostel blocks with rooms,room capacity and students to be allocated
def create_default_hostel_blocks():

    return {
        "Block A": {
            "A101": {"capacity": 4, "students": []},
            "A102": {"capacity": 4, "students": []},
            "A103": {"capacity": 4, "students": []},
            "A104": {"capacity": 4, "students": []},
            "A105": {"capacity": 4, "students": []}
        },

        "Block B": {
            "B201": {"capacity": 4, "students": []},
            "B202": {"capacity": 4, "students": []},
            "B203": {"capacity": 4, "students": []},
            "B204": {"capacity": 4, "students": []},
            "B205": {"capacity": 4, "students": []}
        },



        

        "Block C": {
            "C301": {"capacity": 3, "students": []},
            "C302": {"capacity": 3, "students": []},
            "C303": {"capacity": 3, "students": []},
            "C304": {"capacity": 3, "students": []},
            "C305": {"capacity": 3, "students": []}
        }
    }

# DATA
hostel_blocks = create_default_hostel_blocks()
students = {}
# SAVE DATA
def save_data():
    data = {
        "students": students,
        "hostel_blocks": hostel_blocks
    }
    try:

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("\nData saved successfully.")

        return True

    except OSError:

        print("\nERROR: The system could not save the data.")

        return False

# LOAD DATA

def load_data():

    global students
    global hostel_blocks

    if not os.path.exists(DATA_FILE):

        print("\nNo previous data file found.")
        print("The system will start with empty records.")

        return

    try:

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        if not isinstance(data, dict):

            raise ValueError("Invalid data format.")

        if "students" not in data:

            raise ValueError("Student data is missing.")

        if "hostel_blocks" not in data:

            raise ValueError("Hostel data is missing.")

        if not isinstance(data["students"], dict):

            raise ValueError("Invalid student data.")

        if not isinstance(data["hostel_blocks"], dict):

            raise ValueError("Invalid hostel data.")

        students = data["students"]
        hostel_blocks = data["hostel_blocks"]

        print("\nPrevious data loaded successfully.")

    except (json.JSONDecodeError, ValueError, OSError):

        print("\nWARNING: The saved data file is damaged")
        print("or cannot be read.")

        print("The system will start with empty records.")

        students = {}

        hostel_blocks = create_default_hostel_blocks()

# Occupancy overview of the hostel blocks

def show_occupancy_overview():

    print("\n" + "=" * 60)
    print("           HOSTEL OCCUPANCY OVERVIEW")
    print("=" * 60)

    total_capacity = 0
    total_occupied = 0

    for block_name, rooms in hostel_blocks.items():

        block_capacity = 0
        block_occupied = 0

        for room in rooms.values():

            capacity = room["capacity"]
            occupied = len(room["students"])

            block_capacity += capacity
            block_occupied += occupied

        block_available = block_capacity - block_occupied

        print(
            f"{block_name}: "
            f"Occupied = {block_occupied}, "
            f"Capacity = {block_capacity}, "
            f"Available = {block_available}"
        )

        total_capacity += block_capacity
        total_occupied += block_occupied

    total_available = total_capacity - total_occupied

    print("-" * 60)

    print(
        f"OVERALL: "
        f"Occupied = {total_occupied}, "
        f"Capacity = {total_capacity}, "
        f"Available = {total_available}"
    )

    print("=" * 60)

# (b) Student Registration and Hostel Room Allocation

def register_student():

    print("\n" + "=" * 60)
    print("                STUDENT REGISTRATION")
    print("=" * 60)

    # Registration number
    while True:

        registration_number = input(
            "Enter student registration number: "
        ).strip()

        if registration_number == "":

            print("ERROR: Registration number cannot be empty.")

            continue

        if registration_number in students:

            print(
                "ERROR: A student with this registration "
                "number already exists."
            )

            continue

        break

    # Name
    while True:

        name = input(
            "Enter student name: "
        ).strip()

        if name == "":

            print("ERROR: Student name cannot be empty.")

            continue

        if not any(character.isalpha() for character in name):

            print("ERROR: Please enter a valid name.")

            continue

        break

    # Course
    while True:

        course = input(
            "Enter course: "
        ).strip()

        if course == "":

            print("ERROR: Course cannot be empty.")

            continue

        break

    # Year
    while True:

        year = input(
            "Enter year of study: "
        ).strip()

        if year == "":

            print("ERROR: Year of study cannot be empty.")

            continue

        if not year.isdigit():

            print(
                "ERROR: Year of study must be a number."
            )

            continue

        if int(year) <= 0:

            print(
                "ERROR: Year of study must be greater than zero."
            )

            continue

        break

    # Phone
    while True:

        phone = input(
            "Enter phone number: "
        ).strip()

        if phone == "":

            print("ERROR: Phone number cannot be empty.")

            continue

        if not phone.isdigit():

            print(
                "ERROR: Phone number should contain digits only."
            )

            continue

        if len(phone) < 9 or len(phone) > 15:

            print(
                "ERROR: Enter a valid phone number."
            )

            continue

        break

    # Record Hostel fee to be paid by students
    while True:

        fee_input = input(
            "Enter total hostel fee: "
        ).strip()

        try:

            total_fee = float(fee_input)

            if total_fee < 0:

                print(
                    "ERROR: Hostel fee cannot be negative."
                )

                continue

            break

        except ValueError:

            print(
                "ERROR: Please enter a valid numeric amount."
            )

    students[registration_number] = {

        "name": name,
        "course": course,
        "year": year,
        "phone": phone,
        "block": None,
        "room": None,
        "total_fee": total_fee,
        "payments": []

    }

    save_data()

    print("\nSTUDENT REGISTERED SUCCESSFULLY!")

    print("-" * 60)

    print(f"Registration Number: {registration_number}")
    print(f"Name:                {name}")
    print(f"Course:              {course}")
    print(f"Year of Study:       {year}")
    print(f"Phone:               {phone}")
    print(f"Total Hostel Fee:    {total_fee:,.2f}")
    print(f"Outstanding Balance: {total_fee:,.2f}")

    print("-" * 60)

# Room allocation for student who have registered

def allocate_room():

    print("\n" + "=" * 60)
    print("                  ROOM ALLOCATION")
    print("=" * 60)

    if not students:

        print("There are no registered students.")
        print("Please register a student first.")

        return

    # Validate registration number of students
    while True:

        registration_number = input(
            "Enter student registration number: "
        ).strip()

        if registration_number == "":

            print(
                "ERROR: Registration number cannot be empty."
            )

            continue

        if registration_number not in students:

            print(
                "ERROR: Student not found."
            )

            continue

        break

    student = students[registration_number]

    # Check existing allocation of the rooms
    if student["room"] is not None:

        print(
            f"This student is already allocated to "
            f"{student['block']} - {student['room']}."
        )

        return

    # Validate room number
    while True:

        room_number = input(
            "Enter room number: "
        ).strip().upper()

        if room_number == "":

            print(
                "ERROR: Room number cannot be empty."
            )

            continue

        selected_block = None
        selected_room = None

        for block_name, rooms in hostel_blocks.items():

            if room_number in rooms:

                selected_block = block_name
                selected_room = rooms[room_number]

                break

        if selected_room is None:

            print(
                "ERROR: Room not found."
            )

            print(
                "Please enter a valid room number."
            )

            continue

        break

    capacity = selected_room["capacity"]
    occupied = len(selected_room["students"])
    available = capacity - occupied

    print("\nRoom Information")
    print("-" * 60)

    print(f"Block:              {selected_block}")
    print(f"Room:               {room_number}")
    print(f"Capacity:           {capacity}")
    print(f"Currently Occupied: {occupied}")
    print(f"Available Spaces:   {available}")

    print("-" * 60)

    # Check capacity of the hostel room for allocation
    if occupied >= capacity:

        print("\nROOM ALLOCATION REJECTED!")

        print(
            f"{room_number} is already full."
        )

        print(
            f"It has {occupied} out of {capacity} students."
        )

        return

    # Extra safety check
    if registration_number in selected_room["students"]:

        print(
            "ERROR: This student is already recorded "
            "in this room."
        )

        return

    selected_room["students"].append(
        registration_number
    )

    student["block"] = selected_block
    student["room"] = room_number

    save_data()

    print("\nROOM ALLOCATION SUCCESSFUL!")

    print("-" * 60)

    print(f"Student:             {student['name']}")
    print(f"Registration Number: {registration_number}")
    print(f"Block:               {selected_block}")
    print(f"Room:                {room_number}")

    print(
        f"Remaining spaces:    "
        f"{capacity - len(selected_room['students'])}"
    )

    print("-" * 60)

# Calculate balance from total fees of the hostel

def calculate_balance(student):

    total_paid = sum(student["payments"])

    balance = student["total_fee"] - total_paid

    return total_paid, balance

# (c) Record Payment for registered students

def record_payment():

    print("\n" + "=" * 60)
    print("                  FEE PAYMENT")
    print("=" * 60)

    if not students:

        print("There are no registered students.")
        print("Please register a student first.")

        return

    while True:

        registration_number = input(
            "Enter student registration number: "
        ).strip()

        if registration_number == "":

            print(
                "ERROR: Registration number cannot be empty."
            )

            continue

        if registration_number not in students:

            print(
                "ERROR: Student not found."
            )

            continue

        break

    student = students[registration_number]

    total_paid, balance = calculate_balance(student)

    print("\nStudent Fee Information")

    print("-" * 60)

    print(f"Student:             {student['name']}")
    print(f"Registration Number: {registration_number}")
    print(f"Total Hostel Fee:    {student['total_fee']:,.2f}")
    print(f"Total Paid:          {total_paid:,.2f}")
    print(f"Outstanding Balance: {balance:,.2f}")

    print("-" * 60)

    if balance <= 0:

        print(
            "This student's hostel fees are fully paid."
        )

        return

    while True:

        payment_input = input(
            "Enter payment amount: "
        ).strip()
        try:
            payment = float(payment_input)
            if payment <= 0:
                print(
                    "ERROR: Payment must be greater than zero."
                )
                continue
            if payment > balance:
                print(
                    f"ERROR: Payment cannot be greater than "
                    f"the outstanding balance of "
                    f"{balance:,.2f}."
                )
                continue
            break
        except ValueError:

            print(
                "ERROR: Please enter a valid numeric amount."
            )

    student["payments"].append(payment)

    total_paid, balance = calculate_balance(student)

    save_data()

    print("\nPAYMENT RECORDED SUCCESSFULLY!")

    print("-" * 60)
    print(f"Payment Made:        {payment:,.2f}")
    print(f"Total Paid:          {total_paid:,.2f}")
    print(f"Outstanding Balance: {balance:,.2f}")
    if balance == 0:
        print("Payment Status:      FULLY PAID")
    else:
        print("Payment Status:      OUTSTANDING")
    print("-" * 60)
# (d)Search students by their Registration number or Name
def search_student():
    print("\n" + "=" * 60)
    print("                  SEARCH STUDENT")
    print("=" * 60)

    if not students:
        print("There are no registered students.")
        return
    search_value = input(
        "Enter student name or registration number: "
    ).strip()

    if search_value == "":
        print(
            "ERROR: Search value cannot be empty."
        )
        return

    found_students = []

    if search_value in students:

        found_students.append(
            (
                search_value,
                students[search_value]
            )
        )

    else:
        search_name = search_value.lower()

        for registration_number, student in students.items():

            if search_name in student["name"].lower():

                found_students.append(
                    (
                        registration_number,
                        student
                    )
                )

    if not found_students:
        print("\nNo student found.")

        return
    print("\nSTUDENT SEARCH RESULTS")
    print("=" * 60)

    for registration_number, student in found_students:

        total_paid, balance = calculate_balance(student)

        print(
            f"\nRegistration Number: "
            f"{registration_number}"
        )

        print(
            f"Name:                "
            f"{student['name']}"
        )

        print(
            f"Course:              "
            f"{student['course']}"
        )

        print(
            f"Year of Study:       "
            f"{student['year']}"
        )

        print(
            f"Phone:               "
            f"{student['phone']}"
        )

        if student["block"] is not None:

            print(
                f"Hostel Block:        "
                f"{student['block']}"
            )

            print(
                f"Room:                "
                f"{student['room']}"
            )

        else:

            print(
                "Hostel Block:        Not allocated"
            )

            print(
                "Room:                Not allocated"
            )

        print(
            f"Total Hostel Fee:    "
            f"{student['total_fee']:,.2f}"
        )

        print(
            f"Total Paid:          "
            f"{total_paid:,.2f}"
        )

        print(
            f"Outstanding Balance: "
            f"{balance:,.2f}"
        )

        if balance <= 0:

            print(
                "Payment Status:      FULLY PAID"
            )

        else:
            print(
                "Payment Status:      OUTSTANDING"
            )
        print("-" * 60)
# Full Hostel Occupancy Report
def occupancy_report():
    print("\n" + "=" * 70)
    print("                  FULL OCCUPANCY REPORT")
    print("=" * 70)
    total_capacity = 0
    total_occupied = 0

    for block_name, rooms in hostel_blocks.items():

        print(f"\n{block_name}")
        print("-" * 70)

        block_capacity = 0
        block_occupied = 0

        for room_number, room in rooms.items():

            capacity = room["capacity"]
            occupied = len(room["students"])
            available = capacity - occupied

            block_capacity += capacity
            block_occupied += occupied

            print(
                f"\nRoom: {room_number}"
            )

            print(
                f"Capacity: {capacity} | "
                f"Occupied: {occupied} | "
                f"Available: {available}"
            )

            if occupied == 0:

                print("Students: None")

            else:

                print("Students:")

                for registration_number in room["students"]:

                    student = students.get(
                        registration_number
                    )

                    if student:

                        print(
                            f"  - {student['name']} "
                            f"({registration_number})"
                        )

        block_available = (
            block_capacity - block_occupied
        )

        print("-" * 70)

        print(
            f"{block_name} SUMMARY: "
            f"Occupied = {block_occupied}, "
            f"Capacity = {block_capacity}, "
            f"Available = {block_available}"
        )
        total_capacity += block_capacity
        total_occupied += block_occupied

    total_available = (
        total_capacity - total_occupied
    )
    print("\n" + "=" * 70)
    print("OVERALL HOSTEL SUMMARY")
    print("-" * 70)

    print(f"Total Capacity:  {total_capacity}")
    print(f"Total Occupied:  {total_occupied}")
    print(f"Total Available: {total_available}")

    print("=" * 70)

# Fee student defulter Report
def fee_defaulters_report():

    print("\n" + "=" * 70)
    print("                  FEE DEFAULTERS REPORT")
    print("=" * 70)

    if not students:

        print("There are no registered students.")

        return

    while True:

        threshold_input = input(
            "Enter outstanding balance threshold: "
        ).strip()

        try:

            threshold = float(threshold_input)

            if threshold < 0:

                print(
                    "ERROR: Threshold cannot be negative."
                )

                continue

            break

        except ValueError:

            print(
                "ERROR: Please enter a valid numeric amount."
            )

    defaulters = []

    for registration_number, student in students.items():

        total_paid, balance = calculate_balance(student)

        if balance > threshold:

            defaulters.append(
                (
                    registration_number,
                    student,
                    total_paid,
                    balance
                )
            )

    if not defaulters:

        print(
            f"\nNo students have an outstanding balance "
            f"above {threshold:,.2f}."
        )

        return

    print(
        f"\nSTUDENTS WITH BALANCE ABOVE "
        f"{threshold:,.2f}"
    )

    print("=" * 70)

    for registration_number, student, total_paid, balance in defaulters:

        print(
            f"\nRegistration Number: "
            f"{registration_number}"
        )

        print(
            f"Name:                "
            f"{student['name']}"
        )

        print(
            f"Course:              "
            f"{student['course']}"
        )

        print(
            f"Phone:               "
            f"{student['phone']}"
        )

        if student["block"] is not None:

            print(
                f"Hostel Block:        "
                f"{student['block']}"
            )

            print(
                f"Room:                "
                f"{student['room']}"
            )

        else:

            print(
                "Hostel Block:        Not allocated"
            )

            print(
                "Room:                Not allocated"
            )

        print(
            f"Total Hostel Fee:    "
            f"{student['total_fee']:,.2f}"
        )

        print(
            f"Total Paid:          "
            f"{total_paid:,.2f}"
        )

        print(
            f"Outstanding Balance: "
            f"{balance:,.2f}"
        )

        print("-" * 70)

    print(
        f"Total Number of Defaulters: "
        f"{len(defaulters)}"
    )

    print("=" * 70)

# View all resgistered students

def view_all_students():

    print("\n" + "=" * 70)
    print("                    ALL REGISTERED STUDENTS")
    print("=" * 70)

    if not students:

        print("No students have been registered.")

        print("=" * 70)

        return

    print(
        f"Total Registered Students: {len(students)}"
    )

    print("=" * 70)

    for registration_number, student in students.items():

        total_paid, balance = calculate_balance(student)

        print(
            f"\nRegistration Number: "
            f"{registration_number}"
        )

        print(
            f"Name:                "
            f"{student['name']}"
        )

        print(
            f"Course:              "
            f"{student['course']}"
        )

        print(
            f"Year:                "
            f"{student['year']}"
        )

        print(
            f"Phone:               "
            f"{student['phone']}"
        )

        if student["block"] is not None:

            print(
                f"Room:                "
                f"{student['block']} - "
                f"{student['room']}"
            )

        else:

            print(
                "Room:                Not allocated"
            )

        print(
            f"Total Fee:           "
            f"{student['total_fee']:,.2f}"
        )

        print(
            f"Total Paid:          "
            f"{total_paid:,.2f}"
        )

        print(
            f"Outstanding Balance: "
            f"{balance:,.2f}"
        )

        if balance <= 0:

            print(
                "Payment Status:      FULLY PAID"
            )

        else:

            print(
                "Payment Status:      OUTSTANDING"
            )

        print("-" * 70)

    print("=" * 70)

# (f) Main Menu of the Hostel Management System
def main():

    load_data()

    show_occupancy_overview()

    while True:

        print("\n" + "=" * 65)

        print(
            "       HOSTEL ROOM BOOKING AND FEES MANAGEMENT SYSTEM"
        )

        print("=" * 65)

        print("1. Register Student")
        print("2. Allocate Room")
        print("3. Record Fee Payment")
        print("4. Search Student")
        print("5. View Full Occupancy Report")
        print("6. View Fee Defaulters")
        print("7. View All Students")
        print("8. Save Data")
        print("9. Exit")

        print("=" * 65)

        choice = input(
            "Enter your choice (1-9): "
        ).strip()

        if choice == "1":

            register_student()

        elif choice == "2":

            allocate_room()

        elif choice == "3":

            record_payment()

        elif choice == "4":

            search_student()

        elif choice == "5":

            occupancy_report()

        elif choice == "6":

            fee_defaulters_report()

        elif choice == "7":

            view_all_students()

        elif choice == "8":

            save_data()

        elif choice == "9":

            print("\nSaving data before exit...")

            save_data()

            print("\n" + "=" * 60)

            print(
                "Thank you for using the "
                "Hostel Management System."
            )

            print("=" * 60)

            break

        else:

            print("\nERROR: Invalid menu choice.")

            print(
                "Please enter a number from 1 to 9."
            )

# Program start
if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\n\nProgram interrupted by user.")
        print("Saving data before closing...")

        save_data()

        print("Program closed safely.")

    except Exception as error:

        print("\nAn unexpected error occurred.")
        print("The program has been stopped safely.")

        print(
            "Error details:",
            error
        )