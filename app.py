# import flask and render_template here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flast app</h1><p>be careful, it's still under construction..."

@app.route('/profile/<name>')
def profile_name(name):
    return "<h1>Welcome to {}\'s profile</h1>".format(name.capitalize())

# @app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
# def pnhh(name, age, favorite_hobby, hometown):
#     namecap = name.capitalize()
#     hobby = favorite_hobby.capitalize()
#     city = hometown.replace('_', ' ').title()[:-2]
#     state = hometown[-2:].upper()
#     home = city+" "+state
#     html1 = "<h1>Welcome to {}\'s profile!</h1> <h3>About {}: </h3>".format(namecap, namecap)
#     html2 = "<b> Age:</b> <ul><li> {} </li></ul>".format(age)
#     html3 = "<b> Favorite Hobby: </b><ul><li> {} </li></ul>".format(hobby)
#     html4 = "<b> Hometown: </b><ul><li> {} </li></ul>".format(home)
#     return html1 + html2 + html3 + html4

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def show_profile(name, age, favorite_hobby, hometown):
    namecap = name.capitalize()
    hobby = favorite_hobby.title()
    city = hometown.replace('_', ' ').title()[:-2]
    state = hometown[-2:].upper()
    home = city+" "+state
    return render_template('profile.html', name=namecap, age=age, favorite_hobby=hobby, hometown=home)

# tell your flask app to run with debug mode on
app.run(debug=True)
