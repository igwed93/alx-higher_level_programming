-- lists all genres of the show Dexter
-- wget https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      import the dump table into the hbtn_0d_tvshows
--
-- each record should display: tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT tv_genres.`name`
    FROM tv_genres
WHERE tv_genres.name NOT IN (
SELECT tv_genres.`name`
    FROM tv_genres
INNER JOIN tv_show_genres
    ON tv_genres.`id` = tv_show_genres.`genre_id`
INNER JOIN tv_shows
    ON tv_show_genres.`show_id` = tv_shows.`id`
WHERE tv_shows.`title`='Dexter')
ORDER BY tv_genres.`name` ASC;
