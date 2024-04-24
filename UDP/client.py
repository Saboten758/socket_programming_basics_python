import socket
localip="localhost"
port=20000
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.connect((localip,port))
msg=str.encode("HELLO SERVER")
s.send(msg)
msg,addr=s.recvfrom(1024)
print(f"MESSAGE FROM {addr}: {msg.decode('utf-8')}")
s.close()