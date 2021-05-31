from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/dashboard', methods=['POST'])
def home():
	if request.method == 'POST':
		admin_pass = '123456'
		user_name = request.form['username']
		user_password = request.form['pass']

		if user_name == 'admin':
			if user_password == admin_pass:
				return '<h1>Welcome to admin Dashboard</h1>'
			else:
				return '<h1>Credentials doesnot match. Please try again</h1>'

		return f'<h3>Hello!!</h3><h1>{user_name}</h1>'
	else:
		return render_template('Day21(home).html', flag = '')
		

@app.route('/login')
def login():
	return render_template('Day21(login).html')

@app.route('/register')
def register():
	return render_template('Day21(register).html')

@app.route('/contact')
def contact():	
	return render_template('Day21(contact).html')

@app.route('/about')
def about():	
	return render_template('Day21(about).html')	

if __name__ == '__main__':
	app.run(debug=True)
