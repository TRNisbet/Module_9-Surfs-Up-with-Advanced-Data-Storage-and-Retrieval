# RAN IN FIRST PART OF THE MODULE
# Import Flask
# from flask import Flask

# # create a new Flask instance called app
# app = Flask(__name__)

# # Create Flask Routes
# @app.route('/')
# def hello_world():
#     return 'Hello World'

# export FLASK_APP=app.py <-Ran in terminal???

# set FLASK_APP=app.py <-Ran in terminal???

# flask run <-Ran in terminal???
#END OF STUFF RAN IN FIRST PART OF THE MODULE 

# The first thing we'll need to import is datetime, NumPy, and Pandas. 
# We assign each of these an alias so we can easily reference them later.
import app
import datetime as dt
import numpy as np
import pandas as pd

# the dependencies we need for SQLAlchemy, 
# which will help us access our data in the SQLite database.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# add the code to import the dependencies that we need for Flask
from flask import Flask, jsonify

# set up our database engine for the Flask application
# in much the same way we did for climate_analysis.ipynb
engine = create_engine("sqlite:///hawaii.sqlite")

# eflect the database into our classes
Base = automap_base()

# Add the following code to reflect the database
Base.prepare(engine, reflect=True)

# We'll create a variable for each of the classes so that 
# we can reference them later, as shown below
session = Session(engine)

#This will create a Flask application called "app."
app = Flask(__name__)


# Notice the __name__ variable in this code. This is a special type 
# of variable in Python. Its value depends on where and how the code 
# is run. For example, if we wanted to import our app.py file into 
# another Python file named example.py, the variable __name__ would 
# be set to example. Here's an example of what that might look like:

# print("example __name__ = %s", __name__)

# if __name__ == "__main__":
#     print("example is being run directly.")
# else:
#     print("example is being imported")

# define the welcome route using the code below
@app.route("/")

# create a function welcome() with a return statement. Add this line to your code:
# Next, add the precipitation, stations, tobs, and temp routes that we'll need for 
# this module into our return statement. We'll use f-strings to display them for our investors:
def welcome():
    return (
        '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')





