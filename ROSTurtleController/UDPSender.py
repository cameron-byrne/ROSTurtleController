import socket
import time

def main ():
    UDP_IP = "64.85.170.130"
    UDP_PORT = 17484
    MESSAGE = b"Hello, World!"

    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    for j in range(10):
        time.sleep(1)
        for i in range(10000):
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

if __name__ == "__main__":
    main()