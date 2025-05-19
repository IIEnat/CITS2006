# CLI Login System with Access Control

This is a **simple Command-Line Interface (CLI) Login System** designed to demonstrate **Role-Based Access Control (RBAC)**.

This program is designed to **demonstrate the concept of access control**. It shows how different user roles have different levels of access. The functionality is **intentionally minimal** to focus on the **core access control logic**, not on building a fully featured application.

## How It Works
- Users log in using a **username and password**.
- Depending on their **role** (Admin, User, or Guest), they are shown different **menu options** and **permissions**.

## Roles and Permissions
- **Admin**: View all users, shutdown system.
- **User**: View their own profile.
- **Guest**: Read-only access.

## Usage
1. Run the program with:
   ```
   python cli_login_access_control.py
   ```
2. Example login credentials:
   - **Admin**: `admin` / `admin123`
   - **User**: `user1` / `userpass`
   - **Guest**: `guest` / `guestpass`

