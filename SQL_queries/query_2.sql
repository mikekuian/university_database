SELECT s.name, g.grade
from students s join grades g join subjects s2 
WHERE s.id = g.student_id AND s2.name = "Calculus"
GROUP by s.id 
order by g.grade DESC 
LIMIT 1;