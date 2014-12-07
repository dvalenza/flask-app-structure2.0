from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask.ext.login import login_required, login_user, logout_user, current_user
from sqlalchemy import select

from ..database import db_session
from ..models import User
from forms import LoginForm, CreateAccForm

from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt()

mod = Blueprint('users', __name__, template_folder='templates',
                       static_folder='static')

@mod.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         user = User.query.filter_by(email = form.email.data.lower()).first()
         if user:
            if user.match_password(form.password.data):
                login_user(user)
                flash('You are successfully logged in.')
                return redirect(url_for('home.home'))
            else:
                flash('Wrong email/password combination. Try again!')
         else:
            flash('No such email exists.')
    if current_user.is_authenticated():
        flash('You are already logged in.')
        return redirect(url_for('home.home'))
    return render_template('users/login.html', form=form)

@mod.route('/newuser', methods=['GET', 'POST'])
def newuser():
    form = CreateAccForm()
    if form.validate_on_submit():
      user = User.query.filter_by(email = form.email.data.lower()).first()    
      if user: #check if email exists
        flash('Email Already Exists!')
      else:
        newAcc=User(form.username.data,form.email.data,form.password.data)
        db_session.add(newAcc)
        db_session.commit()
        login_user(newAcc)
        flash('You are successfully logged in.')
        return redirect(url_for('home.home'))
    return render_template('users/newuser.html', form=form)

@mod.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))
