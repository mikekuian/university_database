SELECT s.name AS SubjectName
FROM grades g
JOIN subjects s ON g.subject_id = s.id
JOIN teachers t ON s.teacher_id = t.id
JOIN students s2 ON g.student_id = s2.id
WHERE s2.name = 'William Mason' AND t.name = 'Andryi Stawrowskii';