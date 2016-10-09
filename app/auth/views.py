# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import render_template, redirect, request, url_for, flash
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('用户名或密码无效')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您退出了！ ')
    return redirect(url_for('main.index'))
