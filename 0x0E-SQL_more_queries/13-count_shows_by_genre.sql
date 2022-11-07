-- lists all genres hbtn_0d_tvshows and displays the number of shows linked to each.
-- wget https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      import the dump table into the hbtn_0d_tvshows
--
-- each record should display: tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT g.`name` AS `genre`, 
COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON g.`id` = s.`genre_id`
GROUP BY g.`name`
ORDER BY `number_of_shows` DESC;
