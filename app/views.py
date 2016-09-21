from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'f_name': 'Nat'}
    form = LoginForm
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/feed')
def feed():
    posts = [
        {
            "title": "test",
            "synopsis": "this is the synposis"

        },
        {
            "title": "Post 2",
            "synopsis": "This is the synopsis for post 2"
        }
    ]
    return render_template('feed.html', posts=posts)
