0x0E. SQL - More queries

# In this project, I kept practicing on SQL queries, working with permissoins, joins, and unions.

Tasks

0. My privileges!

	0-privileges.sql: A script that lists all privileges of the MySQL users user_0d_1 and user_0d_2.

1. Root user

	1-create_user.sql: A script that creates the MySQL server user user_0d_1.

2. Read user

	2-create_read_user.sql: MySQL script that creates the database hbtn_0d_2 and the user user_0d_2 with password user_0d_2_pwd.

3. Always a name

	3-force_name.sql: MySQL script that creates the table force_name.

	Description:

	id INT.

	name VARCHAR(256) can’t be null.

4. ID can't be null

	4-never_empty.sql: MySQL script that creates the table id_not_null.

	Description:

	id INT with the default value 1.

	name VARCHAR(256).

5. Unique ID

	5-unique_id.sql: MySQL script that creates the table unique_id.

	Description:

	id INT with the default value 1 and must be unique.

	name VARCHAR(256).

6. States table

	6-states.sql: A script that creates the database hbtn_0d_usa and the table states.

	Description:

	id INT unique, auto generated, can’t be null and is a primary key.

	name VARCHAR(256) can’t be null.

7. Cities table

	7-cities.sql: A script that creates the database hbtn_0d_usa and the table cities.

	Description:

	id INT unique, auto generated, can’t be null and is a primary key.

	state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table.

	name VARCHAR(256) can’t be null.

8. Cities of California

	8-cities_of_california_subquery.sql: MySQL script that lists all the cities of California that can be found in the database hbtn_0d_us, sorted in ascending order by cities.id

9. Cities by States

	9-cities_by_state_join.sql: MySQL script that lists all cities contained in the database hbtn_0d_usa, sorted in ascending order by cities.id.

10. Genre ID by show

	10-genre_id_by_show.sql: MySQL script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

11. Genre ID for all shows

	11-genre_id_all_shows.sql: MySQL script that lists all shows contained in the database hbtn_0d_tvshows, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

	If a show doesn’t have a genre, display NULL.

12. No genre

	12-no_genre.sql: MySQL script that lists all shows contained in hbtn_0d_tvshows without a genre linked, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

13. Number of shows by genre

	13-count_shows_by_genre.sql: A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

14. My genres

	14-my_genres.sql: A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter, sorted in ascending order by the genre name.

15. Only Comedy

	15-comedy_only.sql: MySQL script that lists all Comedy shows in the database hbtn_0d_tvshows, sorted in ascending order by the show title.

16. List shows and genres

	16-shows_by_genre.sql: MySQL script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows, sorted in ascending order by the show title and genre name.

