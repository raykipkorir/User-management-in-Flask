from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, current_user, login_required
from authentication import app, db
from authentication.forms import LoginForm, RegisterForm
from authentication.models import User

@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password1.data,
        )
        db.session.add(user)
        db.session.commit()
        if user and user.check_password(attempted_password=form.password1.data):
            login_user(user)
        flash("Account created successfully", category="success")
        return redirect(url_for("home"))
    elif form.errors != {}:
        for error in form.errors.values():
            flash(error, category="danger")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f"You are now logged in as:{current_user}")
            return redirect(url_for("home"))
        else:
            flash("Incorrect username or password", category="danger")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login_page"))


@app.route("/")
@login_required
def home():
    return render_template("home.html")
    