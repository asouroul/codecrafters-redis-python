import socket  # noqa: F401
import threading

def handle_client(connection):
        """Handles a single client"""
        with connection:
            while data := connection.recv(4096):
                _ = data
                connection.sendall(b"+PONG\r\n") # Sends response to client

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment the code below to pass the first stage
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        connection,_ = server_socket.accept() # wait for client
        client_threading = threading.Thread(target=handle_client, args=(connection,))
        client_threading.start()



if __name__ == "__main__":
    main()
