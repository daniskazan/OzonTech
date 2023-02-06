-- Напишите запрос к базе данных,
-- который возвращает всех пользователей вместе с некоторой дополнительной информацией:

-- 1)количеством соревнований, в которых он принял участие и решил там хотя бы одну задачу,
-- соответствующую колонку в выводе следует назвать solved_at_least_one_contest_count,
-- 2)количеством соревнований, в которых он принял участие (то есть сделал хотя бы одну попытку решения),
-- соответствующую колонку в выводе следует назвать take_part_contest_count.

-- Строки в выводе сортируйте в первую очередь по невозрастанию solved_at_least_one_contest_count,
-- затем по невозрастанию take_part_contest_count, затем по возрастанию id.

WITH cte AS (
SELECT
s.user_id,
u.name as user_name,
count(distinct case when s.success=true then s.problem_id) AS problem_count,
max(CASE WHEN s.success = true THEN s.submitted_at ELSE NULL END) AS latest_successful_submitted_at
FROM submissions s
JOIN users u ON s.user_id = u.id
JOIN problems p ON s.problem_id = p.id
JOIN contests c ON p.contest_id = c.id
WHERE c.id = (SELECT MAX(id) FROM contests) and s.success=true
GROUP BY s.user_id, u.name
)
SELECT
RANK() OVER (ORDER BY problem_count DESC, latest_successful_submitted_at DESC) as rank,
user_id,
user_name,
problem_count,
latest_successful_submitted_at
FROM cte
WHERE problem_count > 0
ORDER BY
problem_count DESC,
latest_successful_submitted_at ASC,
user_id ASC;