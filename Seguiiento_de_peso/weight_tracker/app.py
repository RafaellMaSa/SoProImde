import re
import sqlite3
from tkinter.tix import NoteBook
from flask import Flask,render_template, request, redirect
from user import init_db, add_user, get_users, add_measurement, get_measurements
from datetime import date, datetime

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()
        age = request.form['age']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        if not name:
            return "Name is required", 400
        try: 
            age = int(age) if age else None
            height = float(height) if height else None
            weight = float(weight) if weight else None
        except ValueError:
            return "Invalid numeric input", 400
        
        add_user(name, age, gender, height, weight)
        return redirect('/')
    return render_template('register.html')

@app.route('/users')
def users():
    all_users = get_users()
    return render_template('users.html', users=all_users)

@app.route('/add_measurement', methods=['GET', 'POST'])
def add_measurement_route():
    users = get_users()
    if request.method =='POST':
        user_id = request.form['user_id']
        date = request.form['date']
        if not date:
            date = datetime.now().strftime('%Y-%m-%d %H:%M')
        weight = request.form['weight']
        waist = request.form['waist']
        notes = request.form['notes'].strip()

        try:
            user_id = int(user_id)
            weight = float(weight)
            waist = float(waist) if waist else None
        except ValueError:
            return "Invalid numeric input", 400
        
        add_measurement(user_id, date, weight, waist, notes)
        return redirect(f'/measurements/{user_id}')
    return render_template('add_measurement.html', users=users)

@app.route('/measurements/<int:user_id>', methods = ['GET'])
def measurements(user_id):
    user_measurements = get_measurements(user_id)
    users = get_users()
    user_name = next((u[1] for u in users if u[0] == user_id),"Unknown User")

    dates = [m[0] for m in user_measurements] if user_measurements else[]
    weights = [m[1] for m in user_measurements] if user_measurements else[]

    return render_template('measurements.html', measurements=user_measurements, 
                           user_name=user_name,
                           dates = dates,
                           weights = weights)

@app.route('/measurements/<int:user_id>', methods = ['GET', 'POST'])
def measurements(user_id):
    date = request.form.get('date')
    if not date:
        date = datetime.now().strftime('%Y-%m-%d %H:%m')
    weight = request.form.get('weight')
    waist = request.form.get('waist')
    notes = request.form.get('notes', '').strip()

    try:
        weight = float(weight)
        waist = float(waist) if waist else None
    except ValueError:
        return "Invalid numeric input", 400


    add_measurement(user_id, date, weight, waist, notes)
    return redirect(f'/measurements/{user_id}')

if __name__ == '__main__':
    app.run(debug=True)