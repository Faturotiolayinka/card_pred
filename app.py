from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
USERS_FILE = 'users.json'

# Helper to load users
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('register.html', error='User already exists')
        users[username] = {'password': password}
        save_users(users)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('predict'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    prediction = session.get('last_prediction')
    reasons = session.get('last_reasons', [])
    return render_template('dashboard.html', prediction=prediction, reasons=reasons)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'username' not in session:
        return redirect(url_for('login'))
    prediction = None
    reasons = []
    if request.method == 'POST':
        distance_from_home = float(request.form['distance_from_home'])
        distance_from_last_transaction = float(
            request.form['distance_from_last_transaction']
        )
        ratio_to_median_purchase_price = float(
            request.form['ratio_to_median_purchase_price']
        )
        repeat_retailer = request.form['repeat_retailer']
        used_chip = request.form['used_chip']
        used_pin_number = request.form['used_pin_number']

        # Dynamic fraud logic for demo
        is_fraud = False
        if distance_from_home > 100000:
            is_fraud = True
            reasons.append('Distance from home is unusually high.')
        if distance_from_last_transaction > 50000:
            is_fraud = True
            reasons.append(
                'Distance from last transaction is suspiciously high.'
            )
        if ratio_to_median_purchase_price > 10000:
            is_fraud = True
            reasons.append('Purchase price ratio is much higher than normal.')
        if repeat_retailer == '0':
            is_fraud = True
            reasons.append('Transaction is not with a repeat retailer.')
        if used_chip == '0':
            is_fraud = True
            reasons.append('Card chip was not used for this transaction.')
        if used_pin_number == '0':
            is_fraud = True
            reasons.append('PIN was not used for this transaction.')

        if is_fraud:
            prediction = 'Fraud'
        else:
            prediction = 'Not Fraud'
            reasons.append('All values are within normal range.')
        session['last_prediction'] = prediction
        session['last_reasons'] = reasons
        return redirect(url_for('dashboard'))
    return render_template('predict.html', prediction=prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
