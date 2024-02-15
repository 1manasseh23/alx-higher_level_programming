-- 101-avg_temperatures.sql

-- This is a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Import the table dump
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
SURCE /path/to/avg_temperatures.sql;
ALTER DATABASE hbtn_0c_0_etmp RENAME TO hbtn_0c_0;

-- List average temperature by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM  hbtn_0c_0.second_table
GROUP BY city
ORDER BY AVG(temperature) DESC;
