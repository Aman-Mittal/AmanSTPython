from app import app
@app.route('/')
@app.route('/aman')
@app.route('/index')
def index():
    user={'username':'Aman'}
    skill="Python,C,C++"
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello '''+ user['username']+''' u r skilled in '''+skill+''' </h1>
    </body>
</html>'''

