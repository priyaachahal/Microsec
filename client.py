import socket

HOST = ''
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
while True:
    data = raw_input("./webpage.sh www.usec.io Ninja");
    s.send(data);
    if(str == "Exit"):
        break;
s.close();