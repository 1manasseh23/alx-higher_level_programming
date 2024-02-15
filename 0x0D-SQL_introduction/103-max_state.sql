-- 103-max_state.sql

-- This is a script that displays the max temperature of each state (ordered by State name)
SELECT state, MAX(max_temp) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
