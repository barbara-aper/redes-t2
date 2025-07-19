# /chatapp/routes.py

from flask import Blueprint, render_template, redirect, url_for
from .events import ROOMS  # Importa a lista de salas do events.py

main = Blueprint('main', __name__)

@main.route('/')
def lobby():
    """
    Renderiza a página inicial (lobby) e passa a lista de salas ativas.
    """
    return render_template("lobby.html", rooms=list(ROOMS))

@main.route("/rooms/<string:username>")
def rooms(username):
    """
    Renderiza a página das salas para um usuário específico.
    """
    if username:
        return render_template("rooms.html", username=username)
    else:
        # Se faltar informação, volta para o lobby
        return redirect(url_for('main.lobby'))

@main.route("/chat/<string:room_name>/<string:username>")
def chat(room_name, username):
    """
    Renderiza a página do chat para uma sala e usuário específicos.
    """
    if room_name in ROOMS and username:
        return render_template("chat.html", room_name=room_name, username=username)
    else:
        # Se faltar informação, volta para o Rooms
        return redirect(url_for('main.rooms', username=username))

@main.route("/code/<string:room_name>/<string:username>")
def code(room_name, username):
    """
    Renderiza a página de solicitação de senha para uma sala e usuário específicos.
    """
    if room_name in ROOMS and username:
        return render_template("code.html", room_name=room_name, username=username)
    else:
        # Se faltar informação, volta para o Rooms
        return redirect(url_for('main.rooms', username=username))