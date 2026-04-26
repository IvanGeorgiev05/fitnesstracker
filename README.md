#Project description 

This is a command_line fitness tracking application built in Python. The program allows
users to log different types of workouts such as general activities,
cardio activities and running activities, which are then saved to a JSON file.
Users can view their recorded workouts and have options to filter them by type,
sort by calories, date or duration and see a summary of totals and averages.


#Class structure

The project uses a three-level inheritance hierarchy as per project requirements.

Activity is the base class which represents a general fitness activity and stores
type, duration, calories burned and date. Includes property getters and setters with
validation. The to_dict method helps with writing to JSON files by converting
objects to dictionaries, the summary method is used for formated output and there
is an overloaded __add__ operator for combining activities which is also one of the
project requirements

CardioActivity inherits from Activity and extends it with distance and average 
heart rate attributes. It overrides summary(), to_dict() and __add__ to include
the new attributes. The __add__ operator averages heart rates when combining two
cardio activities 

RunningActivity inherits from CardioActivity and extends it with a terrain type
attribute. It also overrides summary(), to_dict() and _-add__ to include terrain




#Description of special functions or algorithms used

__add__ method overloads the "+" operator in all three classes to combine workout
data

the methods summary(), to_dict(), __add__ and __str__ are all polymorphic methods
overriden in each subclass

the get_date() method in main.py uses regex to make sure that the date is entered
in the correct format

configparser is used to read JSON filename from config.ini so that file paths are
not hardcoded

filter function is used with lambda to filter workouts by type

sorted function is used by the method sort_workouts() with a lambda key to
sort workouts by duration, calories or date


#How to run
1. Clone git repository with:
           git clone https://github.com/IvanGeorgiev05/fitnesstracker.git
           cd fitnesstracker
2. Run the application python main.py
3. The command_line interface will show the menu to add workouts, view 
recorded workouts and the options to filter, sort or summarise your recorded
workouts. There is also a quit option which exits the program.

#How to run unit tests

In the terminal window, use:

pip install coverage
coverage run -m unittest discover -s tests
coverage report




