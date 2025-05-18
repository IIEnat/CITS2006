# Secure Password Manager (SPM)

This is a **simple but secure command-line password manager** built with Python and SQLAlchemy. It allows you to securely store encrypted passwords for various services in a local SQLite database (`passwords.db`). I would consider this password manager actually secure as the key used for encrypting and decrypting passwords is stored locally in the user's file system so if an attacker were to gain access to the db file, they would NOT be able to decrypt the stored encrypted passwords. 

## Features
- Add service credentials (service name, username, password)
- View all stored credentials (with decrypted passwords)

### Required Python Packages
```
sqlalchemy
python-dotenv
cryptography
```

## Setup Instructions

### 1. Generate a Valid Fernet Key
Use the following Python snippet to generate a valid key:
```
python
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
```
Copy the generated key.

### 2. Create the `.env` File
In the same directory as `password_manager.py`, create a file named `.env` with the following content:
```
SECRET_KEY=your_generated_fernet_key_here
```
Replace `your_generated_fernet_key_here` with the generated key from the previous step.

### 3. Install Dependencies
Run the following command:
```
pip install sqlalchemy python-dotenv cryptography
```

### 4. Run the Program
```
python3 password_manager.py
```

## Usage
- **1. Add Entry**: Store a new service username and password (passwords are encrypted).
- **2. View Entries**: List all stored services and their decrypted passwords.
- **3. Exit**: Close the program.

## Notes
- The database `passwords.db` will be created in the same directory if it doesn't already exist.
- Ensure you keep your `.env` file secure. Losing or exposing your `SECRET_KEY` compromises the security of your stored data.
