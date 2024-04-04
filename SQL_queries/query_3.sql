SELECT gr.name AS group_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Calculus'
GROUP BY gr.id
ORDER BY average_grade DESC;