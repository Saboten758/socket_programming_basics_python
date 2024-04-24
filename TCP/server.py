import socket
localip="localhost"
port=12345
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.bind((localip,port))
s.listen(5)
conn,addr=s.accept()
print(f"{addr} is now connected to server")
print("SENDING HELLO!")
msg=str.encode(f"HELLO {addr}, Thanks for connecting to the server!")
conn.send(msg)
data=conn.recv(1024)
print(f"REPLY FROM {addr}:{data.decode('utf-8')}")
s.close()