from flask import Flask
from .extensions import socketio

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'barline'

    socketio.init_app(app)

    # Importa e registra as rotas das salas de lobby, chat, preenchimento de senha e menu de salas
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Importa os eventos de tempo real para registrá-los
    from . import events

    return app