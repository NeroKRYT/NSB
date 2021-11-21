from app import app
from flask import render_template

@app.route('/')
@app.route('/index.html')

def index():
   user = {'username': 'Student'}
   posts = [
      {
         'author': {'username': 'Eugene'},
         'body': 'Oh hi Mark'
      },
      {
         'author': {'username': 'Michel'},
         'body': 'Oh hi Johnny'
      },
      {
         'author': {'username': 'Lion'},
         'body': 'The program is working like it should'
      }
   ]
   return render_template('index.html', title = 'Welcome to Heaven', user = user, posts = posts)
