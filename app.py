from flask import *
app = Flask(__name__)
@app.route("/")
def login():
	return render_template("login.html")
	
@app.route("/registration")
def registration():
	return render_template("registration.html")
	
if __name__ == '__main__':
	app.run(debug = True)		
	
	
