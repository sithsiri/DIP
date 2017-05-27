#This is the server, not the client
#Python 3 compatible
import time
import socket

print("DIP Server super-alpha")

time.sleep(5)

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = int(float(input("Port to run server on: ")))
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send(bytes("Thank you for connecting, send something", "utf-8"))
   print(c.recv(1024))
   c.close()                # Close the connection
print("Connection closed")

time.sleep(5)