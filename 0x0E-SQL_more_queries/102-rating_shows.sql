-- Lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record displays: tv_shows.title - rating sum
SELECT `title`, SUM(`rating`) AS `rating sum`
FROM `tv_shows`
GROUP BY `title`
ORDER BY `rating sum` DESC;
