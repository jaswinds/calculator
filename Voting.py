# Get user input
nationality = input("Enter your nationality (Indian/Australian): ").strip().lower()
age = int(input("Enter your age: "))
caste = input("Enter your caste: ").strip().lower()

# Check voting eligibility
if (nationality == "Indian" or nationality == "Australian") and caste == "singh" and age >= 18:
    print("You have the right to vote.")
else:
    print("You do not have the right to vote.")