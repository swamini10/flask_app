from flask import Flask  #  import Flask

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