-- This script  lists all genres in the database by rating
-- results are in  descending order by their rating
SELECT name, SUM(tv_show_ratings.rate) 'rating'
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
