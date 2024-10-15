from flask import jsonify
from datetime import datetime, timezone
from app import db

class ChartData(db.Model):
    __tablename__ = 'chart_data'
    label = db.Column(db.String(255), primary_key=True)
    value = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
def get_chart_data():
    result = ChartData.query.order_by(ChartData.created).all()

    labels = [row.label for row in result]
    values = [row.value for row in result]

    return jsonify({'labels': labels, 'values': values})
