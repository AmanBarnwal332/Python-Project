students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
while True:
    print("\n1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists!")
        else:
            marks = []

            for i in range(3):
                mark = float(input("Enter marks: "))
                marks.append(mark)

            students[name] = marks
            print("Student added successfully!")

    elif choice == "2":
        for name, marks in students.items():
            average = sum(marks) / len(marks)

            if average >= 85:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "F"

            print(name, round(average, 2), grade)

    elif choice == "3":
        highest_average = -1
        topper = ""

        for name, marks in students.items():
            average = sum(marks) / len(marks)

            if average > highest_average:
                highest_average = average
                topper = name

        print("Topper:", topper)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
