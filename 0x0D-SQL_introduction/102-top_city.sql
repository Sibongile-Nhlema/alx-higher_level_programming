-- This script displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT city, AVG(value) avg_temp
FROM temperatures
WHERE month = 7 || month = 8
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;
