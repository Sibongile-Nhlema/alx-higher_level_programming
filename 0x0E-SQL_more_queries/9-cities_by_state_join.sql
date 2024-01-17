-- This script lists all cities contained in hbtn_0d_usa
-- resuts are in ascending order by cities.id
-- display: cities.id - cities.name - states.name
SELECT  cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.states_id = states.id
ORDER BY cities.id;
