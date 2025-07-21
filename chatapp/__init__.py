# /chatapp/__init__.py

from flask import Flask
from .extensions import socketio

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'barline'

    socketio.init_app(app)

    # Importa e registra as rotas do lobby e do chat
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Importa os eventos de tempo real para registrá-los
    from . import events

    return app