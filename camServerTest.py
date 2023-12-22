import socket
import cv2
import time

UDP_IP = "172.17.0.1"
UDP_PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # time.sleep(3)

    if frame is not None:
        d = frame.flatten()
        s = d.tostring()

    for i in range(20):
        sock.sendto(s[i*46080:(i+1)*46080], (UDP_IP, UDP_PORT))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break