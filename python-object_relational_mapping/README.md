# Python - Object-Relational Mapping

## Description
This project focuses on bridging the gap between Relational Databases and Python using Object-Relational Mapping (ORM). The first part interacts with the database directly using `MySQLdb` module, while the second part uses `SQLAlchemy` ORM framework.

## Files
* `0-select_states.py` - Lists all states from the database.
* `1-filter_states.py` - Lists all states starting with 'N'.
* `2-my_filter_states.py` - Filters states based on user input (vulnerable to SQL injection).
* `3-my_safe_filter_states.py` - Filters states based on user input safely.
* `4-cities_by_state.py` - Lists all cities from the database.
* `5-filter_cities.py` - Lists all cities of a specific state.
* `model_state.py` - State class definition for SQLAlchemy.
* `7-model_state_fetch_all.py` - Fetches all State objects via SQLAlchemy.
* `8-model_state_fetch_first.py` - Fetches first State object.
* `9-model_state_filter_a.py` - Filters States containing letter 'a'.
* `10-model_state_my_get.py` - Gets specific State object matching input argument.
* `11-model_state_insert.py` - Inserts "Louisiana" into states.
* `12-model_state_update_id_2.py` - Updates name of State where id=2.
* `13-model_state_delete_a.py` - Deletes all State objects containing letter 'a'.
* `model_city.py` - City class definition for SQLAlchemy.
* `14-model_city_fetch_by_state.py` - Fetches cities joined with states.

