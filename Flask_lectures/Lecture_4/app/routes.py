from flask import render_template
from app import app
@app.route('/')
@app.route('/aman')
@app.route('/index')
def index():
    duser={'username':'Aman'}
    #return render_template('index.html',title='Home',user=duser)
    return render_template('index.html',user=duser)

