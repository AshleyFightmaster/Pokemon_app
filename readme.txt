1. Flask Forms (WTForms)
-- Used to accept user information from the frontend, pass it to our backend, and store it in Database.

2. Flask Models (SQLAlchemy)
--

3. We're primarily going to be working with only the auth section today.

(Forms Section)
-- add login route to auth blueprint (remember to remove it from main routes)
-- polish/finish signup.html
-- pip install flask-wtf (remember to pip freeze when you add new pip installs to venv)
-- create forms.py in auth, create UserCreationForm
-- on auth.routes import the form on the signup route
-- Add SECRET_KEY to .env for security (rememeber to update your config file)
-- Add form inputs on signup.html (also, add form.hidden_tag() at the top of form)
-- GET/POST requests
-- import request on auth.routes

(Models Section)
-- create models.py on root level of app
-- pip install flask-sqlalchemy
-- Create User & Post Models
-- On auth.routes instantiate/add the User

(Database Section)
-- create new instance on ElephantSQL
-- add DATABASE_URL to .env (rememeber to add 'ql' after 'postgres')
-- update config file. (The Variable name must be 'SQLALCHEMY_DATABASE_URI' when using SQLAlchemy)
-- pip install flask-migrate, psycopg2 (MAC:psycopg2-binary)
-- add migrate,db imports to __init__.py
-- initialize our database to work with our Database
-- import models
-- migrate models to database
(Terminal Commands to migrate) 
(flask db init,flask db migrate,flask db upgrade)

4. Redirect from signup to login
-- import redirect, url_for on auth.routes