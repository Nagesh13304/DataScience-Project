import pandas as pd

# Sample Data
data = {
    'Student ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 21, 22, 23],
    'Grade': ['A', 'B', 'A', 'C'],
    'Attendance (%)': [95, 80, 85, 70]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# 1. Display Records
def display_records():
    print("\nStudent Records:")
    print(df)

# 2. Add a New Record
def add_record(student_id, name, age, grade, attendance):
    global df
    new_record = {
        'Student ID': student_id,
        'Name': name,
        'Age': age,
        'Grade': grade,
        'Attendance (%)': attendance
    }
    df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    print("\nNew record added successfully!")

# 3. Search for a Student
def search_student(student_id):
    result = df[df['Student ID'] == student_id]
    if not result.empty:
        print("\nStudent Found:")
        print(result)
    else:
        print("\nStudent not found!")

# 4. Calculate Average Attendance
def calculate_average_attendance():
    average = df['Attendance (%)'].mean()
    print(f"\nAverage Attendance: {average:.2f}%")

# 5. Save to CSV
def save_to_csv(filename='student_records.csv'):
    df.to_csv(filename, index=False)
    print(f"\nRecords saved to {filename}")

# Menu
while True:
    print("\nMenu:")
    print("1. Display Records")
    print("2. Add Record")
    print("3. Search Student")
    print("4. Calculate Average Attendance")
    print("5. Save to CSV")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        display_records()
    elif choice == 2:
        sid = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        attendance = float(input("Enter Attendance (%): "))
        add_record(sid, name, age, grade, attendance)
    elif choice == 3:
        sid = int(input("Enter Student ID to search: "))
        search_student(sid)
    elif choice == 4:
        calculate_average_attendance()
    elif choice == 5:
        save_to_csv()
    elif choice == 6:
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid choice! Please try again.")
