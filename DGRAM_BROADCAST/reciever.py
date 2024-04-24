import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind(('',37000))
while True:
    msg,addr=s.recvfrom(1024)
    print(f"MESSAGE FROM {addr} :{msg.decode('utf-8')}")