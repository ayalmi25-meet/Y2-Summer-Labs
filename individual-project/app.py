from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder = "/home/student/Documents/GitHub/Y2-Summer-Labs/individual-project/templates",static_folder="static")
app.config['SECRET_KEY'] = 'super-secret-key'


# need to change this when there is wifi!!
firebaseConfig = {
	"apiKey": "AIzaSyD1AumZXyg9Wh_oT57OBPjuo--zhDLaE9M",
  "authDomain": "mccabi-haifa-real.firebaseapp.com",
  "projectId": "mccabi-haifa-real",
  "storageBucket": "mccabi-haifa-real.appspot.com",
  "messagingSenderId": "895334542168",
  "appId": "1:895334542168:web:f0792173f8e291506a932d",
 	"measurementId": "G-RKHRMFHG55",
  "databaseURL":"https://mccabi-haifa-real-default-rtdb.europe-west1.firebasedatabase.app/"
}









firebase = pyrebase.initialize_app(firebaseConfig) 
auth = firebase.auth()
db = firebase.database()

@app.route('/',methods = ['GET','POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		user = auth.sign_in_with_email_and_password(email, password)
		login_session['user'] = user
		return redirect(url_for('verf'))

	else:
		return render_template("login.html")
	



@app.route('/signup',methods = ['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template("signup.html")

	else:
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		fav_player = request.form['fav_player']

	
		login_session['user'] = auth.create_user_with_email_and_password(email, password)
		user_UID=login_session['user']['localId']
		db.child('users').child('user_UID').set({"username":username,"password":password,"fav_player":fav_player,"email":email})
		return redirect(url_for('home'))
	


@app.route('/verification',methods = ['GET','POST'])
def verf():
	if request.method == 'GET':
		return render_template("verification.html")

	else:
		favplayer = request.form['fav_player']
		ogfav=db.child('users').child('user_UID').child("fav_player").get().val()
		if favplayer == ogfav:
			return redirect(url_for('home'))

		else:
			problem = "the player you wrote is not your favorite, are you sure you are the real user?"
			return render_template("verification.html",problem = problem)




@app.route('/home',methods=['GET','POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html")

	else:
		if request.args.get("f")== 'f1':
			return redirect(url_for('players'))

		elif request.args.get("f")== 'f2':
			return redirect(url_for('rewards'))

		elif request.args.get("f")== 'f3':
			return redirect(url_for('history'))

		elif request.args.get("f")== 'f4':
			return redirect(url_for('reviews'))


@app.route('/players',methods = ['GET','POST'])
def players():
	if request.method == 'GET':
		return render_template("players.html")

	else:
		return redirect(url_for('home'))




@app.route('/rewards',methods = ['GET','POST'])
def rewards():
	if request.method == 'GET':
		return render_template("reward.html")

	else:
		return redirect(url_for('home'))




@app.route('/history',methods = ['GET','POST'])
def history():
	if request.method == 'GET':
		return render_template("history.html")

	else:
		return redirect(url_for('home'))



@app.route('/reviews',methods=['GET','POST'])
def reviews():
	if request.method == 'GET':
		return render_template("reviews.html")

	else:
		experience = request.form['experience']
		improve = request.form['improve']
		comment = request.form['comment']

		if experience==None or improve==None or comment==None:
			problem = "sorry, please fill all the form"
			return render_template("reviews.html",problem=problem)
		else:
			review = {"experience":experience,"improve":improve,"comment":comment}
			db.child('reviews').push(review)
			return redirect(url_for('thanks'))



@app.route('/thanks',methods = ['GET','POST'])
def thanks():
	if request.method == 'GET':
		return render_template("thanks.html")

	else:
		return redirect(url_for('login'))










if __name__ == '__main__':
	app.run(debug=True)