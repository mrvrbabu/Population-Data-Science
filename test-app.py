from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:talktome@192.168.0.169:5432/worldpopulation'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


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
    app.run(host='0.0.0.0', port='8080', debug=True)
