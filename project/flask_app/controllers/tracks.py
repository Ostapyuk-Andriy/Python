from flask_app import app, render_template, session, redirect, request, flash
from flask_app.models.track import Track


@app.route('/tracks')
def tracks():
    if 'dj_id' not in session:
        return redirect('/logout')
    return render_template('tracks.html', tracks = Track.get_all())

@app.route('/tracks/new')
def new_track():
    if 'dj_id' not in session:
        return redirect('/logout')
    return render_template('new_track.html')


@app.route('/tracks/create', methods = ['POST'])
def create_track():
    print(request.form)
    if not Track.validate_track(request.form):
        return redirect('/tracks/new')
    Track.save(request.form)
    return redirect('/tracks')

@app.route('/tracks/<int:id>')
def show_track(id):
    if 'dj_id' not in session:
        return redirect('/logout')
    data = {'id':id}
    return render_template('tracks_show.html', track = Track.get_one(data))

@app.route('/tracks/edit/<int:id>')
def edit_track(id):
    if 'dj_id' not in session:
        return redirect('/logout')
    data = {'id':id}
    return render_template('tracks_edit.html', track = Track.get_one(data))

@app.route('/update/track', methods=['POST'])
def update_track():
    if 'dj_id' not in session:
        return redirect('/logout')
    if not Track.validate_track(request.form):
        return redirect(f"/tracks/edit/{request.form['id']}")    
    print(request.form)
    Track.update(request.form)
    return redirect('/tracks')

@app.route('/delete/track/<int:id>')
def delete(id):
    data ={'id':id}
    Track.destroy(data)
    return redirect('/tracks')
