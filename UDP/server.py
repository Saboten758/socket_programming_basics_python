import socket
localip="localhost"
port=20000
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.bind((localip,port))
print("UDP SERVER UP AND RUNNING!")
msg,addr=s.recvfrom(1024)
print(f"MESSAGE FROM {addr}: {msg.decode('utf-8')}")
msg=str.encode("HELLO CLIENT")
s.sendto(msg,addr)
s.close()