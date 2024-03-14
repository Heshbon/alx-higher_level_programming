-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
-- Display NULL if a show doesn’t have a genre.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
