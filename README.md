# Bond Test Task

Django project for managing movies.

## Try it!

Movie DataBase Project deployed on Render. Link:

    ### todo

## Installation

Python 3 should be installed. Install PostgresSQL and create db.

    https://github.com/Oomamchur/Bond_test_task
    cd Bond_test_task
    python -m venv venv

On Windows:

    venv\Scripts\activate

On macOS or Linux:

    source/bin/activate

This project uses environment variables to store sensitive information such as the Django secret key and database credentials.
Create a `.env` file in the root directory of your project and add your environment variables to it. This file should not be committed to the repository.
You can see the example in `.env.sample` file

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Use the following command to load prepared data from fixture to test and debug your code:

    python manage.py loaddata fixture_data.json

## Features

1. Admin panel for advanced managing
2. Added Bootstrap for a better look
3. Managing Movies on website
4. Filtering by title, year, directors and actors
5. Added pagination
6. Added tests

## Demo

![demo.png](demo.png)



