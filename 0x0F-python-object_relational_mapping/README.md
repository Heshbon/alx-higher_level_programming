0x0F. Python - Object-relational mapping

In this project, I learned about Python - Object-relational mapping in database scripting. I became familiar with using MySQLdb and SQLAlchemy to query, create, edit, and delete tables in MySQL.

Tasks 📃

0. Get all states

	0-select_states.py: Python script that lists all states from the database hbtn_0e_0_usa.

	Results are sorted in ascending order by states.id.

	Usage: ./0-select_states.py <mysql username> <mysql password> <database name>.

1. Filter states

	1-filter_states.py: Python script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

	Results are sorted in ascending order by states.id.

	Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>.

2. Filter states by user input

	2-my_filter_states.py: Python script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa.

	Results are sorted in ascending order by states.id.

	Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>.

3. SQL Injection...

	3-my_safe_filter_states.py: Python script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa.

	Results are sorted in ascending order by states.id.

	Safe from MySQL injection.

	Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>.

4. Cities by states

	4-cities_by_state.py: Python script that lists all cities from the database hbtn_0e_4_usa.

	Results are sorted in ascending order by cities.id.

	Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>.

5. All cities by state

	5-filter_cities.py: Python script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.

	Results are sorted in ascending order by cities.id.

	Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name>.

6. First state model

	model_state.py: Python file that contains the class definition of a State and an instance Base = declarative_base().

7. All states via SQLAlchemy

	7-model_state_fetch_all.py: Python script that lists all State objects from the database hbtn_0e_6_usa.

	Results are sorted in ascending order by states.id.

	Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>.

8. First state

	8-model_state_fetch_first.py: Python script that prints the first State object from the database hbtn_0e_6_usa.

	If the table states is empty, print Nothing.

	Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>.

9. Contains `a`

	9-model_state_filter_a.py: Python script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.

	Results are sorted in ascending order by states.id.

	Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>.

10. Get a state

	10-model_state_my_get.py: Python script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa.

	If no state searched for, display Not found.

	Display the states.id.

	Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name to search>.

11. Add a new state

	11-model_state_insert.py: Python script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.

	Print the new states.id after creation.

	Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>.

12. Update a state

	12-model_state_update_id_2.py: Python script that changes the name of a State object from the database hbtn_0e_6_usa.

	Usage: ./12-model_state_update_id_2.py <mysql usernam> <mysql password> <database name>.

13. Delete states

	13-model_state_delete_a.py: Python script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa.

	Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>.

14. Cities in state

	model_city.py: Python file that contains the class definition of a City.

		Includes class attribute that is foreign key to states.id.


	14-model_city_fetch_by_state.py: Python script that prints all City objects from the database hbtn_0e_14_usa.

	Results are sorted in ascending order by cities.id.

	Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>.
