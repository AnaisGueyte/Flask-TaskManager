from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from model.db import Task, User
from datetime import datetime
from flask_login import LoginManager, login_user, current_user, logout_user


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '7d441kizf2b6176amPM'


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(id=user_id)


#CODE FOR THE FORM

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        print 'dans signup get'
        return render_template('signup.html')
    elif request.method == 'POST':
        try:
            print 'dans signup try'
            mylogin = User()
            mylogin.pseudo = request.form['pseudo']
            mylogin.password = request.form['password']
            print request.form['pseudo']
            print request.form['password']
            mylogin.save()
        except:
            print 'dans signup except'
            flash('oops', 'danger')
            return redirect(url_for('signup'))
        else:
            print 'dans signup else'
            login_user(mylogin)
            flash("Bonjour " + current_user.pseudo + ", voici vos taches !", 'success')
            return redirect(url_for('list'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print 'dans login get'
        return render_template('login.html')
    elif request.method == 'POST':
        try:
            print 'dans login post'
            print request.form['pseudo']
            print request.form['password']
            user = User.objects.get(pseudo = request.form['pseudo'], password = request.form['password'])
        except:
            print 'dans login except'
            flash('oops', 'danger')
            return redirect(url_for('login'))
        else:
            print 'dans login else'
            login_user(user)
            print 'APRES LOGIN USER'
            return redirect(url_for('list'))



@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html', users=User.objects)
    elif request.method == 'POST':
        try:
            mytask = Task()
            mytask.name = request.form['name']
            print mytask.name
            mytask.user = current_user._get_current_object()
            print mytask.user
            mytask.assignee = User.objects.get(id=request.form['assignee'])
            print mytask.assignee
            mytask.date = datetime.strptime(request.form['date'], "%Y-%m-%d")
            print mytask.date
            mytask.save()
        except Exception as e:
            print e
            flash('Oops, try again !', 'danger')
            return redirect(url_for('form'))
        else:
            flash("Nouvelle tache ajoutee", 'success')
            return redirect(url_for('list'))


@app.route('/list')
def list():
    print 'DANS LA METHODE LIST'
    return render_template('list.html', tasks=Task.objects.filter(assignee=current_user._get_current_object()), users=User.objects)


@app.route('/deleteTask', methods=['POST'])
def deleteTask():
    if request.method == 'POST':
        try:
            print 'DANS DELETETASK'
            taskid = request.form['id']
            print taskid
            thetask = Task.objects.get(id=taskid)
            thetask.delete()
        except:
            flash("oops", "danger")
            print "ohoh"
        else:
            print "yessss"
            print taskid
            return jsonify(taskid)





@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)