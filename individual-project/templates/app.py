from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder = "/home/student/Documents/GitHub/Y2-Summer-Labs/individual-project/templates",static_folder="static")
app.config['SECRET_KEY'] = 'super-secret-key'


# need to change this when there is wifi!!
firebaseConfig = {
  "apiKey": "AIzaSyCWuhy5eb9hl1zC94aqAtUEcqRbw2x8I-s",
  "authDomain": "ayal-s-website.firebaseapp.com",
  "projectId": "ayal-s-website",
  "storageBucket": "ayal-s-website.appspot.com",
  "messagingSenderId": "1085585626944",
  "appId": "1:1085585626944:web:772bb1958e322b37d68ca5",
  "measurementId": "G-62VVZ0RY2D",
  "databaseURL":"https://ayal-s-website-default-rtdb.europe-west1.firebasedatabase.app/"

}









firebase = pyrebase.initialize_app(firebaseConfig) 
auth = firebase.auth()
db = firebase.database()

@app.route('/',methods = ['GET','POST'])
def login():
	if request.methods == 'GET':
		return render_template("login.html")

	else:
		username = request.form['username']
		password = request.form['password']
	try:
		login_session['user'] = auth.create_user_with_email_and_password(email, password)
		user_UID=login_session['user']['localId']
		db.child('users').child('user_UID').set({"username":username,"password":password})
		return redirect(url_for('verf'))
	except:
		problem = "something went wrong bro, try again:)"







