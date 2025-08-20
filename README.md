# Attendance-System
A web application to track student attendance automatically from group photos using facial recognition. Teachers can upload a class photo, generate attendance reports and manage records easily.

Features

Upload group photo → detect faces and mark attendance automatically

Attendance reports → download CSV files with present/absent status

Daily attendance view → check who was present for each session

Total attendance summary → track cumulative attendance over time

Student image database → view stored student images

Simple teacher login system → credentials stored in users.csv

Process

Upload group image from the dashboard

System detects faces and marks attendance automatically

Check the generated attendance report

View daily attendance logs

View total attendance summary

Download the full CSV report

Manage student image database as needed

Tech Stack

Backend: Flask (Python)

Frontend: HTML, CSS (Jinja templates)

Database: CSV/Excel files (Pandas for data handling)

Face recognition: OpenCV / face_recognition / MTCNN

Installation

Clone this repository:

git clone https://github.com/amitpaul3002/Attendance-System.git
cd attendance-monitor


Create and activate a virtual environment :

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Generate initial data files:

python attendance.py
python create_user.py


Run the Flask app:

python app.py


Open in browser:

http://127.0.0.1:5000

Default Login
Username: teacher1  
Password: pass123  


(Modify users.csv to add/change teachers)

Project Structure
attendance-monitor/
│
├── app.py                # Main Flask app
├── attendance.py         # Creates initial student CSV/Excel
├── create_user.py        # Creates default teacher login
├── data.csv / data.xlsx  # Student attendance records
├── users.csv             # Teacher credentials
│
├── templates/            # HTML templates
│   ├── about.html
│   ├── contact.html
│   ├── dashboard.html 
│   ├── database.html
│   ├── index.html 
│   ├── login.html
│   ├── result.html
│   ├── total_attendance.html
│   └── updated_attendance.html
│
└── static/               # CSS, result images, etc.
    ├── Data/
    |     └──IMAGES
    ├── style.css
    └── style2.css

Contributing

Feel free to fork this project and submit pull requests for new features or bug fixes.
DEVELOPER --- Amit Paul and his friends
