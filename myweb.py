from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__) #instantiate Flask app

app.config['SECRET_KEY'] = 'e76eb715c3abf64888ed6ed73fd92517'

posts = [
	{
		'author': 'Le Dao',
		'content': 'Hy vọng tuần tới bạn sẽ cho mình có nhiều cơ hội hơn để hạnh phúc'
	},
	{
		'author': 'New Moon',
		'content': 'Uống nước, ưu tiên giấc ngủ, ăn đủ chất, bảo vệ cổ họng, đỉnh đầu và lòng bàn chân.'
	}
]

@app.route('/')

@app.route('/home')
def home():
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
