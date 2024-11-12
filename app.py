from dash import Dash, html
from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
from loginScript import login
from registration import emailCheck, register

# Set up Flask server and Dash app
server = Flask(__name__)
server.secret_key = 'supersecretkey'  # Needed for session management
app = Dash(__name__, server=server, routes_pathname_prefix="/dashboard/")

# Serve the index page
@server.route('/')
def index():
    return render_template("index.html")

# Serve the login page
@server.route('/login')
def login_page():
    return render_template("login.html")

# Handle form submission and verification
@server.route('/verify-login', methods=["POST"])
def verify_login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Verify the username and hashed password
    myMessage, loggedIn = login(username, password)
    if loggedIn == True:
        session['logged_in'] = True  # Set session flag for login
        return redirect(url_for("dash_page"))
    else:
        # If verification fails, reload the login page with an error message
        return render_template("login.html", message=myMessage)
    
# Serve the register page
@server.route('/register')
def register_page():
    return render_template("register.html")

# Handle form submission and verification
@server.route('/verify-register', methods=["POST"])
def verify_register():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    password = request.form.get("password")
    confPassword = request.form.get("confirmPassword")

    # Verify the username and hashed password
    text, emailVerification = emailCheck(email)
    if emailVerification == True:
        register(name, email, phone, password)
    else:
        # If verification fails, reload the login page with an error message
        return render_template("register.html", message=text)

# Main Dash app page after successful login
@server.route('/app')
def dash_page():
    # Check if the user is logged in
    if not session.get("logged_in"):
        return redirect(url_for("login_page"))

    # Return the Dash layout if the user is logged in
    return app.index()

# Define the Dash layout (only accessible after successful login)
app.layout = html.Div([
    html.H1("Welcome to the Main Dashboard!"),
    html.P("You have successfully logged in.")
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
