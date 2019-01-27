from flask import Flask, render_template, request, session,redirect,flash,url_for
from Newgoal import *
import functools

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='dev'
)
@app.route('/init')
def init():
    init_db()
    return 'db initialised'
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('Login'))
        return view(**kwargs)
    return wrapped_view


@app.route('/Resgister', methods=('GET', 'POST'))
def Register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        re_password = request.form['re_password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif password != re_password:
            error = 'Password do not match.'
        else:
            Newgoal.create_user(username, password,re_password)
            return redirect(url_for('Login'))
        flash(error)
    return render_template('Resgister.html')

@app.route('/Login',methods=('GET', 'POST'))
def Login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = Newgoal.get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                return redirect(url_for('Saving'))
        flash(error)
    return render_template("Login.html")


@app.route('/Logout')
def Logout():
    session.clear()
    return redirect(url_for('Saving'))

#****Goals*****
@app.route('/Saving')
def Saving():
    if 'id' in session:
        posts = Newgoal.get_goals()
        return render_template('Goal.html', posts = posts)
    else:
        return render_template('base.html')


@app.route('/<string:id>/update', methods=('GET', 'POST'))
def update(id):
    post = Newgoal.get_goal(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            Newgoal.update_goal(post)
            return redirect(url_for('Saving'))

    return render_template('update.html', post = post)

@app.route('/<string:id>/delete', methods=('GET', 'POST'))
def delete(id):
    Newgoal.delete_goal(id)
    posts = Newgoal.get_goals()
    return render_template('base.html', posts = posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        Due = request.form['Due']
        description = request.form['description']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            Newgoal.create_goal(session['user_name'], title, body,Due,description)
            return redirect(url_for('Saving'))

    return render_template('posting.html')

if __name__ == "__main__":
    app.run(debug=True)

