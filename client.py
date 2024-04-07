import socket
from time import time

IP = "127.0.0.1"
PORT = 8080

ONE = 0.1
ZERO = 0.001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((IP, PORT))

output = server.recv(4096).decode()

binaryMsg = ""
print("recieving...")
while not output.endswith("EOF"):
    first = time()
    output = server.recv(4096).decode()
    last = time()
    
    if ((last - first) >= ONE):
        binaryMsg += "1"
    else:
        binaryMsg += "0"
    
server.close()

msg = ""
for i in range(0, len(binaryMsg), 8):
    byte = binaryMsg[i:i+8]
    msg += chr(int(byte, 2))

print(msg)