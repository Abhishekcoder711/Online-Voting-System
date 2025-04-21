# Online-Voting-System

A Command-Line Interface (CLI) based **Online Voting System** developed using **Python**. This project allows users to register, log in, cast their vote for political parties, and view real-time voting results. It ensures secure authentication and prevents duplicate voting.

## Features

- Voter Registration
- Secure Login Authentication
- Vote Casting to Party A, B, or C
- Prevents Double Voting
- View Live Voting Results
- Simple and Interactive CLI Interface

## Technologies Used

- **Language:** Python 3
- **Modules:** `getpass`, custom class-based structure (`User`, `VotingSystem`)
- **Security:** Password input is hidden using `getpass`
- **Voting Integrity:** Only one vote per user is allowed

## 📂 File Structure
online-voting-system/ │ ├── main.py # Main application loop ├── users.py # User management (register, login) ├── votes.py # Voting logic and result display └── README.md # Project documentation


## ▶ How to Run

1. **Download or clone the repository:**

   ```bash
   git clone https://github.com/Abhishekcoder711/Online-Voting-System

2. **To Run the Main file
   ```bash
   python mani.py

## Example Output
1. Register
2. Login
3. Vote
4. View Results
5. Exit
Enter your choice:

## Limitations
--> Data is stored in runtime memory; exiting the app resets data.
--> No external database or file storage implemented yet.

## License
This project is intended for educational use only.

## Author
Abhishek Kumar Mishra,
Chandigarh University
