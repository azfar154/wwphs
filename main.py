from flask import Flask,render_template,flash,redirect,url_for
from flaskproject import app,db,bcrypt
from flaskproject.models import User
from flaskproject import sources_gms,sources_hs
from flaskproject.forms import RegistrationForm,LoginForm
from flask_login import login_user, current_user, logout_user, login_required
@app.route("/")
def home():
    return render_template('home.html')
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
@app.route("/sourcesgms/")
def sources_for_gms():
    return render_template('data.html',data=sources_gms)
@app.route('/sourceshss/')
def sources_for_hss():
    return render_template('data.html',data=sources_hs)
@app.route('/calendar/')
def calendar():
    return render_template('calendar.html')
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')