SELECT g.grade, s2.name, g2.name  
FROM grades g
JOIN subjects s ON s.id = g.subject_id AND s.name = 'Calculus'
JOIN students s2 ON s2.id = g.student_id
JOIN groups g2 on g2.id = s2.group_id AND g2.name = 'K-13'
WHERE s.name = 'Calculus';