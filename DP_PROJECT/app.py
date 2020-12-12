
# Importing essential libraries
from flask import Flask, render_template, request,url_for,redirect
from back import *

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')                                    ## return index page intially

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		X = request.form['para1']
		Y = request.form['para2']                                       ## take in paras from html page.
		if(len(X)==0 or len(Y)==0):
			return render_template('index.html',percent=0)          ## as nothing is common we give 0 as a parameter
		else:
			a = lcs(X,Y)                                            ## finding LCS b/w them
			b = a/max(len(X),len(Y))*100                            ## using logic for finding percentage
			percent = str(round(b, 2))
			return render_template('index.html',percent=percent)    ## returning percentage to the page back 

if __name__ == '__main__':
	app.run(debug=True)
