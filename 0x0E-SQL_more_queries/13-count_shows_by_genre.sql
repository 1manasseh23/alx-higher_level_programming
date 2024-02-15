-- 13-count_shows_by_genre.sql

-- This a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
