from app import app
@app.route('/')
@app.route('/aman')
@app.route('/index')
def index():
    return "Hello World!"
