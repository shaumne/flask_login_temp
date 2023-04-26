from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from db.db import db
import db.models as db_models
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder="./template")
app.secret_key = 'super_secret_key'

# Flask-login initialization
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User loader function for Flask-login
@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        db_client = db()
        user = db_client.execute(select(db_models.User).filter_by(id=user_id)).scalar_one_or_none()
        db_client.close()
        return user
    return None

# Index route
@app.route('/')
def index():
    return render_template('login.html')

# Login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db().scalar(select(db_models.User).filter_by(
            username=request.form['username']))

        if user is not None and check_password_hash(user.password, request.form['password']):
            login_user(user)
            error = ""
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)

# Index route
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


# Register function
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        error = None 
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        user = db_models.User(username=username, password=hashed_password)
        session = db()
        session.add(user)
        try:
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
            error1 = "Username already exists"
            return render_template('register.html', error1=error1)
        flash('Successfully registered', 'success')
        return render_template('login.html')

# Logout function
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
    
