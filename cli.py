from main import Habit

def cli():
    # Main menu
    print("")
    print("Main menu:")
    print("1. Create")
    print("2. Delete")
    print("3. Edit")
    print("4. Checkoff")
    print("5. Analyse")
    print("6. Help")
    print("7. Exit" )
    print("")

    try: 
        number = int(input("Enter a number:"))
    except ValueError:
        print("Please enter a number.")
        cli()

    # Add a habit to the json file
    if number == 1:
        habit_name = str.lower(input("Enter a habit name:"))

        try:
            habit_period = int(input("Enter the period you want check your habit. Enter 1 for daily and 7 for weekly:"))
            if habit_period == 1 or habit_period == 7:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Please enter the number 1 or 7.")
            cli()

        try:
            habit_cost = int(input("Enter the cost of of your habit in euro. If there are no cost enter 0:"))
        except ValueError:
            print("Please enter a number.")
            cli()

        habit = Habit(habit_name,habit_period,habit_cost)
        habit.add_habit()
        cli()

    # Delete a habit from the json file
    elif number == 2:
        habit_name = str.lower(input("Enter a habit name you want to delete:"))
      
        try:
            Habit.del_habit(habit_name,habit_name)
        except NameError:
            cli()
        
    # Edit a habit from the json file
    elif number == 3:
        print("")
        print("Edit menu:")
        print("1. Name")
        print("2. Period")
        print("3. Cost")
        print("4. Return to main menu")
        print("")

        try: 
            number_edit = int(input("Enter a number:"))
        except ValueError:
            print("Please enter a number.")
           
            cli()

        # Edit the name
        if number_edit == 1:
            
            old_habit_name = str.lower(input("Enter the old habit name:"))
            new_habit_name = str.lower(input("Enter the new habit name:"))
            Habit.edit_habit_name(old_habit_name,old_habit_name,new_habit_name)  
            cli()  

        # Edit the period     
        if number_edit == 2:
            
            habit_name = str.lower(input("Enter the habit name:"))
                
            try:
                new_habit_period = int(input("Enter the new habit period. Enter 1 for daily and 7 for weakly:"))
                if new_habit_period == 1 or new_habit_period == 7:
                    pass
                else:
                    raise ValueError
            except ValueError:
                print("Please enter the number 1 or 7.")
                cli()
            
            Habit.edit_habit_period(habit_name,habit_name,new_habit_period)
            cli()

        # Edit the cost
        if number_edit == 3:
            
            habit_name = str.lower(input("Enter the habit name:"))
                
            try:
                new_habit_cost = int(input("Enter the new habit cost in Euro:"))
            except ValueError:
                print("Please enter a number.")
                cli()
            
            Habit.edit_habit_cost(habit_name,habit_name,new_habit_cost)
            cli()

        # Go back to the main menu
        if number_edit == 4:
            cli()

    # Check off a habit
    elif number == 4:

        habit_name_check = str.lower(input("Enter a habit name you want to check:"))
        Habit.check_off(habit_name_check,habit_name_check)
        cli()

    # Display all the habits in a table
    elif number == 5:
        print("")
        print("Analyses menu:")
        print("1. All")
        print("2. Period")
        print("3. Longest current streak")
        print("4. Longest all time streak")
        print("5. Cost")
        print("6. Money saved")
        print("7. Return to main menu")
        print("")

        try: 
            number_analyses = int(input("Enter a number:"))
        except ValueError:
            print("Please enter a number.")
            cli()
        print("")

        # Display All
        if number_analyses == 1:
            Habit.display_all_habits(number_analyses)
            print("")
            cli()
        # Sorted by periodicity
        elif number_analyses == 2:
            Habit.display_all_habits_periodicity(number_analyses)
            print("")
            cli()
        # Sorted by longest current streak
        elif number_analyses == 3:
            Habit.display_all_habits_longest_current_streak(number_analyses)
            print("")
            cli()
        # Sorted by longest all time streak
        elif number_analyses == 4:
            Habit.display_all_habits_longest_all_time_streak(number_analyses)
            print("")
            cli()
        # Sorted by cost
        elif number_analyses == 5:
            Habit.display_all_habits_cost(number_analyses)
            print("")
        # Sorted by Money saved
        elif number_analyses == 6:
            Habit.display_all_habits_money_saved(number_analyses)
            print("")
            cli()
        # Return to main menu
        elif number_analyses == 7:
            cli()
        else:
            print("Invaild input. Try again.")
            cli()

    # Explanation of the functions
    elif number == 6:
        print("")
        print("Here is the explenation of every function you have in the main menu:")
        print("1. Create a habit using where you can choose the name, period (daily or weekly) and the cost of the habit.")
        print("2. Delete a habit you have formaly created or that ones that have been created for you.")
        print("3. Change a habits name, period or cost.")
        print("4. Check off an habit and increase your streak.")
        print("5. Display your habits in a table, you can also sort them by multiple parameters.")
        print("6. Get help if you do not understand the functions.")
        print("7. Exit the habit tracker.")
        print("")
        cli()

    # Exit the habit tracker
    elif number == 7:
        cli()


    else:
        print("Invaild input. Try again.")
        cli()
    
if __name__ == "__main__":
    cli()


