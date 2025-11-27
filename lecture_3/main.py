def avg(nums):
    # Calculate the average of a list of numbers
    # Return None if the list is empty
    return sum(nums) / len(nums) if nums else None

def normalize(grades):
    # Keep only valid integer grades in the range [0, 100]
    return [g for g in grades if isinstance(g, int) and 0 <= g <= 100]

def find_student(students, name):
    # Search for a student by name in the list
    # Return the student dictionary if found, otherwise None
    for s in students:
        if s["name"] == name:
            return s
    return None

def add_new_student(students):
    # Add a new student to the list
    # Prevent empty names and duplicate entries
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if find_student(students, name):
        print(f"Student '{name}' already exists.")
        return
    students.append({"name": name, "grades": []})
    print(f"Added student: {name}")

def add_grades_for_student(students):
    # Add grades for an existing student
    # Grades must be integers between 0 and 100
    name = input("Enter student name: ").strip()
    student = find_student(students, name)
    if not student:
        print(f"Student '{name}' not found.")
        return

    while True:
        raw = input("Enter a grade (or 'done' to finish): ").strip().lower()
        if raw == "done":
            break
        try:
            grade = int(raw)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
                print(f"Added grade {grade} to {name}.")
            else:
                print("Invalid grade. Please enter a number from 0 to 100 (inclusive).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_full_report(students):
    # Generate a report of all students and their average grades
    # Also display max, min, and overall average
    print("--- Student Report ---")
    if not students:
        print("No students to report.")
        return

    all_avgs = []
    for s in students:
        name = s["name"]
        valid = normalize(s["grades"])
        if not valid:
            print(f"{name}'s average grade is N/A.")
            continue
        a = avg(valid)
        all_avgs.append(a)
        print(f"{name}'s average grade is {a:.2f}.")

    if all_avgs:
        print(f"\nMax Average: {max(all_avgs):.2f}")
        print(f"Min Average: {min(all_avgs):.2f}")
        print(f"Overall Average: {avg(all_avgs):.2f}")
    else:
        print("No valid grades to compute statistics.")

def find_top_student(students):
    # Find the student(s) with the highest average grade
    # Handle ties and empty grade lists
    print("--- Top Student ---")
    scored = []
    for s in students:
        valid = normalize(s["grades"])
        if valid:
            scored.append((s["name"], avg(valid)))

    if not scored:
        print("No valid grades available.")
        return

    best_avg = max(scored, key=lambda x: x[1])[1]
    top = [(n, a) for n, a in scored if a == best_avg]

    if len(top) == 1:
        n, a = top[0]
        print(f"The student with the highest average is {n} with a grade of {a:.2f}.")
    else:
        print("Tie for top student:")
        for n, a in top:
            print(f"- {n} with a grade of {a:.2f}")

def main():
    # Main program loop with menu-driven interface
    students = []
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1 Add a new student")
        print("2 Add grades for a student")
        print("3 Generate a full report")
        print("4 Find the top student")
        print("5 Exit program")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_new_student(students)
        elif choice == "2":
            add_grades_for_student(students)
        elif choice == "3":
            generate_full_report(students)
        elif choice == "4":
            find_top_student(students)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1–5.")

if __name__ == "__main__":
    # Entry point of the program
    main()
