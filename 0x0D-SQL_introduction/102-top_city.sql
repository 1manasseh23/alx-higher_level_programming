-- 102-top_city.sql

-- This is a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(avg_tem) AS avg_temperature
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temperature DESC
LIMIT 3;
