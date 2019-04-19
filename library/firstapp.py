from flask import Flask
from flask import render_template
from flask import request
from library.textanalytics import textanalytics as ta

app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'hello world'

@app.route('/')
def main_page():
    name='John'
    return render_template('index.html',name=name)

@app.route('/textanalytics',methods=['POST','GET'])
def textanalytics_page():
    if request.method == 'GET':
        return render_template('forms/textanalytics_form.html')
    elif request.method == 'POST':
        first=request.form['first']
        second=request.form['second']
        commonwords=ta.union(first,second)
        return render_template('forms/textanalytics_form_result.html',first=first,second=second,commonwords=commonwords)
