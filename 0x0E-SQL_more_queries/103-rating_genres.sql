-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Records are ordered by descending rating.
SELECT `name`, SUM(`rating`) AS `rating sum`
FROM `tv_genres`
GROUP BY `name`
ORDER BY `rating sum` DESC;
