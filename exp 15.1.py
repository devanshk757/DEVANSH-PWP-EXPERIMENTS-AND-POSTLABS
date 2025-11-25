import sqlite3

print("Post Lab of 06 Devansh Karia")

conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

# User input
student_enroll = int(input("Enter your Enrollment no.: "))
student_name = input("Enter Your Name: ")

# Check if student exists
cursor.execute("SELECT Enrollment FROM student_record WHERE Enrollment = ?", (student_enroll,))
result = cursor.fetchone()

if result:
    Subject = input("Enter the subject name: ")
    Mark = int(input("Enter the Mark of the Respective Subject: "))

    # Use INSERT OR REPLACE to avoid UNIQUE constraint error
    cursor.execute('''
        INSERT OR REPLACE INTO student_record (Enrollment, Name, Subject, Mark)
        VALUES (?, ?, ?, ?)
    ''', (student_enroll, student_name, Subject, Mark))

    conn.commit()
    print(f"\nSubject '{Subject}' with mark {Mark} has been added/updated for {student_name} ({student_enroll}).")

else:
    print("\nStudent not found in the database.")

conn.close()
