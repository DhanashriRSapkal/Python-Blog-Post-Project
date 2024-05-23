from flask import *
from flask.templating import render_template
from dbmodule import *

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/AuthorReg")
def reg():
    return render_template("AuthorReg.html")

@app.route("/AuthorLogin")
def log():
    return render_template("Welcome_AuthorLogin.html")

@app.route("/UserReg")
def seconf_func():
    return render_template("UserReg.html")

@app.route("/UserLogin")
def usfunc():
    return render_template("Welcome_UserLogin.html")



@app.route("/AuthorReg",methods=["POST"])
def AuthorReg():
    Id=request.form["Id"]
    Authorname=request.form["Authorname"]
    Password=request.form["Password"]
    Email=request.form["Email"]
    City=request.form["City"]
    t=(Id,Authorname,Password,Email,City)
    Addauthor(t)
    return redirect("/")



@app.route("/UserReg",methods=["POST"])
def UserReg():
    Id=request.form["Id"]
    Username=request.form["Username"]
    Password=request.form["Password"]
    Email=request.form["Email"]
    City=request.form["City"]
    t=(Id,Username,Password,Email,City)
    Adduser(t)
    return redirect("/") 

@app.route("/AuthorLogin",methods=["POST"])
def AuthorLogin():
    Id=request.form["Id"]
    Authorname=request.form["Authorname"]
    Blog=request.form["Blog"]
    t=(Id,Authorname,Blog)
    addpost(t)
    return redirect("/")

@app.route("/UserLogin",methods=["POST"])
def UserLogin():
    Email=request.form["Email"]
    Password=request.form["Password"]
    t=(Email,Password)
    showpost(t)
    return redirect("/")
  
if(__name__=="__main__"):
    app.run(debug=True)
