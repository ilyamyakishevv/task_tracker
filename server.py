from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_user(): 
    return "Привет, пользователь!"


if __name__ == "__main__": 
    app.run(debug=True)