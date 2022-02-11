'''
Author: BDFD
Date: 2022-02-03 15:32:30
LastEditTime: 2022-02-04 15:06:29
LastEditors: BDFD
Description: 
FilePath: \Heroku_Python_Template\server.py
'''
# from crypt import methods
# from pickle import TRUE
# from unittest import result
# from uuid import RESERVED_FUTURE
from flask import Flask, render_template, request, redirect
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY']= 'bdfd2005'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/blog')
def blog():
  posts = [
    {'title':'Technology in 2019', 'author':'avi'},
    {'title':'China is stronger than ever', 'author':'david'}
  ]
  return render_template(
    'blog.html', 
    author = 'bdfd', 
    sunny = True, 
    posts=posts)

@app.route('/signup', methods=['GET','POST'])
def signup():
  form = SignUpForm()
  if form.is_submitted():
    result = request.form
    print('Hello World, result is',result)
    return render_template('user.html', result=result)
  return render_template('signup.html', form=form)

if __name__ == '__main__':
  app.run()
