# Initialize an empty dictionary to store user information
user_info = {}

# Function to add user information to the dictionary
def add_user(name, age):
    user_info[name] = age
    print(f"User {name} added successfully.")

# Function to retrieve user information by name
def get_user(name):
    if name in user_info:
        print(f"{name}'s age is {user_info[name]}.")
    else:
        print(f"No information found for {name}.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add User")
    print("2. Get User Information")
    print("3. Exit")
    choice = input("Please choose an option (1/2/3): ")

    if choice == "1":
        name = input("Enter the user's name: ")
        age = int(input(f"Enter {name}'s age: "))
        add_user(name, age)
    elif choice == "2":
        name = input("Enter the name to retrieve information: ")
        get_user(name)
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")
