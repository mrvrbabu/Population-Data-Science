import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

load_dotenv()  # load variables from .env file into environment

GET_POPULATION = (
    """SELECT * FROM population;"""
)

url = os.environ.get("DATABASE_URL")   # gets variables from environment
connection = psycopg2.connect(url)
app = Flask(__name__)


@app.get('/api/queryall')
def queryall():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_POPULATION)
            person = cursor.fetchall()

    return {
        "person": person
        # "last_name": last_name
    }
