from getpass import getpass

# Simple user database with roles
USER_DB = {
    "admin": {"password": "admin123", "role": "Admin"},
    "user1": {"password": "userpass", "role": "User"},
    "guest": {"password": "guestpass", "role": "Guest"}
}

def show_menu(role):
    print(f"\nLogged in as {role}")
    if role == "Admin":
        print("1. View All Users")
        print("2. Shutdown System")
    elif role == "User":
        print("1. View Profile")
    elif role == "Guest":
        print("1. Read-Only Access")

def perform_action(role):
    if role == "Admin":
        choice = input("Select an option: ")
        if choice == "1":
            print("\n--- User List ---")
            for username in USER_DB:
                print(f"- {username} ({USER_DB[username]['role']})")
        elif choice == "2":
            print("System shutting down...")
        else:
            print("Invalid option.")

    elif role == "User":
        print("\nAccessing user profile...")

    elif role == "Guest":
        print("\nRead-only access granted. Nothing more to see here.")

def login():
    print("Welcome to the CLI Login System")
    username = input("Username: ")
    password = getpass("Password: ")

    user = USER_DB.get(username)
    if user and user["password"] == password:
        show_menu(user["role"])
        perform_action(user["role"])
    else:
        print("\nLogin failed: Invalid username or password.")

if __name__ == "__main__":
    login()
