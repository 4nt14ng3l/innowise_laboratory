import sqlite3

# --- Step 1: Create Database and Tables ---
def setup_database():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Create table: students
    # id: unique identifier (Primary Key)
    # full_name: full name of the student
    # birth_year: year of birth
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        birth_year INTEGER
    )
    ''')

    # Create table: grades
    # id: unique identifier (Primary Key)
    # student_id: foreign key referencing students.id
    # subject: name of the subject
    # grade: grade between 1 and 100
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        grade INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    ''')

    conn.commit()
    conn.close()

# --- Step 2: Insert Sample Data ---
def insert_data():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Prevent duplicate insertion if data already exists
    cursor.execute('SELECT COUNT(*) FROM students')
    if cursor.fetchone()[0] > 0:
        print("Data already inserted")
        conn.close()
        return

    # Sample students
    students = [
        ('Alice Johnson', 2005), ('Brian Smith', 2004), ('Carla Reyes', 2006),
        ('Daniel Kim', 2005), ('Eva Thompson', 2003), ('Felix Nguyen', 2007),
        ('Grace Patel', 2005), ('Henry Lopez', 2004), ('Isabella Martinez', 2006)
    ]

    # Sample grades
    grades = [
        (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
        (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
        (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
        (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
        (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
        (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
        (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
        (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
        (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92)
    ]

    cursor.executemany('INSERT INTO students (full_name, birth_year) VALUES (?, ?)', students)
    cursor.executemany('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', grades)

    conn.commit()
    conn.close()

# --- Step 3: SQL Queries ---
def query_grades_for_alice(cursor):
    # Find all grades for Alice Johnson
    cursor.execute('''
    SELECT subject, grade FROM grades
    JOIN students ON grades.student_id = students.id
    WHERE full_name = 'Alice Johnson'
    ''')
    return cursor.fetchall()

def query_average_per_student(cursor):
    # Calculate average grade per student
    cursor.execute('''
    SELECT full_name, AVG(grade) FROM grades
    JOIN students ON grades.student_id = students.id
    GROUP BY student_id
    ''')
    return cursor.fetchall()

def query_students_born_after_2004(cursor):
    # List all students born after 2004
    cursor.execute('SELECT full_name, birth_year FROM students WHERE birth_year > 2004')
    return cursor.fetchall()

def query_average_per_subject(cursor):
    # List all subjects and their average grades
    cursor.execute('SELECT subject, AVG(grade) FROM grades GROUP BY subject')
    return cursor.fetchall()

def query_top_3_students(cursor):
    # Find the top 3 students with the highest average grades
    cursor.execute('''
    SELECT full_name, AVG(grade) as avg_grade FROM grades
    JOIN students ON grades.student_id = students.id
    GROUP BY student_id
    ORDER BY avg_grade DESC
    LIMIT 3
    ''')
    return cursor.fetchall()

def query_students_below_80(cursor):
    # Show all students who scored below 80 in any subject
    cursor.execute('''
    SELECT DISTINCT full_name FROM grades
    JOIN students ON grades.student_id = students.id
    WHERE grade < 80
    ''')
    return cursor.fetchall()

# --- Step 4: Menu to Run Queries ---
def run_queries():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    print("Choose a query:")
    print("1 - All grades for Alice Johnson")
    print("2 - Average grade per student")
    print("3 - Students born after 2004")
    print("4 - Average grade per subject")
    print("5 - Top 3 students by average grade")
    print("6 - Students with any grade below 80")

    choice = input("Enter query number: ")

    if choice == '1':
        results = query_grades_for_alice(cursor)
    elif choice == '2':
        results = query_average_per_student(cursor)
    elif choice == '3':
        results = query_students_born_after_2004(cursor)
    elif choice == '4':
        results = query_average_per_subject(cursor)
    elif choice == '5':
        results = query_top_3_students(cursor)
    elif choice == '6':
        results = query_students_below_80(cursor)
    else:
        print("Invalid choice")
        conn.close()
        return

    # Print results
    for row in results:
        print(row)

    conn.close()

# --- Run Program ---
setup_database()
insert_data()
run_queries()
