-- This script  lists all shows, and all genres linked to that show
-- If a show doesn’t have a genre,it displays NULL in the genre column
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name
