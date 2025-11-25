import sqlite3

print("Post Lab of 06 Devansh Karia")

conn = sqlite3.connect('student_record.db')

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS student_record(

#         Enrollment INTEGER PRIMARY KEY,
#         Name TEXT NOT NULL,
#         Subject TEXT NOT NULL,
#         Mark INTEGER NOT NULL
        
#         )''')

# #commit Changes

# conn.commit()

# student_record = [
#     (92510133006, 'Devansh Karia', 'PWP', 95),
#     (92510133015, 'Mafaz Musani', 'PWP', 97),
#     (92510133023, 'Krishraj Rathod', 'PWP', 91),
#     (92510133025, 'Jenish Desai', 'PWP', 92),
#     (92510133003, 'Manthan Dobariya', 'PWP', 89)
#     ]

# cursor.executemany('''INSERT INTO student_record (Enrollment, Name, Subject, Mark)
#                    VALUES (?,?,?,?)''', student_record)

# conn.commit()

# cursor.execute('SELECT * FROM student_record')
# rows = cursor.fetchall()
# print("All Student Records: ")
# for row in rows:
#     print(row)
    

# #For student Have marks more than 90
# cursor.execute('SELECT Name, Subject, Mark FROM student_record WHERE Mark > 90')
# high_Marks = cursor.fetchall()

# print("\n Students with Marks greater than 90: ")
# for student in high_Marks:
#     print(student)

# #Update Marks
# cursor.execute('''UPDATE student_record SET Mark = 99 
#                   WHERE name = 'Krishraj Rathod' AND subject = 'PWP' ''')

# conn.commit()

# #Verify The Update

# cursor.execute('SELECT Name, Mark FROM student_record WHERE name = "Krishraj Rathod"')
# updated_mark = cursor.fetchone()
# print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}")  
   
# # Delete a student record (e.g.,DEVENDRASINH DOLATSINH JADEJA )
# cursor.execute('''DELETE FROM student_record WHERE name = 'Manthan Dobariya' ''')

# # Commit the changes
# conn.commit()

# # Verify the deletion
# cursor.execute('SELECT * FROM student_record WHERE name = "Manthan Dobariya"')
# deleted_name = cursor.fetchone()

# if deleted_name is None:
#     print("\n Manthan Dobariya has been successfully deleted.")

# # Calculate the average Mark
# cursor.execute('''SELECT AVG(Mark) FROM student_record''')
# avg_mark = cursor.fetchone()[0]

# print(f"\nThe average mark of students is: {avg_mark:.2f}")

# conn.close()

#--------------------------------------------Post-Lab--------------------------------------------

import sqlite3

print("Post Lab of 06 Devansh Karia")

# Step 1: Connect to SQLite database
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

# Step 2: Create the table with composite primary key
cursor.execute('''
CREATE TABLE IF NOT EXISTS student_record(
    Enrollment INTEGER,
    Name TEXT NOT NULL,
    Subject TEXT NOT NULL,
    Mark INTEGER NOT NULL,
    PRIMARY KEY (Enrollment, Subject)
)
''')
conn.commit()

# Step 3: Insert multiple subject records for each student
student_record = [
    (92510133006, 'Devansh Karia', 'PWP', 92),
    (92510133006, 'Devansh Karia', 'SS', 94),
    (92510133006, 'Devansh Karia', 'ICE', 91),
    (92510133006, 'Devansh Karia', 'APTI', 90),
    (92510133060, 'Devansh Karia', 'DSC', 83),

    (92510133015, 'Mafaz Musani', 'PWP', 90),
    (92510133015, 'Mafaz Musani', 'SS', 87),
    (92510133015, 'Mafaz Musani', 'ICE', 91),
    (92510133015, 'Mafaz Musani', 'APTI', 89),
    (92510133015, 'Mafaz Musani', 'DSC', 90),

    (92510133023, 'Krishraj Rathod', 'PWP', 81),
    (92510133023, 'Krishraj Rathod', 'SS', 92),
    (92510133023, 'Krishraj Rathod', 'ICE', 91),
    (92510133023, 'Krishraj Rathod', 'APTI', 89),
    (92510133023, 'Krishraj Rathod', 'DSC', 95),

    (92510133025, 'Jenish Desai', 'PWP', 91),
    (92510133025, 'Jenish Desai', 'SS', 86),
    (92510133025, 'Jenish Desai', 'ICE', 94),
    (92510133025, 'Jenish Desai', 'APTI', 96),
    (92510133025, 'Jenish Desai', 'DSC', 87),

    (92510133003, 'Manthan Dobariya', 'PWP', 82),
    (92510133003, 'Manthan Dobariya', 'SS', 96),
    (92510133003, 'Manthan Dobariya', 'ICE', 85),
    (92510133003, 'Manthan Dobariya', 'APTI', 89),
    (92510133003, 'Manthan Dobariya', 'DSC', 91),
]

cursor.executemany('''
INSERT OR REPLACE INTO student_record (Enrollment, Name, Subject, Mark)
VALUES (?, ?, ?, ?)
''', student_record)
conn.commit()

# Step 4: Display All Records
print("\nAll Student Records:")
cursor.execute('SELECT * FROM student_record')
for row in cursor.fetchall():
    print(row)

# Step 5: Display Students with Marks > 90
print("\nStudents with Marks Greater Than 90:")
cursor.execute('SELECT Name, Subject, Mark FROM student_record WHERE Mark > 90')
for row in cursor.fetchall():
    print(row)

# Step 6: Update a Mark
cursor.execute('''
UPDATE student_record 
SET Mark = 98 
WHERE Name = 'Mafaz Musani' AND Subject = 'PWP'
''')
conn.commit()

# Step 7: Confirm Update
cursor.execute('''
SELECT Name, Mark FROM student_record 
WHERE Name = 'Mafaz Musani' AND Subject = 'PWP'
''')
updated = cursor.fetchone()
if updated is not None:
    print(f"\nUpdated Mark for {updated[0]} in PWP: {updated[1]}")
else:
    print("\nNo matching record found for Mafaz Musani in PWP.")

# Step 8: Delete Jenish Desai’s DSC record
cursor.execute('''
DELETE FROM student_record 
WHERE Name = 'Jenish Desai' AND Subject = 'DSC'
''')
conn.commit()

# Step 9: Confirm Deletion
cursor.execute('''
SELECT * FROM student_record 
WHERE Name = 'Jenish Desai' AND Subject = 'DSC'
''')
if cursor.fetchone() is None:
    print("\nJenish Desai's DSC record has been successfully deleted.")

# Step 10: Calculate Average Mark
cursor.execute('SELECT AVG(Mark) FROM student_record')
average = cursor.fetchone()[0]
print(f"\nAverage Mark of All Students: {average:.2f}")

conn.close()




