from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session


app = Flask(__name__, template_folder = "templates")

app.config['SECRET_KEY']="username"

@app.route('/' , methods=['GET','POST'])
def Login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		username = request.form['username']
		birth_month = request.form['birthmonth']
		
		
		login_session['username'] = username
		login_session['birthmonth'] = birth_month
	


		return redirect(url_for('home'))





@app.route('/home',methods=['GET','POST'])
def home():
	if request.method == "GET":
		username = login_session['username']
		return render_template("home.html",username = username)
	else:

		return redirect(url_for('fortune'))

@app.route('/fortune')
def fortune():
	fortunes = ["free pass microfeedback:)","to be meet ta", "to have 1000000 meet coins", "to win 10000000 shekels","to eat pasta in iasa", "to have curfew every day at 12 pm", "to have permission talking yout mother langauge", "to become sari","to meet with messi", "to have free time all day"]
	birth_month = login_session['birthmonth']
	index=len(birth_month)

	chosen_one=fortunes[9]
	if index<10:
		chosen_one=fortunes[index]
	return render_template("fortune.html" , chosen=chosen_one)

	


if __name__ == '__main__':
	app.run(debug=True)













