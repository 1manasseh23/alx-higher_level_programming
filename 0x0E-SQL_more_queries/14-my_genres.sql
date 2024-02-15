-- 14-my_genres.sql


-- This a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT g.`name`
FROM `tv_genres` AS g
JOIN `tv_show_genres` AS s ON s.`genre_id` = g.`id`
JOIN `tv_shows` AS t ON t.`id` = s.`show_id`
WHERE t.`title` = 'Dexter'
ORDER BY g.`name` ASC;
