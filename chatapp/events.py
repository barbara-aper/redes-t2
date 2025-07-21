# /chatapp/events.py

from flask import request
from .extensions import socketio
from flask_socketio import emit, join_room, leave_room

# Usamos uma lista para armazenar as salas ativas de forma global e suas senhas
ROOMS = []
Codes = []

@socketio.on("connect")
def handle_connect():
    """
    Envia a lista de salas para um cliente que acaba de se conectar.
    """
    print(f"Cliente conectado: {request.sid}")
    emit("update_room_list", list(ROOMS))

@socketio.on('create_room')
def handle_create_room(room_name, room_code):
    """
    Cria uma nova sala e atualiza a lista para todos os clientes.
    """
    if room_name not in ROOMS:
        ROOMS.append(room_name)
        Codes.append(room_code)
        # broadcast=True garante que todos os clientes recebam a lista atualizada
        emit('update_room_list', list(ROOMS), broadcast=True)
    print(f"Sala criada: {room_name}. Salas atuais: {ROOMS}")

@socketio.on("join")
def handle_join(data):
    """
    Adiciona um usuário a uma sala específica.
    """
    username = data.get('username')
    room = data.get('room')
    
    join_room(room) 
    
    print(f"Usuário {username} entrou na sala {room}")
    
    # Notifica os outros membros da sala sobre a entrada
    # to=room garante que a mensagem vá apenas para esta sala
    emit("chat", {
        "message": f"{username} entrou na sala",
        "username": "System"
    }, to=room)

@socketio.on("leave")
def handle_leave(data):
    """
    Remove um usuário de uma sala.
    """
    username = data.get('username')
    room = data.get('room')

    leave_room(room) # Função chave do SocketIO para sair de uma sala

    print(f"Usuário {username} saiu da sala {room}")

    # Notifica os outros membros da sala sobre a saída
    emit("chat", {
        "message": f"{username} saiu da sala",
        "username": "System"
    }, to=room)

@socketio.on("new_message")
def handle_new_message(data):
    """
    Recebe uma nova mensagem e a retransmite para a sala correta.
    """
    room = data.get('room')
    emit("chat", data, to=room) # Envia a mensagem apenas para a sala correta

@socketio.on("code_required")
def handle_code_required(room_name):
    """
    Verifica se a sala acessada é privada ou não.
    """
    index = ROOMS.index(room_name)
    code = Codes[index]
    answer = []
    answer.append(room_name)

    if code == '':
        answer.append(False)
    else:
        answer.append(True)
    
    emit("code_is_required", answer)

@socketio.on("code_verify")
def handle_code_verify(room_name, room_code):
    """
    Verifica se o código entrado para uma sala é o correto.
    """
    index = ROOMS.index(room_name)
    code = Codes[index]
    answer = []
    answer.append(room_name)

    if code == room_code:
        answer.append(True)
    else:
        answer.append(False)

    emit("code_is_verified", answer)