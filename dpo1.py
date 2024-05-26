from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'

db = SQLAlchemy(app)

class Materials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    count = db.Column(db.String(50))

    def __init__(self, name, count):
        self.name = name
        self.count = count

with app.app_context():
    db.create_all()

@app.route('/add_materials', methods=['POST'])
def add_employee():
    name = request.form['name']
    count = request.form['count']
    materials = Materials(name, count)
    db.session.add(materials)
    db.session.commit()
    return{"session": "Materials added successfully"}

@app.route('/get_materials/<int:id>')
def get_employee(id):
    materials = Materials.query.get(id)
    if materials:
        return jsonify({
            'id': materials.id,
            'name': materials.name,
            'count': materials.count
        })
    else:
        return {'error': 'Materials not found'}

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)