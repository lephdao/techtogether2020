from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

app = Flask(__name__) #instantiate Flask app


app.config['SECRET_KEY'] = 'e76eb715c3abf64888ed6ed73fd92517'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# create Models
# instead of title, replace with category
#
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String())
	category = db.Column(db.String(300), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return f"Post('{self.author}', '{self.category}', '{self.date_posted}')"


@app.route('/')

@app.route('/home')
def home():
	n = random.randint(1, 18)
	posts = Post.query.filter_by(id=n)
	return render_template('home.html', posts=posts, title='Main Blog')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

# this line is to run myweb.py with python3
if __name__ == '__main__':
	app.run(debug=True)
