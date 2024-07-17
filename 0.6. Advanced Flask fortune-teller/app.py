from flask import Flask,render_template
import random


app = Flask(__name__)

@app.route('/home')
def home():
	return render_template("home.html")



@app.route('/fortune')
def fortune():

	fortunes = ["free pass microfeedback","to be meet ta","to have 1000000 meet coins","to win 10000000 shekels","to eat pasta in iasa", "to have curfew every day at 12 pm", "to have permission talking yout mother langauge","to become sari","to meet with messi","to have free time all day"]
	rnd = fortunes[random.randint(0,10)]
	return render_template("fortune.html",rand =rnd)








if __name__ == '__main__':
    app.run(debug=True)
