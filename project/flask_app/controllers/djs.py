from flask_app import app, render_template, redirect, request, bcrypt, session, flash
from flask_app.models.dj import Dj

@app.route('/')
def index():
    return render_template('frontpage.html')

@app.route('/register/dj')
def register_dj():
    return render_template('register_dj.html')


@app.route("/register", methods = ['post'])
def register():
    print(request.form)

    # TODO validate our dj
    if not Dj.validate_dj(request.form):
        return redirect('/register/dj')

    # TODO hash the password
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    print(hashed_pw)
    # TODO save the dj to the database
    dj_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    dj_id = Dj.save(dj_data)
    # TODO log in the dj
    session['dj_id'] = dj_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    # TODO redirect dj to app
    return redirect('/tracks') #recipes


#! READ and VERIFY AKA LOGIN

@app.route('/login', methods=['post'])
def login():
    # TODO see of the email is in our DB
    dj = dj.get_by_email(request.form)
    if not dj:
        flash('invalid credentials')
        return redirect('/')
    # TODO check to see of the password provided matches the password in our DB
    password_valid = bcrypt.check_password_hash(dj.password, request.form['password'])
    print(password_valid)
    if not password_valid:
        flash('ivalid credentials')
        return redirect('/')
    # TODO log in the dj
    session['dj_id'] = dj.id
    session['first_name'] = dj.first_name
    session['last_name'] = dj.last_name
    
    # TODO redirect dj to app
    return redirect('/tracks') #recipes
    
    


#! LOGOUT

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')