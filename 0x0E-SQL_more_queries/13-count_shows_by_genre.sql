-- count the number of tv shows associated with a particular genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN  tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.id IS NOT NULL
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
