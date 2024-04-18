# 0x0E. SQL - More queries

In this project, I kept practicing on SQL queries, working with permissoins, joins, and unions.

# Tasks 📃

# 0. My privileges!

  + <u>[0-privileges.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/0-privileges.sql)</u>: `A script that lists all privileges of the MySQL users user_0d_1 and user_0d_2.`

# 1. Root user

  + <u>[1-create_user.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/1-create_user.sql)</u>: `A script that creates the MySQL server user user_0d_1.`

# 2. Read user

  + <u>[2-create_read_user.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/2-create_read_user.sql)</u>: `MySQL script that creates the database hbtn_0d_2 and the user user_0d_2 with password`

`user_0d_2_pwd.`

# 3. Always a name

  + <u>[3-force_name.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/3-force_name.sql)</u>: `MySQL script that creates the table force_name.`

  + Description:

	- id INT.

	- name VARCHAR(256) can’t be null.

# 4. ID can't be null

  + <U>[4-never_empty.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/4-never_empty.sql)</u>: `MySQL script that creates the table id_not_null.`

  + Description:

	- id INT with the default value 1.

	- name VARCHAR(256).

# 5. Unique ID

  + <u>[5-unique_id.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/5-unique_id.sql)</u>: `MySQL script that creates the table unique_id.`

  + Description:

	- id INT with the default value 1 and must be unique.

	- name VARCHAR(256).

# 6. States table

  + <u>[6-states.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/6-states.sql)</u>: `A script that creates the database hbtn_0d_usa and the table states.`

  + Description:

	- id INT unique, auto generated, can’t be null and is a primary key.

	- name VARCHAR(256) can’t be null.

# 7. Cities table

  + <u>[7-cities.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/7-cities.sql)</u>: `A script that creates the database hbtn_0d_usa and the table cities.`

  + Description:

	- id INT unique, auto generated, can’t be null and is a primary key.

	- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table.

	- name VARCHAR(256) can’t be null.

# 8. Cities of California

  + <u>[8-cities_of_california_subquery.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql)</u>: MySQL script that lists all the cities of California that can be found in the database hbtn_0d_us, sorted in ascending order by cities.id.

# 9. Cities by States

  + <u>[9-cities_by_state_join.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/9-cities_by_state_join.sql)</u>: MySQL script that lists all cities contained in the database hbtn_0d_usa, sorted in ascending order by cities.id.

# 10. Genre ID by show

  + <u>[10-genre_id_by_show.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/10-genre_id_by_show.sql)</u>: MySQL script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

# 11. Genre ID for all shows

  + <u>[11-genre_id_all_shows.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/11-genre_id_all_shows.sql)</u>: MySQL script that lists all shows contained in the database hbtn_0d_tvshows, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

  + If a show doesn’t have a genre, display NULL.

# 12. No genre

  + <u>[12-no_genre.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/12-no_genre.sql)</u>: MySQL script that lists all shows contained in hbtn_0d_tvshows without a genre linked, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

# 13. Number of shows by genre

  + <u>[13-count_shows_by_genre.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/13-count_shows_by_genre.sql)</u>: A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

# 14. My genres

  + <u>[14-my_genres.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/14-my_genres.sql)</u>: A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter, sorted in ascending order by the genre name.

# 15. Only Comedy

  + <u>[15-comedy_only.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/15-comedy_only.sql)</u>: MySQL script that lists all Comedy shows in the database hbtn_0d_tvshows, sorted in ascending order by the show title.

# 16. List shows and genres

  + <u>[16-shows_by_genre.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/16-shows_by_genre.sql)</u>: MySQL script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows, sorted in ascending order by the show title and genre name.
