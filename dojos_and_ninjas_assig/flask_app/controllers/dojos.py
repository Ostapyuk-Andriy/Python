from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

DATABASE = 'dojos_and_ninjas_schema'


@app.route('/')
def index():
    return redirect('dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojo.html', all_dojos = dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def cool_dojo(id):
    data = {
        'id':id
    }
    return render_template('dojo_show.html', dojo=Dojo.get_dojo_with_ninjas(data))

