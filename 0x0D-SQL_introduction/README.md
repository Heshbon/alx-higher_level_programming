# 0x0D. SQL - Introduction.

This is my first project in which I began to work with SQL and relational databases. I began practicing introductory data definition and data manipulation language, making subqueries, and using functions.

Tasks 📃

# 0. List databases

  + <u>[0-list_databases.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/0-list_databases.sql)</u>: A script that lists all databases of  MySQL server.

# 1. Create a database

  + <u>[1-create_database_if_missing.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/1-create_database_if_missing.sql)</u>: MySQL scirpt that creates the database hbtn_0c_0.

# 2. Delete a database

  + <u>[2-remove_database.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/2-remove_database.sql)</u>: MySQL script that deletes the database hbtn_0c_0.

# 3. List tables

  + <u>[3-list_tables.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/3-list_tables.sql)</u>: MySQL script that lists all the tables of a database.

# 4. First table

  + <u>[4-first_table.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/4-first_table.sql)</u>: MySQL script that creates a table called first_table.

  + Description:

	- id INT.

	- name VARCHAR(256).

# 5. Full description

  + <u>[5-full_table.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/5-full_table.sql)</u>: A script that prints the full description of the table first_table from the database hbtn_0c_0.

# 6. List all in table

  + <u>[6-list_values.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/6-list_values.sql)</u>: A script that lists all rows of the table first_table from the database hbtn_0c_0.

# 7. First add

  + <u>[7-insert_value.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/7-insert_value.sql)</u>: MySQL sript that inserts a new row in the table first_table (database hbtn_0c_0).

  + Description:

	- id = 89.

	- name = Best School.

# 8. Count 89

  + <u>[8-count_89.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/8-count_89.sql)</u>: MySQL script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0.

# 9. Full creation

  + <u>[9-full_creation.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/9-full_creation.sql)</u>: MySQL script that creates a table second_table in the database hbtn_0c_0.

  + Description:

	- id INT.

	- name VARCHAR(256).

	- score INT.

  + Records:

	- id = 1, name = “John”, score = 10.

	- id = 2, name = “Alex”, score = 3.

	- id = 3, name = “Bob”, score = 14.

	- id = 4, name = “George”, score = 8.

# 10. List by best

  + <u>[10-top_score.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/10-top_score.sql)</u>: MySQL script that lists both the score and the name for all records of the table second_table of the database hbtn_0c_0.

# 11. Select the best

  + <u>[11-best_score.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/11-best_score.sql)</u>: MySQL script that lists the score and the name of all records with a score >= 10 in the table second_table of the database hbtn_0c_0.

# 12. Cheating is bad

  + <u>[12-no_cheating.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/12-no_cheating.sql)</u>: A script that updates the score of Bob to 10 in the table second_table.

# 13. Score too low

  + <u>[13-change_class.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/13-change_class.sql)</u>: A script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

# 14. Average

  + <u>[14-average.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/14-average.sql)</u>: A script that computes the score average of all records in the table second_table of the database hbtn_0c_0.

# 15. Number by score

  + <u>[15-groups.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/15-groups.sql)</u>: MySQL script that list the score and number of records with the same score in the table second_table of the database hbtn_0c_0.

# 16. Say my name

  + <u>[16-no_link.sql](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/16-no_link.sql)</u>: A script that list the score and name of all records of the table second_table of the database hbtn_0c_0.
