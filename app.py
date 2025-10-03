from flask import Flask, request, redirect, url_for,session,Response

app = Flask(__name__)  # Create a Flask application instance
app.secret_key = "supersecretkey" # Set a secret key for session management

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "swamini" and password == "swamini@13":
            session["user"] = username #store the user in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials! Please try again.", mimetype="text/plain")
        #  text/html return kare
        
    return'''
    <h2>Login Page</h2>
    <form method="POST">
        username: <input type="text" name="username"><br>
        password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''
    
    
    # weclome page after login
    @app.route("/welcome")
    def Welcome():
        if "user" in session:
            return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href="{url_for("logout")}">Logout</a>
            '''

        return redirect(url_for("login"))

# logout route
@app.route("/logout")
def logout():
    session.pop("user", None)# remove user from session
    return redirect(url_for("login"))