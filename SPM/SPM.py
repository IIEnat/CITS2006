import os
from getpass import getpass
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# Load .env variables
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

if not SECRET_KEY:
    raise ValueError("SECRET_KEY not found in .env file")

try:
    fernet = Fernet(SECRET_KEY)
except Exception as e:
    raise ValueError("Invalid SECRET_KEY. Make sure it is a valid Fernet key.")

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine('sqlite:///passwords.db')
Session = sessionmaker(bind=engine)
session = Session()

class PasswordEntry(Base):
    __tablename__ = 'passwords'
    id = Column(Integer, primary_key=True)
    service = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password_encrypted = Column(String, nullable=False)

Base.metadata.create_all(engine)

def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password.encode()).decode()

def add_entry():
    service = input("Service: ")
    username = input("Username: ")
    password = getpass("Password: ")
    encrypted_password = encrypt_password(password)
    entry = PasswordEntry(service=service, username=username, password_encrypted=encrypted_password)
    session.add(entry)
    session.commit()
    print("Entry added successfully.")

def view_entries():
    entries = session.query(PasswordEntry).all()
    for e in entries:
        decrypted_password = decrypt_password(e.password_encrypted)
        print(f"Service: {e.service}, Username: {e.username}, Password: {decrypted_password}")

def main():
    while True:
        print("\n1. Add Entry\n2. View Entries\n3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
