-- This script lists duplicates in the database (based on scores)
SELECT `score`, COUNT(*) AS `number` FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
