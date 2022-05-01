import socket

def main ():
    UDP_IP = "192.168.1.91"
    UDP_PORT = 17484

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    count = 0
    while True:
        data, addr = sock.recvfrom(16384)  # buffer size is 1024 bytes
        if data is not None:
            count += 1
            print(count)

if __name__ == "__main__":
    main()