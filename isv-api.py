from flask import Flask
from labkeywrapper import labkeywrapper

app = Flask(__name__)

immunespace_api = labkeywrapper.LabKeyWrapper()


@app.route("/")
def home():
    return


@app.route("/study/<str:study_id>/data")
def get_study_data(study_id):
    return


@app.route("/user")
def get_user():
    return