from flask import Flask, request  #  import Flask

app = Flask(__name__)  # Create a Flask application instance
# creat an object of Flask class
@app.route("/")  # Define a route for the root
def home():  # Define a view function for the route
    return "Hello, World! This is my first flask app "  # Return a simple response
    
    #  go to terminal and run the command 
    # set  virtual environment 
    # python -m venv venv
    # .\venv\Scripts\activate
    # pip install flask
    # to run the app
    # flask run
    
    
    # Running on http://127.0.0.1:5000
    # http comunition protocol
    # 127.0.0.1 is localhost
    # 5000 is port number
    # to stop the server ctrl + c
@app.route("/about")  # Define a route for /about  # Running on http://127.0.0.1:5000/about
def about():
    return "this is about"

@app.route("/contact")  # Define a route for /contact  # Running on http://127.0.0.1:5000/contact
def contact():
    return "this is contact"


@app.route("/submit",methods =["GET","POST"])
def submit():
    if request.method == "POST":
        return "You send the data"
    else:
        return "You are only viewing the form"