# DRF Event Feed Backend
**[LS_test_task](https://github.com/Zeroitman/LS_test_task)**

# About the project 
Project for receiving personal feed with events

## Stack

- Python 3.10
- Django 5.2.2
- DRF 3.16.0
- Postgres 14.15

## Local Development
Before running the project locally you should have Postgres and created a database for the project, if not then follow the instructions:
```
1. sudo -i -u postgres # Login as a system user
2. psql # Launch the interactive PostgreSQL console
3. CREATE DATABASE db_name; # Create a database for the project
4. CREATE USER myuser WITH PASSWORD 'mypassword'; # Create a new user
5. GRANT ALL PRIVILEGES ON DATABASE db_name TO myuser; # Grant the user rights to your database
6. ALTER USER myuser CREATEDB; # Allow the user to create a database, which will be needed for tests;
```

To run the project locally, follow these instructions:
```
1. git clone # clone project
2. cd LS_test_task # open project folder
3. cp .env.example backend/.env # Copy environment variables to the project backend folder
4. Make sure that the environment variables in the .env file match the values ​​you specified when creating the DB for the project
5. cd backend # go to the project folder
6. poetry install # install project dependencies and automatically install the environment
7. poetry env activate # command that will show which command should be executed to activate the created virtual environment
8. Run the command output for activate virtual environment
9. ./manage.py migrate # performs migrations
10. ./manage.py seed # loads seeds, superuser will be added with admin/admin
11. ./manage.py test # run test (not required)
12. ./manage.py runserver # launches the project
```
In the project, the functionality of the event feed with various cases is covered by tests. To run the tests, run the command
```
./manage.py test
```
During development, pays attention to the quality of the code. Flake8 is installed in the project. Run the command
```
poetry run flake8
```
drf-spectacular is connected, which automatically generates API documentation in OpenAPI 3.0 format, in which you can test the functionality and view the structure of the request and response.
```
host:port/docs/redoc/ # structure in the request and response
host:port/docs/swagger/ # test and make requests
host:port/docs/schema/ # get the schema
```

