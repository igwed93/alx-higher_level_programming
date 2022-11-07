-- lists all shows without the genre comedy in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
    ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title ASC;
