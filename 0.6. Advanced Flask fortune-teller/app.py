from flask import Flask, render_template, request, redirect, url_for
import random	

app = Flask(__name__, template_folder = "templates")

@app.route('/home', methods=["GET", "POST"])
def home():
	if request.method == 'GET':
		return render_template("hello.html")
	else:
		birth_month = request.form['birthmonth']
		return redirect(url_for('fortune', birth_month=birth_month))	

@app.route('/fortune/<birth_month>')
def fortune(birth_month):
	fortunes = ["free pass microfeedback:)","to be meet ta", "to have 1000000 meet coins", "to win 10000000 shekels","to eat pasta in iasa", "to have curfew every day at 12 pm", "to have permission talking yout mother langauge", "to become sari","to meet with messi", "to have free time all day"]
	index=len(birth_month)
	chosen_one=fortunes[9]
	if index<10:
		chosen=fortunes[index-1]
	return render_template("fortune.html" , chosen=chosen_one)

	


if __name__ == '__main__':
	app.run(debug=True)













