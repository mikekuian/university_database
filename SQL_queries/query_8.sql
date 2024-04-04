SELECT t.name AS TeacherName, sub.name AS SubjectName, AVG(g.grade) AS AverageGrade
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
JOIN grades g ON sub.id = g.subject_id
WHERE t.name = 'Andryi Stawrowskii'
GROUP BY t.name, sub.name
ORDER BY t.name, sub.name;