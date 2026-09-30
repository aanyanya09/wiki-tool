from flask import Flask, render_template

app = Flask(__name__)

# Loads your login page at the main web address
@app.route('/')
def login_page():
    return render_template('index.html') 

# Loads your registration page at /register
@app.route('/register')
def register_page():
    return render_template('register')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
