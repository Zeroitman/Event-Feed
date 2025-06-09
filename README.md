# DRF Event Feed Backend

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
6. ALTER USER lc_user CREATEDB; # Allow the user to create a database, which will be needed for tests;
```

To run the project locally, follow these instructions:
```
1. cp .env.example backend/.env # Copy environment variables to the project backend folder
2. Make sure that the environment variables in the .env file match the values ​​you specified when creating the DB for the project
3. cd backend # go to the project folder
4. poetry install # install project dependencies and automatically install the environment
5. poetry env activate # command that will show which command should be executed to activate the created virtual environment
6. Run the command output
7. ./manage.py migrate # performs migrations
8. ./manage.py seed # loads seeds
9. ./manage.py runerver # launches the project
```
In the project, the functionality of the event feed with various cases is covered by tests. To run the tests, run the command
```
./manage.py test
```

