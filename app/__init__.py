from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import students_bp
    app.register_blueprint(students_bp)
    
    return app
