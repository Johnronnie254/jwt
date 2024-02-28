from flask import Flask
from extensions import db, jwt
from auth import auth_bp
from users import users_bp

def create_app():
    app = Flask(__name__)

    
    
    app.config.from_prefixed_env()
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_ECHO'] = True

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')


    return app
