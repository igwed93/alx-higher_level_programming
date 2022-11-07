-- lists all Comedy shows in the database
-- wget https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      import the dump table into the hbtn_0d_tvshows
--
-- each record should display: tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT s.`title`
    FROM tv_shows AS s
INNER JOIN tv_show_genres AS t
    ON s.`id` = t.`show_id`
INNER JOIN tv_genres AS g
    ON g.`id` = t.`genre_id`
WHERE g.`name`='Comedy'
GROUP BY s.`title`
ORDER BY s.`title` ASC;
