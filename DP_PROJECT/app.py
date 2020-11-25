
# Importing essential libraries
from flask import Flask, render_template, request,url_for,redirect
from back import *

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		X = request.form['para1']
		Y = request.form['para2']
		if(len(X)==0 or len(Y)==0):
			return render_template('index.html',percent=0)
		else:
			a = lcs(X,Y)
			b = a/max(len(X),len(Y))*100
			percent = str(round(b, 2))
			return render_template('index.html',percent=percent)

if __name__ == '__main__':
	app.run(debug=True)