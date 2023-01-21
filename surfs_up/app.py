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
#reference tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link
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
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end <br>
    ''')

# To create the route, add the following code
@app.route("/api/v1.0/precipitation")

#Next, we will create the precipitation() function.
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
# jsonify() can be used to format results into a JSON
# structured file.
# 127.0.0.1:5000/api/v1.0/precipitation

#set up stations route


@app.route("/api/v1.0/stations")
#define stations function
def stations():
    results = session.query(Station.station).all()
    #unravel into an array
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
    #formats list into JSON

#setup temperature route


@app.route("/api/v1.0/tobs")
#define temp_monthly function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#set up statistics route


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# #define statistics function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(
        Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
