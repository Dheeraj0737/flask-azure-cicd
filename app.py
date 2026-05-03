from flask import Flask, render_template, request, redirect, url_for
from models import db, StrengthLog, CardioLog
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    strength_logs = StrengthLog.query.order_by(StrengthLog.date.desc()).all()
    cardio_logs = CardioLog.query.order_by(CardioLog.date.desc()).all()

    # Stats
    total_cardio_distance = sum(log.distance for log in cardio_logs)
    total_strength_sessions = len(strength_logs)
    total_cardio_sessions = len(cardio_logs)

    return render_template('dashboard.html',
        strength_logs=strength_logs,
        cardio_logs=cardio_logs,
        total_cardio_distance=round(total_cardio_distance, 2),
        total_strength_sessions=total_strength_sessions,
        total_cardio_sessions=total_cardio_sessions
    )

@app.route('/strength', methods=['GET', 'POST'])
def strength():
    if request.method == 'POST':
        log = StrengthLog(
            exercise=request.form['exercise'],
            sets=int(request.form['sets']),
            reps=int(request.form['reps']),
            weight=float(request.form['weight']),
            notes=request.form['notes'],
            date=datetime.now()
        )
        db.session.add(log)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('strength.html')

@app.route('/cardio', methods=['GET', 'POST'])
def cardio():
    if request.method == 'POST':
        log = CardioLog(
            cardio_type=request.form['cardio_type'],
            distance=float(request.form['distance']),
            duration=int(request.form['duration']),
            notes=request.form['notes'],
            date=datetime.now()
        )
        db.session.add(log)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('cardio.html')

@app.route('/delete/strength/<int:id>')
def delete_strength(id):
    log = StrengthLog.query.get_or_404(id)
    db.session.delete(log)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/delete/cardio/<int:id>')
def delete_cardio(id):
    log = CardioLog.query.get_or_404(id)
    db.session.delete(log)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)