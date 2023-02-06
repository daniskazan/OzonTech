-- Напишите запрос к базе данных, который построит таблицу результатов для соревнования с максимальным id.
--
-- Вывод должен включать всех пользователей, кто сделал хотя бы одну попытку в этом соревновании.
-- Вывод должен включать 5 колонок:
--
-- rank — место пользователя в контесте (пользователи с одинаковыми результатами делят место);
-- user_id — id пользователя;
-- user_name — name пользователя;
-- problem_count — количество решённых в контесте задач (если одна задача решена многократно, то всё-равно учитывается как одна задача);
-- latest_successful_submitted_at — время, когда была решена последняя из решённых задач у этого пользователя
-- (если одна задача решена многократно, то задача считается решённой в момент первого решения),
-- иными словами, последний момент времени, когда у пользователя увеличилось количество решённых задач.
--
-- Строки следует сортировать по невозрастанию problem_count,
-- затем по неубыванию latest_successful_submitted_at,
-- затем по возрастанию user_id.
--
-- Пользователи, которые решили одинаковое количество задач (имеют равные problem_count)
-- и имеют равные значения latest_successful_submitted_at, должны поделить одно место.
-- Обратите внимание, что если несколько пользователей делят места, то в нумерации мест образуется разрыв.
-- Например, если первое место делят два пользователя,
-- то следующий пользователь должен получить место 3(то есть последовательность мест имеет вид: 1,1,3).



WITH cte AS (
    SELECT
           s.user_id as user_id,
           u.name as user_name,
           count(DISTINCT s.problem_id) AS problem_count,
           max(CASE WHEN s.success = true THEN s.submitted_at ELSE NULL END) AS latest_successful_submitted_at
    FROM submissions s
    JOIN users u ON s.user_id = u.id
    JOIN problems p ON s.problem_id = p.id
    JOIN contests c ON p.contest_id = c.id
    WHERE c.id = (SELECT MAX(id) FROM contests)
    GROUP BY s.user_id, u.name
    )

SELECT
       RANK() OVER (PARTITION BY problem_count, latest_successful_submitted_at) as rank,
       user_id,
       user_name,
       problem_count,
       latest_successful_submitted_at
FROM cte
ORDER BY
         problem_count DESC,
         latest_successful_submitted_at ASC,
         user_id ASC