import re
from activity import Activity, CardioActivity, RunningActivity
from file_handler import write_json, read_json, dict_to_obj


def get_date():
    while True:
        date = input("Date (DD.MM.YYYY): ").strip()

        if re.match(r"^\d{2}\.\d{2}\.\d{4}$", date):
            return date
        else:
            print("Invalid date format. Please use DD.MM.YYYY.")


def get_duration():
    while True:
        try:
            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            total = (hours*60) + minutes

            if total > 0:
                return total
            else:
                print("Duration must be greater than 0.")
        except ValueError:
            print("Hours and minutes must be a whole number.")


def get_calories():
    while True:
        try:
            calories = int(input("Calories burned: "))

            if calories > 0:
                return calories
            else:
                print("Calories burned must be greater than 0")
        except ValueError:
            print("Calories burned must be a whole number.")


def get_distance():
    while True:
        try:
            km = int(input("Kilometres passed: "))
            m = int(input("Metres passed: "))
            distance = km + (m/1000)

            if distance > 0:
                return distance
            else:
                print("Distance must be greater than 0.")
        except ValueError:
            print("Kilometres and metres must be a whole number.")


def get_heartrate():
    while True:
        try:
            heartrate = int(input("Enter average heart rate: "))

            if heartrate > 0:
                return heartrate
            else:
                print("Heart rate must be greater than 0.")
        except ValueError:
            print("Heart rate must be a whole number.")


def create_activity():
    print("\nCreating a new workout...")

    workout_type = input("Workout type: ").strip()
    total_duration = get_duration()
    calories = get_calories()
    date = get_date()

    return Activity(workout_type, total_duration, calories, date)


def create_cardio_activity():
    print("\nCreating a new workout...")

    workout_type = input("Workout type: ").strip()
    total_duration = get_duration()
    calories = get_calories()
    date = get_date()
    distance = get_distance()
    heartrate = get_heartrate()

    return CardioActivity(workout_type, total_duration, calories, date, distance, heartrate)


def create_running_activity():
    print("\nCreating a new workout...")

    workout_type = input("Workout type: ").strip()
    total_duration = get_duration()
    calories = get_calories()
    date = get_date()
    distance = get_distance()
    heartrate = get_heartrate()
    terrain = input("Enter type of terrain: ").strip()

    return RunningActivity(workout_type, total_duration, calories, date, distance, heartrate, terrain)


def load_workouts():
    try:
        data = read_json()
        return dict_to_obj(data)
    except(FileNotFoundError, Exception):
        print("No recorded workouts found.")
        return []


def display_workouts(workouts):
    if not workouts:
        print("No workouts to display.")
        return

    counter = 1
    for workout in workouts:
        print(f"{counter}. {workout}")
        counter += 1


def filter_workouts(workouts):
    keyword = input("Enter activity type to filter by: ").strip().lower()
    filtered = list(filter(lambda w: keyword in w.type.lower(), workouts))

    if filtered:
        print(f"\nWorkouts matching '{keyword}': ")
        display_workouts(filtered)
    else:
        print(f"No workouts found matching '{keyword}'.")

    return filtered


def sort_workouts(workouts):
    print(f"\nSort by:\n"
          f"1. Duration\n"
          f"2. Calories\n"
          f"3. Date")
    choice = input("Choose 1,2 or 3: ").strip()

    while choice not in("1", "2", "3"):
        print("Invalid entry")
        choice = input("Choose 1,2 or 3: ").strip()

    if choice == "1":
        sorted_workouts = sorted(workouts, key=lambda w: w.duration)
    elif choice == "2":
        sorted_workouts = sorted(workouts, key=lambda w: w.calories)
    else:
        sorted_workouts = sorted(workouts, key=lambda w: w.date)

    print("\nSorted workouts: ")
    display_workouts(sorted_workouts)

    return sorted_workouts


def show_summary(workouts):
    if not workouts:
        print("No workouts to summarise.")
        return

    total_duration = sum(w.duration for w in workouts)
    total_calories = sum(w.calories for w in workouts)
    count = len(workouts)

    avg_duration = total_duration / count
    avg_calories = total_calories / count

    print(f"\n--- Workout summary ---")
    print(f"Total workouts: {count}")
    print(f"Total duration : {total_duration} minutes.")
    print(f"Total calories burned: {total_calories}.")
    print(f"Average duration: {avg_duration:.1f} minutes.")
    print(f"Average calories burned: {avg_calories:.1f}.")


if __name__ == '__main__':
    running = True
    print("Welcome to Ivan's Fitness App!")

    while running:
        print(f"\nMain menu\n"
              f"1. Add new activity\n"
              f"2. Show recorded workouts\n"
              f"3. Quit")

        answer = input("What would you like to do?(Type 1, 2 or 3): ").strip()

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

            activity = input("What would you like to do?(Type 1, 2, 3 or 4):").strip()

            while activity not in ("1","2","3","4"):
                print("Invalid entry")
                activity = input("What would you like to do?(Type 1, 2, 3 or 4):")
                activity = activity.strip()

            if activity == "1":
                workout = create_activity()
                write_json(workout)
                print("Workout saved.")

            elif activity == "2":
                workout = create_activity()
                write_json(workout)
                print("Workout saved.")

            elif activity == "3":
                workout = create_running_activity()
                write_json(workout)
                print("Workout saved.")

        elif answer == "2":
            workouts = load_workouts()

            if workouts:
                print("\nRecorded workouts: ")
                display_workouts(workouts)

                print(f"\nOptions:\n"
                      f"1. Filter by type\n"
                      f"2. Sort workouts\n"
                      f"3. Show summary\n"
                      f"4. Back to main menu")

                sub = input("Choose option 1, 2, 3 or 4: ").strip()

                while sub not in ("1", "2", "3", "4"):
                    print("Invalid entry.")
                    sub = input("Choose option 1, 2, 3 or 4: ").strip()

                if sub == "1":
                    filter_workouts(workouts)

                elif sub == "2":
                    sort_workouts(workouts)

                elif sub == "3":
                    show_summary(workouts)

        elif answer == "3":
            print("Goodbye!")
            running = False
















