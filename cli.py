from main import Habit

def cli():

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
        return
    
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
            return 

        try:
            habit_cost = int(input("Enter the cost of of your habit in euro. If there are no cost enter 0:"))
        except ValueError:
            print("Please enter a number.")
            return

        habit = Habit(habit_name,habit_period,habit_cost)
        habit.add_habit()
    
    elif number == 2:
        habit_name = str.lower(input("Enter a habit name you want to delete:"))
      
        try:
            Habit.del_habit(habit_name,habit_name)
        except NameError:
            return
        

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
            return

        if number_edit == 1:
            
            old_habit_name = str.lower(input("Enter the old habit name:"))

            new_habit_name = str.lower(input("Enter the new habit name:"))

            Habit.edit_habit_name(old_habit_name,old_habit_name,new_habit_name)    
                
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
                return
            
            Habit.edit_habit_period(habit_name,habit_name,new_habit_period)

        if number_edit == 3:
            
            habit_name = str.lower(input("Enter the habit name:"))
                
            try:
                new_habit_cost = int(input("Enter the new habit cost in Euro:"))
            except ValueError:
                print("Please enter a number.")
                return
            
            Habit.edit_habit_cost(habit_name,habit_name,new_habit_cost)

        if number_edit == 4:
            cli()


    elif number == 4:

        habit_name_check = str.lower(input("Enter a habit name you want to check:"))

        Habit.check_off(habit_name_check,habit_name_check)


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
            return
        print("")

        if number_analyses == 1:
            Habit.display_all_habits(number_analyses)
            print("")
        elif number_analyses == 2:
            Habit.display_all_habits_periodicity(number_analyses)
            print("")
        elif number_analyses == 3:
            Habit.display_all_habits_longest_current_streak(number_analyses)
            print("")
        elif number_analyses == 4:
            Habit.display_all_habits_longest_all_time_streak(number_analyses)
            print("")
        elif number_analyses == 5:
            Habit.display_all_habits_cost(number_analyses)
            print("")
        elif number_analyses == 6:
            Habit.display_all_habits_money_saved(number_analyses)
            print("")
        elif number_analyses == 7:
            cli()
        else:
            print("Invaild input. Try again.")

           
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


    elif number == 7:
        return


    else:
        print("Invaild input. Try again.")
    
if __name__ == "__main__":
    cli()


