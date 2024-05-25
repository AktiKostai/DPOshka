from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    count = db.Column(db.String(50))

    def __init__(self, name, count):
        self.name = name
        self.count = count

with app.app_context():
    db.create_all()

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    count = request.form['count']
    employee = Employee(name, count)
    db.session.add(employee)
    db.session.commit()
    return{"session": "Employee added successfully"}

@app.route('/get_employee/<int:id>')
def get_employee(id):
    employee = Employee.query.get(id)
    if employee:
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'count': employee.count
        })
    else:
        return {'error': 'Employee not found'}

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)