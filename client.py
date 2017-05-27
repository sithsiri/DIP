#This is the client, not the server
#Python 3 compatible
import time
import socket

print("DIP Client super-alpha")

s = socket.socket()         # Create a socket object
host = socket.gethostname() #input("Server hostname: ")
port = int(float(input("Server port: ")))

s.connect((host, port))
print(s.recv(1024))
s.send(bytes(input("Send: "), "utf-8"))
s.close                     # Close the socket when done
print("Connection closed")

time.sleep(5)
