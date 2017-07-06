from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/signup')
def signup():

    return render_template('signup.html')




@app.route('/')
def index():
    return redirect('/signup')




app.run()
