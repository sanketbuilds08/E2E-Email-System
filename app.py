from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from emails import send_email

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Static credentials
VALID_USER = "admin"
VALID_PASS = "1234"

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == VALID_USER and password == VALID_PASS:
        session['logged_in'] = True
        return redirect('/dashboard')
    else:
        return "Invalid credentials"

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template("dashboard.html")

@app.route('/send_mail', methods=['POST'])
def send_mail_route():
    try:
        subject = request.json.get('subject')
        body = request.json.get('message')

        success = send_email(subject, body)
        if success:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'fail'})
    except Exception as e:
        return jsonify({'status': 'fail', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
