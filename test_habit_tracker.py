import unittest
from main import Habit
import json
from datetime import datetime, timedelta
import os


try:
    with open("habit_data.json", "r") as file:
        data = json.load(file)

    with open("habit_data_copy.json", "w") as file:
        json.dump(data, file, indent=8, default= str)

    if os.path.exists("habit_data.json"):
        os.remove("habit_data.json")

except FileNotFoundError:
    pass


class testhabit(unittest.TestCase):

    def test_add_habit(self):
       
        habit = Habit("test", 1, 20)

        habit.add_habit()

        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        test_habit = [
        {
                "Name": "test",
                "Period in days": 1,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 20,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }
        ]
            
        self.assertEqual(saved_data, test_habit)
    
    def test_del_habit(self):

        habit = Habit("test", 1, 20)

        habit.del_habit("test")

        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)
        
        self.assertEqual(saved_data, [])

    def test_edit_habit_name(self):

        habit = Habit("test", 1, 20)

        habit.add_habit()

        habit.edit_habit_name("test","test2")

        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        test_habit = [
        {
                "Name": "test2",
                "Period in days": 1,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 20,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }
        ]
            
        self.assertEqual(saved_data, test_habit)

        habit.del_habit("test2")

    def test_edit_habit_period(self):

        habit = Habit("test", 1, 20)

        habit.add_habit()

        habit.edit_habit_period("test", 7)

        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        test_habit = [
        {
                "Name": "test",
                "Period in days": 7,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 20,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }
        ]
            
        self.assertEqual(saved_data, test_habit)

        habit.del_habit("test")

    def test_edit_habit_cost(self):

        habit = Habit("test", 1, 20)

        habit.add_habit()

        habit.edit_habit_cost("test", 40)

        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        test_habit = [
        {
                "Name": "test",
                "Period in days": 1,
                "Current streak length": 0,
                "Longest streak": 0,
                "Cost in euro": 40,
                "Money saved in euro": 0,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": (datetime.now().date() - timedelta(days=10)).isoformat()
        }
        ]
            
        self.assertEqual(saved_data, test_habit)

        habit.del_habit("test")

    def test_check_off(self):

        habit = Habit("test", 1, 20)

        habit.add_habit()

        habit.check_off("test")

        with open("habit_data.json", "r") as file:
            saved_data = json.load(file)

        test_habit = [
        {
                "Name": "test",
                "Period in days": 1,
                "Current streak length": 1,
                "Longest streak": 1,
                "Cost in euro": 20,
                "Money saved in euro": 20,
                "Start date": datetime.now().date().isoformat(),
                "Last checked": datetime.now().date().isoformat()
        }
        ]
            
        self.assertEqual(saved_data, test_habit)

        habit.del_habit("test")



try:
    with open("habit_data_copy.json", "r") as file:
        data = json.load(file)

    with open("habit_data.json", "w") as file:
        json.dump(data, file, indent=8, default= str)

    if os.path.exists("habit_data_copy.json"):
        os.remove("habit_data_copy.json")

except FileNotFoundError:
    pass

if __name__ == "__main__":
    unittest.main()
