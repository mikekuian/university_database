SELECT s.name 
FROM subjects s 
JOIN teachers t ON s.teacher_id = t.id 
WHERE t.name = 'Andryi Stawrowskii'
ORDER BY s.name;