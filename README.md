# JPete Books

A website built with the Flask Python framework, that acts as a basic 'online' library for public domain books.

## Getting started
 The project uses a local virtual environment for development, the steps below are what is used to run the virtual environment
 To use the virtual environment, run the command `.venv\Scripts\activate`
 To exit the environment, run the command `.venv\Scripts\deactivate`

 To ensure that Flask is properly set up, run the command `set FLASK_APP=FlaskSite:main` in order to get localhost to run properly. 
 After that, run the command `flask run` to actually run the localhost environment.

 To note, any changes made to the HTML files will require a page reload to get the changes to appear on the web page
 
 ## Live Environment
 The live / production environment for this app is hosted on Heroku, (here)[https://flask-app-portfolio-jpete.herokuapp.com/]
 
 ## Tech used
 The following tech is used in the project:
 - Flask
 - Bootstrap CSS / Flask-Bootstrap
 - HTML
 - WTForms
 - SQLAlchemy / Flask-SQLAlchemy
 - python-dotenv (to handle local env variables)
