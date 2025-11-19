# Ask the user for their full name
user_name = input("Enter your full name: ")
print(f"Hello, {user_name}!")  # Greet the user using their name

# Ask for birth year and calculate age
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_year = 2025
current_age = current_year - birth_year  # Calculate current age

# Define a function to determine life stage based on age
def life_stage(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

# Create an empty list to store hobbies
hobbies = []

# Ask the user for hobbies until they type 'stop'
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':  # Case-insensitive check
        break
    hobbies.append(hobby)  # Add hobby to the list

# Display the final profile summary
print("\nProfile Summary:")
print(f"Name: {user_name}")
print(f"Age: {current_age}")
print(f"Life Stage: {life_stage(current_age)}")

# Print hobbies if any were entered
if hobbies:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")  # Print each hobby with a bullet
else:
    print("You didn't mention any hobbies.")  # Message if no hobbies were entered