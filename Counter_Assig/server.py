from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app. secret_key = "I like apples"

@app.route('/')          
def routeTimes():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")
    
@app.route('/destroy_session')          
def destroySession():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    



