from flask import Blueprint, Flask

def createAPP():
    app = Flask(__name__)
    
    from app.routes.cliente import cliente_bp
    app.register_blueprint(cliente_bp) 
    
    return app