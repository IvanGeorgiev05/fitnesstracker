from activity import Activity, CardioActivity, RunningActivity
from file_handler import write_json, read_json, dict_to_obj
if __name__ == '__main__':
    running = True
    print("Welcome to Ivan's Fitness App!")
    while running:
        print(f"\nMain menu\n"
              f"1. Add new activity\n"
              f"2. Show recorded workouts\n"
              f"3. Quit")
        answer = input("What would you like to do?(Type 1, 2 or 3): ")
        answer = answer.strip()
        while answer not in("1", "2", "3"):
            print("Invalid entry")
            answer = input("What would you like to do?(Type 1, 2 or 3): ")
            answer = answer.strip()
        if answer == "1":
            print(f"\nChoose activity type:\n"
                  f"1. Activity\n"
                  f"2. Cardio Activity\n"
                  f"3. Running Activity\n"
                  f"4. Back to main menu")
            activity = input("What would you like to do?(Type 1, 2, 3 or 4):")
            activity = activity.strip()
            while activity not in ("1","2","3","4"):
                print("Invalid entry")
                activity = input("What would you like to do?(Type 1, 2, 3 or 4):")
                activity = activity.strip()
            if activity == "1":
                print("\nCreating a new workout...")
                workout_type = input("Workout type: ")
                total_duration = 0
                while total_duration == 0:
                    try:
                        hours = int(input("Hours: "))
                        minutes = int(input("Minutes: "))
                        total_duration = (hours * 60) + minutes
                    except ValueError:
                        print("Hours and minutes must be a whole number.")
                        continue
                calories = 0
                while calories == 0:
                    try:
                        calories = int(input("Calories burned: "))
                    except ValueError:
                        print("Calories burned must be a whole number")
                        continue
                date = input("Date(DD.MM.YYYY): ")
                workout = Activity(workout_type, total_duration, calories, date)
                write_json(workout)
                print("Workout saved.")
            elif activity == "2":
                    print("\nCreating a new workout...")
                    workout_type = input("Workout type: ")
                    total_duration = 0
                    while total_duration == 0:
                        try:
                            hours = int(input("Hours: "))
                            minutes = int(input("Minutes: "))
                            total_duration = (hours * 60) + minutes
                        except ValueError:
                            print("Hours and minutes must be a whole number.")
                            continue
                    calories = 0
                    while calories == 0:
                        try:
                            calories = int(input("Calories burned: "))
                        except ValueError:
                            print("Calories burned must be a whole number")
                            continue
                    date = input("Date(DD.MM.YYYY): ")
                    distance = 0
                    while distance == 0:
                        try:
                            km = int(input("Kilometres passed: "))
                            m = int(input("Metres passed: "))
                            distance = km + (m/1000)
                        except ValueError:
                            print("Kilometres and metres must be a whole number")
                            continue
                    heartrate = 0
                    while heartrate == 0:
                        try:
                            heartrate = int(input("Enter average heart rate: "))
                        except ValueError:
                            print("Heart rate must be a whole number")
                            continue
                    workout = CardioActivity(workout_type, total_duration, calories, date, distance, heartrate)
                    write_json(workout)
                    print("Workout saved.")
            elif activity == "3":
                print("\nCreating a new workout...")
                workout_type = input("Workout type: ")
                total_duration = 0
                while total_duration == 0:
                    try:
                        hours = int(input("Hours: "))
                        minutes = int(input("Minutes: "))
                        total_duration = (hours * 60) + minutes
                    except ValueError:
                        print("Hours and minutes must be a whole number.")
                        continue
                calories = 0
                while calories == 0:
                    try:
                        calories = int(input("Calories burned: "))
                    except ValueError:
                        print("Calories burned must be a whole number")
                        continue
                date = input("Date(DD.MM.YYYY): ")
                distance = 0
                while distance == 0:
                    try:
                        km = int(input("Kilometres passed: "))
                        m = int(input("Metres passed: "))
                        distance = km + (m / 1000)
                    except ValueError:
                        print("Kilometres and metres must be a whole number")
                        continue
                heartrate = 0
                while heartrate == 0:
                    try:
                        heartrate = int(input("Enter average heart rate: "))
                    except ValueError:
                        print("Heart rate must be a whole number")
                        continue
                terrain = input("Enter type of terrain: ")
                workout = RunningActivity(workout_type, total_duration, calories, date, distance, heartrate, terrain)
                write_json(workout)
                print("Workout saved.")
        elif answer == "2":
            print("Recorded workouts: ")
            counter = 1
            for workout in dict_to_obj(read_json()):
                print(f"{counter}. {workout}")
                counter +=1















