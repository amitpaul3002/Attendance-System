import csv

with open('users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['username', 'password'])
    writer.writerow(['teacher1', 'pass123'])
    writer.writerow(['teacher2', 'admin456'])

print("users.csv created successfully.")
