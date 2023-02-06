-- Напишите запрос к базе данных, который возвращает все задачи,
-- которые были решены не менее чем двумя пользователями.
-- Найденные задачи следует отсортировать по id.

SELECT p.id, p.contest_id, p.code
FROM problems p
JOIN submissions s ON s.problem_id = p.id AND s.success=true
GROUP BY p.id
HAVING COUNT(DISTINCT s.user_id) >= 2
ORDER BY p.id
