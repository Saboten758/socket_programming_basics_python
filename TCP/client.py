import socket
localip="localhost"
port=12345
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.connect((localip,port))
data=s.recv(1024)
print(f"MESSAGE FROM SERVER:\n{data.decode('utf-8')}")
x=str.encode(input("REPLY:"))
s.send(x)
s.close()