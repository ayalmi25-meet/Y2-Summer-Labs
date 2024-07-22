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
  "databaseURL":"https://ayal-s-website-default-rtdb.europe-west1.firebasedatabase.app/"

}





firebase = pyrebase.initialize_app(firebaseConfig) 
auth = firebase.auth()
db = firebase.database()

@app.route('/',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template("signin.html")

	else:
		email = request.form['email']
		password = request.form['password']
		username = request.form['username']
		full_name = request.form['full_name']
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			user_UID=login_session['user']['localId']
			db.child('users').child('user_UID').set({"name":full_name,"username":username,"email":email})
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
			quotewriter = request.form['quotewriter']
			quoteog = request.form['quoteog']
			user_UID=login_session['user']['localId']
			quote = {"text":quoteog,"said_by":quotewriter,"uid":user_UID}
			try:
				db.child('Quotes').push(quote)
			except:
				print("not adding quote to db")

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
	quotess = db.child("Quotes").get().val()
	return render_template("display.html",quotess =quotess)










if __name__ == '__main__':
	app.run(debug=True)