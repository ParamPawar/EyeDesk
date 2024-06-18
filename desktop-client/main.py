import socketio
import pyautogui
import tkinter as tk

sio = socketio.Client()

def connect_to_server():
    sio.connect('http://localhost:5000')
    
def on_connect():
    print('Connected to server')

def on_disconnect():
    print('Disconnected from server')

def send_control_data(event):
    data = {'type': event.type, 'key': event.keysym, 'x': event.x, 'y': event.y}
    sio.emit('control', data)

sio.on('connect', on_connect)
sio.on('disconnect', on_disconnect)

root = tk.Tk()
root.title("EyeDask Client")

connect_btn = tk.Button(root, text="Connect", command=connect_to_server)
connect_btn.pack()

root.bind('<Motion>', send_control_data)
root.bind('<Key>', send_control_data)

root.mainloop()
