from flask import Flask, render_template  
app = Flask(__name__)   

@app.route("/")
def Welcome():
    return "Welcome!"

@app.route('/play')          
def bluebox():
    return render_template("index.html", times=3 )  

@app.route('/play/<int:x>')
def numPlayed(x):
    return render_template("index.html", times = x)

@app.route('/play/<int:x>/<string:color>')
def numPlayedColor(x, color):
    return render_template("index1.html", times = x, color = color)

if __name__=="__main__":  
    app.run(debug=True)    


