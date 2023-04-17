from flask_app import app, render_template, session, redirect, request
from flask_app.models.painting import Painting


@app.route('/paintings')
def paintings():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('paintings.html', paintings = Painting.get_all())

@app.route('/paintings/new')
def new_painting():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new_painting.html')

@app.route('/paintings/create', methods = ['POST'])
def create_painting():
    print(request.form)
    if not Painting.validate_painting(request.form):
        return redirect('/paintings/new')
    Painting.save(request.form)
    return redirect('/paintings')

@app.route('/paintings/<int:id>')
def show_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id':id}
    return render_template('paintings_show.html', painting = Painting.get_one(data))

@app.route('/paintings/edit/<int:id>')
def edit_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id':id}
    return render_template('paintings_edit.html', painting = Painting.get_one(data))

@app.route('/update/painting', methods=['POST'])
def update_painting():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Painting.validate_painting(request.form):
        return redirect(f"/paintings/edit/{request.form['id']}")    
    print(request.form)
    Painting.update(request.form)
    return redirect('/paintings')

@app.route('/delete/painting/<int:id>')
def delete(id):
    data ={'id':id}
    Painting.destroy(data)
    return redirect('/paintings')
