import socket
def sock_create():
    global s
    global ip
    global port
    ip="127.0.0.1"
    port=20001
    try:
        s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    except:
        print("SOCKET CREATION PROBLEM!")

def sock_binding():
    global s
    global ip
    global port
    try:
        s.bind((ip,port))
        s.listen(5)
        print("TCP SERVER UP AND RUNNING")
    except:
        print("SOCKET BINDING ERROR!")

def sock_accept():
    global s
    try:
        while True:
            conn,addr=s.accept()
            print(f"Connection Established with {addr}")
            x=str.encode(input("Send Something"))
            conn.send(x)
            print("Message Sending success!")
            conn.close()
    except:
        print("ERROR!")

def main():
    sock_create()
    sock_binding()
    sock_accept()

if __name__=="__main__":
    main()
