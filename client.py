import socket
import threading
import tkinter as tk
from tkinter import simpledialog

class GameClient:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.root = tk.Tk()
        self.setup_gui()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        try:
            self.sock.connect((self.host, self.port))
            print("Connected to the server.")
            threading.Thread(target=self.receive_messages).start()
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def receive_messages(self):
        """
        Handles incoming messages from the server.
        """
        pass  # To be implemented

    def setup_gui(self):
        """
        Sets up the GUI for the client.
        """
        pass  # To be implemented

    def on_send(self):
        """
        Handles sending messages to the server.
        """
        pass  # To be implemented

if __name__ == '__main__':
    client = GameClient()
    client.connect_to_server()
    tk.mainloop()
