SELECT s.name AS SubjectName, s2.name AS StudentName
FROM subjects s
JOIN grades g ON s.id = g.subject_id
JOIN students s2 ON s2.id = g.student_id
WHERE s2.name = 'William Mason';