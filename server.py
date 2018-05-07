from flask import Flask, render_template, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app= Flask(__name__)
app.secret_key='swag'
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    if len(request.form['first_name'])<1 or len(request.form['last_name'])<1 or len(request.form['email'])<1 or len(request.form['password'])<1 or len(request.form['confirm_password'])<1:
        flash('All sections must be filled out')
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    if hasNumbers(request.form['first_name'])==True or hasNumbers(request.form['last_name'])==True:
        flash('Your name must not contain any numbers')
    if len(request.form['password'])<8:
        flash('Password must be more than 8 characters')
        return redirect('/')
    if request.form['password']!=request.form['confirm_password']:
        flash('Password and confirm password do not match')
    else:	
        print("Got Post Info")
        print (request.form)
        email=request.form['email']
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        pwd=request.form['password']
        confirm_pwd=request.form['confirm_password']
        return render_template('submit.html', first_name=first_name, last_name=last_name)
@app.route('/danger')
def danger():
    print("a user tried to visit /danger. we have redirected the user to /")
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)
