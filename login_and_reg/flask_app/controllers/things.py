from flask_app import app, render_template, session, redirect

@app.route('/things')
def things():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('logout.html')