def get_age():
    while True:
        age_input = input("Enter your age (1–120): ")
        if not age_input.isdigit():
            print("Invalid input. Please enter a valid number.\n")
            continue
        
        age = int(age_input)
        if age < 1 or age > 120:
            print("Out of range. Please enter a number between 1 and 120.\n")
            continue

        return age

age = get_age()
print(f"\nYour age is {age}")
