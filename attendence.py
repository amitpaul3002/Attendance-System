import pandas as pd

# Create a list of students
students = [
    {"Roll No": 1, "Name": "abhik", "Attendance": 0},
    {"Roll No": 2, "Name": "amit", "Attendance": 0},
    {"Roll No": 3, "Name": "barnali", "Attendance": 0},
    {"Roll No": 4, "Name": "bhaskar", "Attendance": 0},
    {"Roll No": 5, "Name": "samrat", "Attendance": 0},
    {"Roll No": 6, "Name": "smritikona", "Attendance": 0},
    {"Roll No": 7, "Name": "dipanwita", "Attendance": 0},
    {"Roll No": 8, "Name": "subham", "Attendance": 0},
    # Add more students as needed
]

# Convert the list into a DataFrame
df = pd.DataFrame(students)

# Save to a CSV file
csv_path = r"D:\New folder\project\data.csv"
df.to_csv(csv_path, index=False)

# Save to an Excel file
excel_path = r"D:\New folder\project\data.xlsx"
df.to_excel(excel_path, index=False)

print(f"Files created:\nCSV: {excel_path}\n")
