import socket
multicast_grp="224.0.23.39"
port=10000

s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.bind(('',port))
mreq=socket.inet_aton(multicast_grp)+socket.inet_aton('0.0.0.0')
s.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)
while True:
    msg,addr=s.recvfrom(1024)
    print(f"MESSAGE FROM {addr}:{msg.decode('utf-8')}")