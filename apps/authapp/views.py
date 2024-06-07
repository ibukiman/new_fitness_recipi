from flask import Blueprint

authapp = Blueprint(
    'authapp',
    __name__,
    template_folder='templates_auth',
    static_folder='static_auth'
)

from flask import render_template,url_for,redirect,flash
from flask_login import login_user
from sqlalchemy import select
from apps.authapp import forms
from apps import models
from apps.recipiapp import db

@authapp.route('/login',methods=['GET','POST'])
def index():
    form = forms.LoginForm()
    if form.validate_on_submit():
        stmt = (select(models.User).filter_by(username=form.username.data).limit(1))
        user = db.session.execute(stmt).scalars().first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect('/main/top')        #url_for('mainapp.index')
        flash('認証に失敗しました')
    return render_template('login.html',form=form)


