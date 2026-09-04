    HOSTEL ROOM BOOKING AND FEES
    MANAGEMENT SYSTEM

    Project README / System Overview

     Introduction

    The Hostel Room Booking and Fees Management System is a console-based Python application developed to help a hostel warden manage student accommodation and hostel fees.
    It replaces a paper-based hostel ledger with a computerized system for registering students, allocating rooms, recording fee payments,searching records,monitoring occupancy,identifying fee defaulters,and saving records for use across multiple program runs.

     Main Objectives

      Register new hostel students.
      Allocate students to available hostel rooms.
      Prevent allocation to full rooms.
      Record full and partial hostel fee payments.
      Calculate outstanding student balances.
      Search students by name or registration number.
      Display hostel room occupancy information.
      Identify fee defaulters above a specified threshold.
      Save records to a file for future use.
      Automatically load previously saved records.
      Provide a simple menu-driven interface for a hostel warden.
      Technologies Used
      Programming Language: Python
      Data Storage: JSON file
      Interface: Console / Command Line
      Development Environment: PyCharm
      Version Control: Git and GitHub


      Hostel Structure

     Hostel Block	Rooms	Capacity per Room
     Block A	A101 – A105	4 students
     Block B	B201 – B205	4 students
     Block C	C301 – C305	3 students
     
     The total hostel capacity is 55 students.
     System Features
     Student Registration
     Registration number, name, course, year of study, phone number, and total hostel fee are recorded. Duplicate registration numbers are prevented.
     Room Allocation
     The system checks that the student and room exist, verifies that the student has no previous allocation, checks room capacity, rejects full rooms, and updates occupancy.
     Fee Management
     The system records total fees, multiple payments, outstanding balance, and payment status. Invalid and excessive payments are rejected.
     Student Search
     Students can be searched by registration number or name.
     Occupancy Report
     Shows blocks, rooms, capacity, occupied spaces, available spaces, assigned students, and overall occupancy.
     Fee Defaulters Report
     Displays students whose outstanding balance is greater than a user-specified threshold.
     Data Persistence
     Loads saved records at startup, saves after important operations and before exit, and handles missing or damaged JSON files.

    Main Menu

    1. Register Student
       2. Allocate Room
       3. Record Fee Payment
       4. Search Student
       5. View Full Occupancy Report
       6. View Fee Defaulters
       7. View All Students
       8. Save Data
       9. Exit
       The menu continues running until the user selects option 9, Exit.
    Input Validation

     Empty or duplicate registration numbers are rejected.
     Empty or invalid student names are rejected.
     Invalid year-of-study values are rejected.
     Invalid phone numbers are rejected.
     Negative hostel fees are rejected.
     Invalid payment amounts are rejected.
     Payments greater than the outstanding balance are rejected.
     Invalid room numbers are rejected.
     Invalid menu choices are rejected.
     Full rooms cannot receive additional students.

    Data Storage

    The application uses a JSON file for consistent storage:
    hostel_data.json
    This keeps student records, room allocations, and payment information available after the program is closed and restarted.
     Project Files
    File	Purpose
    main.py	Main Python application and system functions.
    hostel_data.json	Stores student and hostel records.
    README.md	Project information, features, operation, and structure.

    How to Run the System

    Make sure Python is installed.
    Open the HostelRoomBookingSystem folder in PyCharm or Visual Studio Code.
    Run main.py.
    Use the displayed menu by entering a number from 1 to 9.
     Workflow
    Start Program → Load Saved Records → Display Occupancy Overview → Display Main Menu → Register Student → Allocate Room → Record Fee Payment → Search / View Reports → Save Data → Exit
     Testing
    The system was tested to confirm that the major functions work correctly.
    Student registration
    Duplicate registration
    Room allocation
    Allocation to a full room
    Invalid room numbers
    Partial and multiple fee payments
    Full fee payment
    Excessive payment rejection
    Student search
    Occupancy reporting
    Fee defaulters reporting
    Viewing all students
    Saving and loading data
    Invalid menu choices
    Exit and automatic saving
    All major functions were confirmed to be working correctly during testing.

    Benefits of the System

    Reduces dependence on paper records.
    Makes student records easier to find.
    Helps monitor room occupancy.
    Prevents over-allocation of rooms.
    Makes fee tracking easier.
    Quickly identifies fee defaulters.
    Reduces calculation errors.
    Keeps records available between program sessions.
    Provides a simple interface for a hostel warden.

    Limitations

    The current version is console-based.
    Data is stored in a local JSON file.
    There is no graphical user interface.
    There is no centralized database server.
    There are no multiple user accounts.
    There is no online fee payment.
    There are no automated SMS or email notifications.

    Conclusion

    The Hostel Room Booking and Fees Management System provides a practical computerized solution for managing hostel accommodation and student fees.
    The system successfully implements student registration, room allocation, capacity checking, fee management, searching, reporting, validation, and persistent data storage. 
    It demonstrates Python concepts including functions, dictionaries, lists, loops, conditional statements, exception handling, file handling, JSON storage, and menu-driven programming.
