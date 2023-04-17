from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("read(all).html", users = User.get_all())

@app.route('/user/new')
def add_user():
    return render_template('create.html')

@app.route('/user/create', methods=["POST"])
def create_user():
    print(request.form)
    user=User.save(request.form)
    return redirect(f"/users/{user}")

@app.route("/users/<int:id>")
def get_user(id):
    data = {'id': id}
    return render_template('read(one).html', user = User.get_one(data))

@app.route("/users/edit/<int:id>")
def edit(id):
    data = {'id': id}   
    return render_template('users(edit).html', user = User.get_one(data))

@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/')