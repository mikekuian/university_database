import sqlite3

# Вкажіть назву вашої бази даних
database_name = 'university.db'

# Відкриваємо файл з SQL скриптом
with open('create_tables.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Підключаємось до бази даних (або створюємо нову)
conn = sqlite3.connect(database_name)

# Створюємо новий об'єкт курсора
cur = conn.cursor()

# Виконуємо SQL скрипт
cur.executescript(sql_script)

# Зберігаємо зміни
conn.commit()

# Закриваємо підключення до бази даних
conn.close()
