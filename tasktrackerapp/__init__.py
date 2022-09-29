from flask import Flask, render_template

def create_app(): 
    app = Flask(__name__)
    app_title = "Task tracker LP26 project"
    app_message = "Project is still in progress"
    app.config.from_pyfile('config.py')    
    @app.route('/')
    def index(): 
        return render_template('index.html', title=app_title, message=app_message)
    return app

