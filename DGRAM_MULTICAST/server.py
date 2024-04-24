import socket
import time
multicast_grp="224.0.23.39"
port=10000

s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,1)
s.settimeout(1)
while True:
    print("SENDING MSG!")
    msg=str.encode("HELLO GUYS")
    s.sendto(msg,(multicast_grp,port))
    time.sleep(1)
