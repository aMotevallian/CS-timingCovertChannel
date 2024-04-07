import socket
from time import sleep

ONE = 0.1
ZERO = 0.001
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))


msg = "this is covert channel secret message. " 
binaryMsg = ""
for char in msg:
    asci = ord(char)
    binaryMsg += format(asci, '08b') 

server.listen(0)
client,addr = server.accept()

n = 0
count = 0
while(count < len(binaryMsg)):
        client.send("test".encode())
        if (binaryMsg[n] == "0"):
            sleep(ZERO)
        else:
            sleep(ONE)

        n = (n + 1) % len(binaryMsg)
        count += 1
        
client.send("EOF".encode())
client.close()

