from flask import Flask, request, render_template
from datetime import datetime
from calendar import isleap

app = Flask(__name__)

def judge_leap_year(year):
    return isleap(year)

def month_days(year, month):
    days_in_month = [31, 29 if judge_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]

def calculate_days_lived(dob):
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    current_date = datetime.today()
    total_days = (current_date - birth_date).days
    return total_days

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        try:
            days_lived = calculate_days_lived(dob)
            return render_template('result.html', name=name, days_lived=days_lived)
        except ValueError:
            return render_template('index.html', error="Invalid date format. Please enter the date in YYYY-MM-DD format.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)