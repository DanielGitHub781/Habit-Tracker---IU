import unittest
from main import Habit
import json
from datetime import datetime, timedelta 

class testhabit(unittest.TestCase):

    def test_add_habit(self):
       
        habit = Habit("test", 1, 20)

        # Add the habit to the json file
        habit.add_habit()

        test_habit = {
                "Name": "test",
                "Period in days": 1,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 20,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }
        
        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        # Look if the test_habit can be found in the json file
        found = False
        for item in saved_data:
            if item == test_habit:
                found = True
                break

        # Check if the operation was succesful
        self.assertTrue(found)
            

    def test_del_habit(self):

        habit = Habit("test", 1, 20)

        # Delete the test habit from the json file
        habit.del_habit("test")

        test_habit = {
                "Name": "test",
                "Period in days": 1,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 20,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }

        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)
        
        # Look if the test_habit can not be found in the json file
        found = True
        for item in saved_data:
            if item == test_habit:
                found = False
                break

        # Check if the operation was succesful
        self.assertTrue(found)


    def test_edit_habit_name(self):

        habit = Habit("test", 1, 20)

        # Add the habit to the json file
        habit.add_habit()

        habit.edit_habit_name("test","test2")

        test_habit = {
                "Name": "test2",
                "Period in days": 1,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 20,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }
        
        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        # Look if the edited test_habit can not be found in the json file
        found = False
        for item in saved_data:
            if item == test_habit:
                found = True
                break
            
        # Check if the operation was succesful
        self.assertTrue(found)

        # Delete the test habit from the json file
        habit.del_habit("test2")

    def test_edit_habit_period(self):

        habit = Habit("test", 1, 20)

        # Add the habit to the json file
        habit.add_habit()

        habit.edit_habit_period("test", 7)

        test_habit ={ 
                "Name": "test",
                "Period in days": 7,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 20,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }
               
        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        # Look if the edited test_habit can not be found in the json file  
        found = False
        for item in saved_data:
            if item == test_habit:
                found = True
                break

        # Check if the operation was succesful
        self.assertTrue(found)

        # Delete the test habit from the json file
        habit.del_habit("test")

    def test_edit_habit_cost(self):

        habit = Habit("test", 1, 20)

        # Add the habit to the json file
        habit.add_habit()

        habit.edit_habit_cost("test", 40)

        test_habit = {
                "Name": "test",
                "Period in days": 1,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 40,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }
        
        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        # Look if the edited test_habit can not be found in the json file
        found = False
        for item in saved_data:
            if item == test_habit:
                found = True
                break  
        
        # Check if the operation was succesful
        self.assertTrue(found)

        # Delete the test habit from the json file
        habit.del_habit("test")

    def test_check_off(self):

        habit = Habit("test", 1, 20)

        # Add the habit to the json file
        habit.add_habit()

        habit.check_off("test")

        test_habit ={
                "Name": "test",
                "Period in days": 1,
                "Current streak length": 1,
                "Longest streak": 1,
                "Cost in euro": 20,
                "Money saved in euro": 20,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": datetime.now().date().isoformat()
        }
        
        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        # Look if the checked test_habit can not be found in the json file
        found = False
        for item in saved_data:
            if item == test_habit:
                found = True
                break

        # Check if the operation was succesful
        self.assertTrue(found)

        # Delete the test habit from the json file
        habit.del_habit("test")

if __name__ == "__main__":
    unittest.main()


              



