from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

clients = {}

@app.route('/')
def index():
    return "Server is running."

@socketio.on('connect')
def handle_connect():
    clients[request.sid] = request.remote_addr
    emit('response', {'message': 'connected to server'})
    print(f"Client connected: {request.remote_addr}")

@socketio.on('disconnect')
def handle_disconnect():
    print(f"Client disconnected: {clients[request.sid]}")
    del clients[request.sid]

@socketio.on('control')
def handle_control(data):
    print(f"Control data received: {data}")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
