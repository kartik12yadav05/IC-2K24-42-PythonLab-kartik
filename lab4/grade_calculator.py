# Grade calculation program

# initialize marks
marks = [0,0,0,0,0]

while True:
    # display menu options
    print("---------------------------------------")
    print("STUDENT GRADE CALCULATOR MENU")
    print("1. Enter marks of new student\n2. Grade of last entered student\n3. Exit")

    # input user choice
    choice = int(input("select option from the menu: "))
    print("---------------------------------------")

    # defining cases of the menu
    match choice:
        case 1:
            for i in range(5):
                marks[i] = float(input(f"marks[{i}]: "))

        case 2:
            total = 0
            for i in range(5):
                total = total + marks[i]

            print("Total marks: ", total)
            avg = total/5
            print("Average marks: ", avg)

            if(avg>= 90):
                print("Grade: A")
            elif(avg>=75 and avg<90):
                print("Grade: B")
            elif(avg>=60 and avg<75):
                print("Grade: C")
            elif(avg>=40 and avg<60):
                print("Grade: D")
            else:
                print("Grade: F")

        case 3:
            print("Thank You :)")
            break

        case _:
            print()

