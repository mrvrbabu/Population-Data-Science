from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2


dbapp = Flask(__name__)

dbapp.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:talktome@192.168.0.169:5432/worldpopulation'

# db = SQLAlchemy(app)


@dbapp.route('/')
def index():
    conn = psycopg2.connect(
        "postgres://postgres:talktome@192.168.0.169:5432/worldpopulation")
    return 'Db connection works'


# @app.route('/queryall')
# def queryall():
#     persons = db.query.all()
#     output = []
#     for person in persons:
#         person_data = {'first_name': first_name, 'last_name': last_name,
#                        'gender': gender, 'date_of_birth': date_of_birth, 'country': country}
#         output.append(person_data)
#     return {"population": output}

# @app.route('/query', methods=['GET'])
# def query_all():
#     people = db.query.all()
#     results = [
#         {
#             "first_name": first_name,
#             "last_name": last_name,
#             "gender": gender,
#             "date_of_birth": date_of_birth,
#             "country": country
#         } for person in people
#     ]
#     return {"count": len(results), "people": results}


if __name__ == "__main__":
    dbapp.run(host='0.0.0.0', port='8081', debug=True)
