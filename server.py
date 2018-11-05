import socket
import nltk
from textAnalysis import TextPosTagger

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 9000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(100)
    print("Waiting for a client")
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 65535 bytes
        #print("I'm listening")
        data = conn.recv(65535).decode()
        #if not data:
            # if data is not received break
            #continue
        print("from connected user: " + str(data))
        #data = input(' -> ')
        text=str(data)
        data= TextPosTagger(str(data))
        
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
