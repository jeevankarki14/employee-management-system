# Employee Management System

A command-line Employee Management System written in Python. The project provides separate roles for a boss, managers, and employees, with role-specific menus and file-based data storage.

## Features

- Boss, manager, and employee login
- Profile viewing and editing
- Employee and manager record management
- Search and delete operations
- Employee password reset
- Employee enquiries and suggestions
- Input validation for names, age, email, salary, and passwords
- Automatic local data-file setup

## Project Structure

```text
.
├── Code/
│   ├── main.py
│   ├── boss.py
│   ├── manager.py
│   ├── employee.py
│   └── setup.py
├── EMS File/
│   └── .gitkeep
├── .gitignore
└── README.md
```

The files inside `EMS File/` are generated locally when the application starts. Runtime `.txt` data is excluded from Git so employee records and passwords are not accidentally committed.

## Requirements

- Python 3.10 or newer recommended
- No third-party packages are required

## Run the Program

From the project root:

```bash
python Code/main.py
```

On some systems, use `python3` instead of `python`.

## Demo Accounts

On the first run, the application creates local demo accounts:

| Role | Email | Password |
|---|---|---|
| Boss | `boss@example.com` | `boss123` |
| Manager | `manager@example.com` | `manager123` |
| Employee | `employee@example.com` | `employee123` |

These accounts are for demonstration only.

## Data Storage

This educational version stores records in local text files using pipe-separated values (`|`). It is suitable for demonstrating Python file handling and basic CRUD operations.

> **Security note:** Passwords are still stored as plain text in the local runtime files. A production system should use a database, hashed passwords, access controls, and stronger authentication.

## Authors / Student Information

The student information displayed by the application is retained from the original academic project.
