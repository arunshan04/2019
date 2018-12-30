from flask import Flask,render_template
import pandas as pd

app=Flask('application')
@app.route('/data')
def data():
    data=pd.read_json('data.json')
    return str({"records":str(len(data)),"page":1,"total":str(len(data)/10),"rows":list(data.rows)}).replace("'",'"')

@app.route('/')
def user():
    return render_template('index.html')
app.run()