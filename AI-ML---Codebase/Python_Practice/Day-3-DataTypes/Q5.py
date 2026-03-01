students = {}

while True:
    print("\n----- MENU -----")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students")
    print("E - Exit")


    choice = input("Enter your choice (A/B/C/D/E): ").upper()

    if choice == "A":
        name = input("Enter Name : ")
        marks = int(input("Enter Marks :"))
        students[name] = marks
        print("Student Added Successfully")

    elif choice == "B":
        name = input("Enter Student name to update :")
        if name in students:
            new_marks = int(input("Enter New Marks : "))
            students[name] = new_marks
            print("Update Marks Successfully")
        else:
            print("Student Not Found")

    elif choice =="C":
        name = input("Name Of Student: ")
        if name in students:
            print("marks:", students[name])
        else:
            print("student not found")

    elif choice == "D":
        if len(students) == 0:
            print("NO STUDENT IN RECORD")
        else:
            print("\nStudents Records:")
            for name,marks in students.items():
                print(name , ":" , marks)

    elif choice == "E":
        print("Exiting Program....")
        break

    else:
        print("Invalid Choice ! Please Try Again")
