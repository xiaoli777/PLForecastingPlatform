from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .Algorithm_test import Predict_Main

# index view function suppressed for brevity

#@app.route('/index')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    predict = Predict_Main()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = predict.date)