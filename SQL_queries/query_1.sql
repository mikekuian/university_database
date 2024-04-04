SELECT s.id, s.name, AVG(g.grade) as average_grade
from students s join grades g 
WHERE s.id = g.student_id 
GROUP by s.id 
order by average_grade DESC 
LIMIT 5;