from flask import Flask, render_template

def create_app(): 
    app = Flask(__name__)
    title = "Task tracker LP26 project"
    message = "Project is still in progress"
    app.config.from_pyfile('config.py')    
    @app.route('/')
    def index(): 
        return render_template('index.html', title=title, message=message)
    return app

