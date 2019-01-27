from flask import *
import os
import Newgoal
import functools
from datetime import datetime
from datetime import timedelta
import shelve


app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


#*************************priya*******************************

app.config.from_mapping(
    SECRET_KEY='dev'
)
@app.route('/init')
def init():
    Newgoal.init_db()
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
            Newgoal.create_user(username, password, re_password)
            return redirect(url_for("Login"))
        flash(error)
    return render_template('Resgister.html')

@app.route('/Login' , methods=('GET', 'POST'))
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
                return redirect(url_for("Saving"))
        flash(error)
    return render_template("Login.html")


@app.route('/Logout')
def Logout():
    session.clear()
    return redirect(url_for('Saving'))

#****Goals*****
#
#{%endfor%}
@app.route('/',methods=('POST','GET'))
def Saving():
    if 'id' in session:
        posts = Newgoal.get_goals()
        if request.method == "POST":
            if 'num' in request.form:
                num = request.form['num']
                Newgoal.saveInfo(session['user_name'], num)
                Newgoal.saveMoney(session['user_name'], num)
                Newgoal.GetPercentage(session['user_name'])
        result = Newgoal.getInfo(session['user_name'])
                #Newgoal.saveMoney(session['user_name'], int(amt))

        #percentage = Newgoal.Percentage(session['user_name'])
        # Val = Newgoal.increaseVal(session['user_name'])
        #aim = Newgoal.getGoal(session['user_name'])
        #result = Newgoal.getInfo(session['user_name'])
        return render_template('Goal.html', posts=posts, result = result)

        # return render_template('Goal.html', posts = posts)
    else:
        return render_template('base.html')

@app.route('/<string:id>/Add',methods=('GET', 'POST'))
def Add(id):
    post = Newgoal.get_goal(id)
    if 'num' in request.form:
        num = request.form['num']
        Newgoal.saveInfo(session['user_name'], num)
        Newgoal.saveMoney(session['user_name'], num)
        post.percentage = Newgoal.GetPercentage(session['user_name'])
        Newgoal.update_goal(post)
        redirect(url_for(Saving))

    return render_template('index.html',post = post)







#@app.route('/Data',methods=('POST','GET'))
#def value():




@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        Due = request.form['Due']
        description = request.form['description']
        Newgoal.Save_body(session['user_name'], body)
        Newgoal.get_body(session['user_name'], body)
        value = Newgoal.GetBody(session['user_name'])
        percentage = Newgoal.GetPercentage(session['user_name'])
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            Newgoal.create_goal(session['user_name'], title, body,Due,description,value,percentage)



            return redirect(url_for('Saving'))
    return render_template('posting.html')

@app.route('/<string:id>/update', methods=('GET', 'POST'))
def update(id):
    post = Newgoal.get_goal(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        description =  request.form['description']
        due = request.form['Due']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            post.description = description
            post.Due = due
            Newgoal.update_goal(post)
            return redirect(url_for('Saving'))

    return render_template('update.html', post=post)

@app.route('/<string:id>/delete', methods=('GET', 'POST'))
def delete(id):
    Newgoal.delete_goal(id)
    posts = Newgoal.get_goals()
    return render_template('Goal.html', posts=posts)

'''
 {% for bod in bodies %}
<p><input type="checkbox"></p>
<p class="body" name = 'add'>Amount: {{ bod }}</p>
      {%endfor%}
'''







if __name__ == "__main__": #only run app when script is run directly
    app.run(debug=True)

