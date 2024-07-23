import json
from datetime import datetime

# Function to load existing data from a JSON file
def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Function to save data to a JSON file
def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Function to log a workout
def log_workout(workouts):
    date = input("Enter the date (YYYY-MM-DD): ")
    exercise = input("Enter the exercise name: ")
    duration = input("Enter the duration in minutes: ")
    calories = input("Enter the calories burned: ")

    workout = {
        'exercise': exercise,
        'duration': int(duration),
        'calories': int(calories)
    }

    if date in workouts:
        workouts[date].append(workout)
    else:
        workouts[date] = [workout]

    print("Workout logged!")

# Function to view workouts
def view_workouts(workouts):
    if not workouts:
        print("No workouts logged yet.")
        return

    for date, exercises in workouts.items():
        print(f"\nDate: {date}")
        for workout in exercises:
            print(f"  Exercise: {workout['exercise']}, Duration: {workout['duration']} minutes, Calories: {workout['calories']} kcal")

# Main function to run the fitness tracker
def main():
    filename = 'workouts.json'
    workouts = load_data(filename)

    while True:
        print("\nFitness Tracker")
        print("1. Log a Workout")
        print("2. View Workouts")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            log_workout(workouts)
            save_data(workouts, filename)
        elif choice == '2':
            view_workouts(workouts)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
