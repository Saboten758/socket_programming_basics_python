import socket
def sock_connect():
    global s
    global ip
    global port
    ip="localhost"
    port=20001
    try:
        s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
        s.connect((ip,port))
        sock_send()
    except:
        print("CONNECTION FAULT! SERVER NOT RUNNING?")

def sock_send():
    global s
    global ip
    global port
    try:
            msg=s.recv(1024)
            print(msg.decode())
    except:
        print("CONNECTION CLOSED MAYBE?")

def main():
    sock_connect()

if __name__=="__main__":
    main()