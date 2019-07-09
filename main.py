from flask import Flask, request, redirect, render_template

import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_user_signup_form():
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup():
  username = request.form['username']
  password = request.form['password']
  verify_pw = request.form['verify_pw']
  email = request.form['email']

  username_error = ''
  password_error = ''
  verify_pw_error = ''
  email_error = ''
  space = '' 

  if len(username) < 3 or len(username) > 20:
    username_error = "Username must be between 3-20 characters long."
    password = ''
    verify_pw = ''
    email = email

  if len(email) >= 1:
    if "@" not in email or '.' not in email:
      email_error = "Please enter valid email."
      password = ''
      verify_pw = ''

    if len(email) < 3 or len(email) > 20:
      email_error = "Please enter valid email."
      password = ''
      verify_pw = ''

  if len(password) < 3 or len(password) > 20:
    verify_pw_error = "Password must be between 3-20 characters."
    password = ''
    verify_pw = ''

  if verify_pw != password:
    verify_pw_error = "Does not match password."
    password = ''
    verify_pw = ''


  if not username_error and not password_error and not verify_pw_error and not email_error:
    username = username
    return redirect('/welcome?username={0}'.format(username))
  else:
    return render_template('signup.html', title="Registration Form",
    username=username, username_error=username_error,
    password=password, password_error=password_error,
    verify_pw=verify_pw, verify_pw_error=verify_pw_error,
    email=email, email_error=email_error)

@app.route("/welcome", methods=["POST", "GET"])
def welcome():
  username = request.args.get('username')
  return render_template('welcome.html', title="Sign-Up Success", username=username)

if __name__=='__main__':
  app.run(host='localhost', port='3000')