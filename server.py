import socket
import sys

def main():
 
HOST = '' 
PORT = 5555 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
    
except socket.error as e:
    print('Bind failed. Error Code : ' + str(e[0]))
    sys.exit()

s.listen(5)	

while True:
	conn, addr = s.accept()
	exec.log("Client connected.")
	
	while True:
	
        data = conn.recv(2048)
		if not data:
            continue
		exec.log("Received command: %s" % data)
		
		if data == "exit":
                exec.log("Client asked server to quit")
                conn.send(data)
                conn.close()
                return
				
		exec.log("Executing command: %s" % data)
		try:
                exec(data)
            except Exception, err:
                test.log("Error occured while executing command: %s" % (
                        data), str(err))
						
s.close();


