from flask import Blueprint, render_template
from app.models import get_chart_data


main = Blueprint('main', __name__)

@main.route('/')
def chart():
    return render_template('chart.html')

@main.route('/chart-data')
def chart_data():
    return get_chart_data()
