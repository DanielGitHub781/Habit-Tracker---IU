import datetime
from datetime import datetime, timedelta
import json
import pandas as pd


class Habit:

    # Base Functions

    def __init__(self, name: str, period: int, cost: int):

        self.name = name
        self.period = period
        self.streak_length = 0
        self.longest_streak = 0
        self.cost_in_euro = cost
        self.money_saved_in_euro = 0
        self.start_date = []
        self.last_checked = []



    def add_habit(self):
        # Definition of a Habit
        data = {
            "Name": self.name,
            "Period in days": self.period,
            "Current streak length": self.streak_length,
            "Longest streak": self.longest_streak,
            "Cost in euro": self.cost_in_euro,
            "Money saved in euro": self.money_saved_in_euro,
            "Start date": datetime.now().date().isoformat(),
            "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
         }

        try:
            with open("habit_data.json", "r") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        # Check if there are duplicates in the file and stop execution if there are duplicates
        for duplicates in data_list:
            if duplicates.get("Name") == self.name:
                print("Please enter a new habit name that does not already exist.")
                return  
        # Append the habit to the json file
        data_list.append(data)

        print("You successfully created a habit") 

        with open("habit_data.json", "w") as file:
            json.dump(data_list, file, indent=8, default=str)
    


    def del_habit(self, del_habit_name):

        with open("habit_data.json", "r") as file:
            data = json.load(file)
        # Check if the habit that should be deleted is in the file
        matching_habits = [name for name in data if name.get("Name") == del_habit_name]

        if not matching_habits:
            print("Please enter a habit name that is in the list.")
            return
        # Delete the defined habit
        filtered_data = [name for name in data if name["Name"] != del_habit_name]

        print("You successfully deleted a habit")

        with open("habit_data.json", "w") as file:
            json.dump(filtered_data, file, indent=8)
    


    def edit_habit_name(self, old_habit_name, new_habit_name):
        with open("habit_data.json", "r") as file:
            data = json.load(file)
        # Check if the habit that should be deleted is in the file
        matching_habits_old = [habit for habit in data if habit.get("Name") == old_habit_name]

        if not matching_habits_old:
            print("Please enter a habit name that is in the list.")
            return
        # Check if the newly defined habit name is a duplicate of an already existing habit
        matching_habits_new = [habit for habit in data if habit.get("Name") == new_habit_name]

        if matching_habits_new:
            print("Please enter a habit name that is not a duplicate.")
            return
        # Change the name of the habit
        for habit in data:
            if habit["Name"] == old_habit_name:
                habit["Name"] = new_habit_name

        print("You successfully edited a habit.")
        
        with open("habit_data.json", "w") as file:
            json.dump(data, file, indent=4)



    def edit_habit_period(self, habit_name, new_habit_period):

        with open("habit_data.json", "r") as file:
            data = json.load(file)
        # Check if the newly defined habit name is a duplicate of an already existing habit
        matching_habits_old = [habit for habit in data if habit.get("Name") == habit_name]

        if not matching_habits_old:
            print("Please enter a habit name that is in the list.")
            return
        # Change the period of the habit
        for new_period in data:
            if new_period["Name"] == habit_name:
                new_period["Period in days"] = new_habit_period 

        print("You successfully edited a habit.")
            
        with open("habit_data.json", "w") as file:
            json.dump(data, file, indent=8, default=str)



    def edit_habit_cost(self, habit_name, new_habit_cost):

        with open("habit_data.json", "r") as file:
            data = json.load(file)
        # Check if the newly defined habit name is a duplicate of an already existing habit
        matching_habits_old = [habit for habit in data if habit.get("Name") == habit_name]

        if not matching_habits_old:
            print("Please enter a habit name that is in the list.")
            return
        # Change the cost of the habit
        for new_cost in data:
            if new_cost["Name"] == habit_name:
                new_cost["Cost in euro"] = new_habit_cost 

        print("You successfully edited a habit.")
            
        with open("habit_data.json", "w") as file:
            json.dump(data, file, indent=8, default=str)



    def check_off(self, habit_name):

        with open("habit_data.json", "r") as file:
            check_off = json.load(file)
        # Check if the newly defined habit name is a duplicate of an already existing habit
        matching_habits = [habit for habit in check_off if habit.get("Name") == habit_name]

        if not matching_habits:
            print("Please enter a habit name that is in the list.")
            return
        # Check what type of period is tracked by the Habit
        for period in check_off:
            if period.get("Period in days") == 1:
                i = 1
        
            elif period.get("Period in days") == 7:
                i = 7

        searched_habit = None
        # Look if the habit name is found in the file
        for habit in check_off:
            if habit["Name"] == habit_name:
               searched_habit = habit

        if searched_habit is not None:
            """
            Get the date of when the habit was last checked and convert
            it into format from which it can be calculated. Calculate the
            difference between today and the last time the habit was checked.
            """
            last_checked_date = searched_habit['Last checked']
            
            last_checked_date = datetime.strptime(last_checked_date, "%Y-%m-%d").date()

            today = datetime.now().date()

            time_dif = today - last_checked_date

            total_days = time_dif.days + (time_dif.seconds / 86400)

            total_days_as_int = int(total_days)

            # Daily habit tracking
            if i == 1:
                # Chosen if it was last checked yesterday
                if total_days_as_int == 1:
                    for habit in check_off:
                        # Find the habit 
                        if habit["Name"] == habit_name:
                            # Increase the current streak length by one
                            habit["Current streak length"] += 1
                            # Add the Cost of the habit to the total money saved
                            habit["Money saved in euro"] += habit["Cost in euro"]
                # Chosen if it was last checked later then yesterday          
                elif total_days_as_int > 1:
                    for habit in check_off:
                        # Find the habit
                        if habit["Name"] == habit_name:
                            # Set the current streak length to one
                            habit["Current streak length"] = 1
                            # Add the Cost of the habit to the total money saved
                            habit["Money saved in euro"] += habit["Cost in euro"]
                # Chosen if it was last checked today            
                elif total_days_as_int < 1:
                    print("You have already checked the habit.")
                    return

            # Weekly habit tracking
            if i == 7:
                # Chosen if it was last checked a week ago
                if 7 < total_days_as_int < 14:
                    for habit in check_off:
                        # Find the habit 
                        if habit["Name"] == habit_name:
                            # Increase the current streak length by one
                            habit["Current streak length"] += 1
                            # Add the Cost of the habit to the total money saved
                            habit["Money saved in euro"] += habit["Cost in euro"]
                # Chosen if it was last checked later than a week ago           
                elif total_days_as_int > 14:
                    for habit in check_off:
                        # Find the habit 
                        if habit["Name"] == habit_name:
                            # Set the current streak length to one
                            habit["Current streak length"] = 1
                            # Add the Cost of the habit to the total money saved
                            habit["Money saved in euro"] += habit["Cost in euro"]
                # Chosen if it was already checked this week            
                elif total_days_as_int <= 7:
                    print("You have already checked the habit.")
                    return

            # Update the Longest streak length if the Current streak length is larger
            for habit in check_off:
                if habit["Current streak length"] > habit["Longest streak"]:
                    for habit in check_off:
                        if habit["Name"] == habit_name:
                            habit["Longest streak"] += 1
                else:
                    pass
            # Update the last time the habit was checked to today
            for habit in check_off:
                if habit["Name"] == habit_name:
                    habit["Last checked"] = datetime.now().date().isoformat()

            print("You have checked the habit.")

            with open("habit_data.json", "w") as file:
                json.dump(check_off, file, indent=8, default=str)        

    
    # Display the habits in a table. Sort them based on their creation dates
    def display_all_habits(self):  

        df = pd.read_json('habit_data.json')
        print(df.to_string())

    # Display the habits in two tables. Sort them based on their periodicities
    def display_all_habits_periodicity(self):

        df = pd.read_json('habit_data.json')

        grouped = df.groupby("Period in days")

        for group, group in grouped:
            print(group.to_string())
            print()
    
    # Display the habits in a table. Sort them based on their longest current streak lengths
    def display_all_habits_longest_current_streak(self):

        df = pd.read_json('habit_data.json')
        sorted_df = df.sort_values(by = "Current streak length", ascending = False)
        print(sorted_df)

    # Display the habits in a table. Sort them based on their all time streak lengths
    def display_all_habits_longest_all_time_streak(self):

        df = pd.read_json('habit_data.json')
        sorted_df = df.sort_values(by = "Longest streak", ascending = False)
        print(sorted_df)

    # Display the habits in a table. Sort them based on their costs
    def display_all_habits_cost(self):

        df = pd.read_json('habit_data.json')
        sorted_df = df.sort_values(by = "Cost in euro", ascending = False)
        print(sorted_df)

    # Display the habits in a table. Sort them based on their amount of money saved
    def display_all_habits_money_saved(self):

        df = pd.read_json('habit_data.json')
        sorted_df = df.sort_values(by = "Money saved in euro", ascending = False)
        print(sorted_df)
