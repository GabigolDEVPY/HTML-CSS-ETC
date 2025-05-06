from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes.login import login_bp
    app.register_blueprint(login_bp)
    
    from app.routes.home import home_bp
    app.register_blueprint(home_bp)
    
    return app