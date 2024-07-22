from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder = "/home/student/Documents/GitHub/Y2-Summer-Labs/Authentication-Lab/templates",static_folder="static")
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
  "apiKey": "AIzaSyCWuhy5eb9hl1zC94aqAtUEcqRbw2x8I-s",
  "authDomain": "ayal-s-website.firebaseapp.com",
  "projectId": "ayal-s-website",
  "storageBucket": "ayal-s-website.appspot.com",
  "messagingSenderId": "1085585626944",
  "appId": "1:1085585626944:web:772bb1958e322b37d68ca5",
  "measurementId": "G-62VVZ0RY2D",
  "databaseURL": ""

}


firebase = pyrebase.initialize_app(firebaseConfig) 
auth = firebase.auth()

@app.route('/',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template("signin.html")

	else:
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			login_session["quotes"] = []
			login_session.modified = True
			return redirect(url_for('home'))
		except:
			problem = "something has gone wrong bruh, try again."
			return render_template("signin.html",problem=problem)


@app.route('/signup',methods=['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template("signup.html")
	else:

		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			login_session["quotes"] = []
			login_session.modified = True
			return redirect(url_for('home'))
		except:
			error = "something has gone wrong bruh, try again."
			return render_template("signup.html",error=error)


@app.route('/home', methods=['GET','POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html")
	else:
		if request.args.get("f")== 'f1':
			print(login_session)
			login_session["quotes"].append(request.form['quote'])
			login_session.modified = True
			return redirect(url_for('thanks'))
		else:
			login_session['user'] = None
			auth.current_user = None
			return redirect(url_for('login'))


@app.route('/signout')
def signout():
	return redirect(url_for('signin'))



@app.route('/thanks')
def thanks():
	return render_template("thanks.html")





@app.route('/display')
def display():
	return render_template("display.html",quotess = login_session["quotes"])











if __name__ == '__main__':
	app.run(debug=True)