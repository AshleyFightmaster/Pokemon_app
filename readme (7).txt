1. Flask is a full-stack micro framework,
-- combining Frontend(HTML,CSS,JS), Backend(Python,JS,Java, etc.), Database (SQL)

2. MVC (Model View Controller)
-- Model (Database), View (Frontend), Controller (Backend)

3. Virtual Environment
-- A tool that helps to keep dependencies required by different projects separate by 
-- creating isolated python virtual environments for them.
-Mac: 
		-create: python3 -m venv my_venv
		-activate: source my_venv/bin/activate

-Windows:
		-create: python -m venv my_venv
		-activate: my_venv\Scripts\activate

--pip install flask

4. useful pip commands
-- pip install
-- pip uninstall
-- pip list
-- pip freeze
-- NOTE: use pip3 for MAC

5. Requirements.txt
-- pip freeze > requirements.txt
-- Just a text file that includes all of the packages needed for the specific project

6. Basic Flask Structure
-- create run.py
-- import Flask
-- create routes

7. Better Flask Structure
-- Utilizing seperation of concerns
-- create app folder
-- create __init__.py (flask import)
-- routes.py (remember to import routes into __init__.py)

__name__ == '__main__' explanation:
-- It's boilerplate code that protects users from accidentally invoking 
-- the script when they didn't intend to

8. Create templates folder & import render_template
-- flask render_template looks for a folder named "templates" in order to render html documents.

9. Create config.py & .env file 
-- It allows us to set different flask variables
-- Better option than just using terminal bc you would have to re-set variables everytime
-- Remember to pip install python-dotenv to utilize .env file
NOTE: Anytime you do a new "pip install" make sure to update your requirements.txt
(pip freeze > requirements.txt)

10. Jinja2
-- templating language for python
-- for loops, if-else statements
-- routing to different pages
-- template inheritance (extends, include)

11. Blueprints
-- Help structure your application by organizing the logic into subdirectories

12. .gitignore
-- Ignores files/folders to push up to github
(.env, my_venv, __pycache__)