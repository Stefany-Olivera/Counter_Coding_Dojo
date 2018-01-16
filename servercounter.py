from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "yftg87ingtybfd7t"

@app.route( "/" )
def front_page():
    
    if "counter" not in session:
        session["counter"] = 1
    else:
        session["counter"] += 1
    return render_template( "index.html")

@app.route("/add2")
def add2():
    session["counter"]+=1
    return redirect("/")


# @app.route( "/result", methods = ["POST"] )
# def result():
#     session["counter"] += 1
    
#     return redirect( "/" )

@app.route( "/reset")
def reset():
    session.clear()
    return redirect( "/" )

app.run( debug = True )