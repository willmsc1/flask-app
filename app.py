from flask import Flask
app = Flask(__name__)

@app.route('/')
def helll_world():
	return 'HI MSOE! The time right now is 2:10pm'
