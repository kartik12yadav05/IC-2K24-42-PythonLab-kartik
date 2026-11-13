# Menu driven program for multiple applications

while True:

    print("-----------------------------------------------")
    print("Select the application you want to run:")
    print("1. ATM Simulation\n2. Student Grade Calculator\n3. Number Guessing Game\n4. Exit")
    print("-----------------------------------------------")

    choice = int(input("Enter your choice (1-4): "))
    print("-----------------------------------------------")



    match choice:
        case 1:
            import ATM_simulation
            
        case 2:
            import grade_calculator
            
        case 3:
            import num_guessing_game
            
        case 4:
            print("Exiting the program.")
            print("Thank You :)")
            break
        case _:
            print("Invalid choice. Select from 1 to 4.")