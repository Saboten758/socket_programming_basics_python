import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.settimeout(1)
msg=str.encode("HEHE BOI")
while True:
    s.sendto(msg,('<broadcast>',37000))
    print("MSG SENT!")
    time.sleep(1)