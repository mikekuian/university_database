import sqlite3
from faker import Faker
import random

fake = Faker()

conn = sqlite3.connect('university.db')
cur = conn.cursor()

# Створення таблиць
# Тут вставте SQL скрипти створення таблиць

# Генерація та вставка даних
# Спочатку для груп
for _ in range(3):  # 3 групи
    cur.execute("INSERT INTO groups (name) VALUES (?)", (fake.word().capitalize(),))

# Для викладачів
for _ in range(5):  # 5 викладачів
    cur.execute("INSERT INTO teachers (name) VALUES (?)", (fake.name(),))

# Для предметів
teachers_ids = [i for i, in cur.execute("SELECT id FROM teachers").fetchall()]
for _ in range(8):  # 8 предметів
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (fake.word().capitalize(), random.choice(teachers_ids)))

# Для студентів
groups_ids = [i for i, in cur.execute("SELECT id FROM groups").fetchall()]
for _ in range(50):  # 50 студентів
    cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (fake.name(), random.choice(groups_ids)))

# Для оцінок
students_ids = [i for i, in cur.execute("SELECT id FROM students").fetchall()]
subjects_ids = [i for i, in cur.execute("SELECT id FROM subjects").fetchall()]
for _ in range(100):  # 100 оцінок
    cur.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)", 
                (random.choice(students_ids), random.choice(subjects_ids), random.randint(1, 5), fake.date()))

conn.commit()
conn.close()
