# Bond Test Task

Django project for managing movies.

## Try it!

Movie DataBase Project deployed on Render. Link:

    https://bond-test-task.onrender.com

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

Use the following command to parse data from https://www.omdbapi.com/ API:

    python manage.py scrape_movies

Due to slow API performance and because ids are chosen randomly, this may take some time.

## Features

1. Admin panel for advanced managing
2. Parsing data from API
3. Added Bootstrap for a better look
4. Managing Movies on website
5. Filtering by title, year, directors and actors
6. Added pagination
7. Added tests

## Demo

![demo.png](demo.png)



