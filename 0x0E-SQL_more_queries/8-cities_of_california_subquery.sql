-- list all cities that can be found in database
SELECT cities.id, cities.name FROM cities, states
WHERE cities.state_id = states.id AND states.name = "california"
ORDER BY cities.id ASC;
