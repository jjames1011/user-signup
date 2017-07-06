from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():
    encoded_error = request.args.get('error')
    return render_template('signup.html',error=encoded_error)



@app.route('/adduser', methods=['POST'])
def add_user():
    user = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    error = ''
#checks if username field is filled out
    if(not user):
        error = 'Please fill in the username.'
        return redirect('/?error=' + error)
    if(' ' in user or len(user) < 3 or len(user) > 20):
        error = 'Usernames can not contain spaces and must be between 3-20 characters long.'
        return redirect('/?error=' + error)
#checks if password field is filled out properly
    if(password.strip()==""):
        error = 'Please fill in the password.'
        return redirect('/?error=' + error)

    if(' ' in password or len(password) < 3 or len(password) > 20):
        error = 'Passwords can not contain spaces and must be between 3-20 characters long.'
        return redirect('/?error=' + error)
#checks if verify field is filled out
    if(verify.strip()==""):
        error= 'Please verify your password.'

        return redirect('/?error=' + error)
#checks if verify field and password field are the same
    if(verify.strip() != password.strip()):
        error = 'Passwords do not match. Please try again.'

        return redirect('/?error=' + error)

    if(len(email)>0):
        if('@' not in email or '.' not in email or len(email)<3 or len(email)>20):
            error = "Not a valid email."
            return redirect('/?error=' + error)



    return render_template('welcome_page.html', username=user)





app.run()
