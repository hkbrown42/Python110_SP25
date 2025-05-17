# ------------------------------------------------------------------------------------------ #
# Title: Working with dictionaries and files
# Desc: Shows how to work with dictionaries and files when using a table of data
# Change Log:
#   Hannah Brown, 5/16/2025, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the data constants
FILE_NAME: str = "MyLabData.csv"
MENU: str = """
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
------------------------------------------------
"""

# Define the program's data
student_first_name: str = ""
student_last_name: str = ""
student_gpa: float = 0.0
message: str = ""
menu_choice: str = ""
student_data: dict = {}
students: list = []
file_data: str = ""
file = None

# When the program starts, read the file data into a list of dictionary rows
# Extract the data from the file
file = open(FILE_NAME, 'r')
for row in file.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = {"FirstName": student_data[0],
                    "LastName": student_data[1],
                    "GPA": float(student_data[2].strip())}
    # Load it into the collection
    students.append(student_data)
file.close()

# Repeat the following tasks
while True:
    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()

    # Display the table's current data
    if menu_choice == "1":
        print("-"*50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade."
            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-"*50)
        continue

    # Add data to the table
    elif menu_choice == "2":
        student_first_name = input("What is the student's first name? ")
        student_last_name = input("What is the student's last name? ")
        student_gpa = float(input("What is the student's GPA? "))

        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "GPA": student_gpa}
        students.append(student_data)
        continue
    
    # Save the data to the file
    elif menu_choice == "3":
        file = open(FILE_NAME, 'w')
        for student in students:
            file.write(f'{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n')
        file.close()
        print("Data saved!")
        continue
        
    # Exit the program
    else:
        break






















