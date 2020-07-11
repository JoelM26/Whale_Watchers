from flask import Flask, jsonify
import numpy as np
import pandas as pd
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from datetime import datetime
from sqlalchemy import inspect

engine = create_engine("sqlite:///whale_watching.sqlite")

# reflect an existing database into a new model
Auto = automap_base()
# reflect the tables
Auto.prepare(engine, reflect=True)

print(Auto.classes)
insp = inspect(engine)
print(insp.get_table_names())
print(insp.get_columns('whale_table'))

ta = Auto.classes.whale_table

# Create our session (link) from Python to the DB
session = Session(engine)

q = session.query(ta).all()

def js(query):
    q_list = []
    for x in query:
        q_list.append({"id":x.id,
                        "species":x.species,
                        "description":x.description,
                        "latitude":x.latitude,
                        "longitude":x.longitude,
                        "location":x.location,
                        "sighted_at":x.sighted_at,
                        "orca_type":x.orca_type,
                        "orca_pod":x.orca_pod,
                        "date":x.date,
                        "time":x.time,
                        "month":x.month,
                        "year":x.year,
                        "hour":x.hour,
                        "year_month":x.year_month})
    return q_list


# Flask Setup
app = Flask(__name__)

#Define Base Route
@app.route("/")
def welcome():
    return (
        f"Whale Watchers<br/>"

    )

@app.route("/api/v1.0/json")
def precipitation():
    # for x in q:
    #     q_list.append({"id":x.id,
    #                     "species":x.species})

    # return jsonify(q_list)
    return jsonify(js(q))

@app.route("/api/v1.0/stations")
@app.route("/api/v1.0/tobs")
@app.route("/api/v1.0/<st_dt>")
@app.route("/api/v1.0/<st_dt>/<en_dt>")
def test():
    return "test"
        
if __name__ == "__main__":
    app.run(debug=True)
