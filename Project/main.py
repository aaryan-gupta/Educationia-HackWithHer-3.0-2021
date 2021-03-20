from flask import Flask, render_template, session, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json, pymysql

with open("config.json", "r") as c:
	params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/educationia"
db = SQLAlchemy(app)

class Class_10(db.Model):
	sno = db.Column(db.Integer, primary_key = True)
	clas = db.Column(db.String(5), nullable = False)
	year = db.Column(db.String(4), nullable = False)
	subject = db.Column(db.String(30), nullable = False)
	url = db.Column(db.String(300), nullable = False)
	date = db.Column(db.String(120), nullable=True)

class Class_12(db.Model):
	sno = db.Column(db.Integer, primary_key = True)
	clas = db.Column(db.String(5), nullable = False)
	year = db.Column(db.String(4), nullable = False)
	subject = db.Column(db.String(30), nullable = False)
	url = db.Column(db.String(300), nullable = False)
	date = db.Column(db.String(120), nullable = True)

@app.route("/")
def index():
	return render_template("index.html", params = params)

@app.route("/books")
def books():
	return render_template("books.html", params = params)

@app.route("/sample-paper")
def samplePaper():
	return render_template("SamplePaper.html", params = params)

@app.route("/last-year-paper")
def lastYearPaper():
	return render_template("LastYearPaper.html", params = params)

@app.route("/last-year-paper/<string:clas>/<string:sub>")
def lastYearPaperSubject(clas, sub):
	if clas == "10":
		if (sub == "english"):
			subject = Class_10.query.filter_by(subject = sub).all()
		if (sub == "maths"):
			subject = Class_10.query.filter_by(subject = sub).all()
		if (sub == "science"):
			subject = Class_10.query.filter_by(subject = sub).all()
		if (sub == "social"):
			subject = Class_10.query.filter_by(subject = sub).all()
		if (sub == "hindi"):
			subject = Class_10.query.filter_by(subject = sub).all()
		if (sub == "punjabi"):
			subject = Class_10.query.filter_by(subject = sub).all()
	if clas == "12":
		if (sub == "english"):
			subject = Class_12.query.filter_by(subject = sub).all()
		if (sub == "maths"):
			subject = Class_12.query.filter_by(subject = sub).all()
		if (sub == "physics"):
			subject = Class_12.query.filter_by(subject = sub).all()
		if (sub == "chemistry"):
			subject = Class_12.query.filter_by(subject = sub).all()
		if (sub == "biology"):
			subject = Class_12.query.filter_by(subject = sub).all()
	return render_template("LastYearPaper.html", params = params, subject = subject, clas = clas)

@app.route("/dashboard", methods = ["GET", "POST"])
def dashboard():
	if ("user" in session and session["user"] == params["admin_user"]):
		class10 = Class_10.query.all()
		class12 = Class_12.query.all()
		return render_template("dashboard.html", params = params, class10 = class10, class12 = class12)
	if request.method == "POST":
		username = request.form.get("inputEmail")
		password = request.form.get("inputPassword")
		if (username == params["admin_user"] and password == params["admin_pwd"]):
			session["user"] = username
			# return render_template("dashboard.html", params = params)
			return redirect("/dashboard")
	return render_template("login.html", params = params)

@app.route("/logout")
def logout():
	session.pop("user")
	return redirect("/")

@app.route("/add-paper", methods = ["GET", "POST"])
def addPaper():
	if ("user" in session and session["user"] == params["admin_user"]):
		if (request.method == "POST"):
			clas = request.form.get("txtClass")
			year = request.values.get("txtYear")
			subject = request.values.get("txtSubject")
			url = request.form.get("link")
			# data = request.form
			date = datetime.now()
			if clas == "10":
				paper = Class_10(clas = clas, year = year, subject = subject, url = url, date = date)
			else:
				paper = Class_12(clas = clas, year = year, subject = subject, url = url, date = date)
			db.session.add(paper)
			db.session.commit()
			flash("Paper Uploaded", "success")
			return redirect("/dashboard")
		return render_template("/dashboard.html", params = params)

@app.route("/delete-paper/<string:clas>/<string:sno>", methods = ["GET", "POST"])
def delete(clas, sno):
	if ("user" in session and session["user"] == params["admin_user"]):
		if(clas == "10"):
			clas10 = Class_10.query.filter_by(sno = sno).first()
			db.session.delete(clas10)
		if(clas == "12"):
			clas12 = Class_12.query.filter_by(sno = sno).first()
			db.session.delete(clas12)
		db.session.commit()
	return redirect("/dashboard")

@app.route("/about")
def about():
	return render_template("aboutus.html")

@app.route("/faq")
def faq():
	return render_template("faq.html", params = params)

@app.route("/maths-12")
def maths_12():
	return render_template("maths_12.html", params = params)

@app.route("/physics-12")
def physics_12():
	return render_template("physics_12.html", params = params)

@app.route("/maths-10")
def maths_class10():
	return render_template("maths_class10.html", params = params)

@app.route("/chem-12")
def chem_12():
	return render_template("chem_12.html", params = params)

@app.route("/bio-12")
def bio():
	return render_template("bio.html", params = params)
@app.route("/eng-12")
def eng_12():
	return render_template("eng_12.html", params = params)

@app.route("/comp-12")
def comp():
	return render_template("comp.html", params = params)

@app.route("/economics-12")
def economics():
	return render_template("economics.html", params = params)

@app.route("/eng-10")
def eng_10():
	return render_template("eng_10.html", params = params)
	
@app.route("/pe")
def pe():
	return render_template("pe.html", params = params)

@app.route("/science-10")
def science_10():
	return render_template("science_10.html", params = params)

@app.route("/sst-10")
def sst():
	return render_template("sst.html", params = params)

@app.route("/qrcode1")
def qrcode1():
	return render_template("qrcode1.html", params = params)


@app.route("/qrcode2")
def qrcode2():
	return render_template("qrcode2.html", params = params)

@app.route("/qrcode3")
def qrcode3():
	return render_template("qrcode3.html", params = params)

@app.route("/qrcode4")
def qrcode4():
	return render_template("qrcode4.html", params = params)

@app.route("/qrcode5")
def qrcode5():
	return render_template("qrcode5.html", params = params)

@app.route("/qrcode6")
def qrcode6():
	return render_template("qrcode6.html", params = params)

@app.route("/qrcode7")
def qrcode7():
	return render_template("qrcode7.html", params = params)

@app.route("/qrcode8")
def qrcode8():
	return render_template("qrcode8.html", params = params)	
	
@app.route("/qrcode9")
def qrcode9():
	return render_template("qrcode9.html", params = params)	
	
@app.route("/qrcode10")
def qrcode10():
	return render_template("qrcode10.html", params = params)

@app.route("/qrcode11")
def qrcode11():
	return render_template("qrcode11.html", params = params)

@app.route("/qrcode12")
def qrcode12():
	return render_template("qrcode12.html", params = params)	

@app.route("/payment")
def payment():
	return render_template("ppaypal.html", params = params)	


app.run(debug=True)

