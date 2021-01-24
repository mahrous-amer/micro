import socket
import sys

HOST = '0.0.0.0'         # The remote host
PORT = 9898              # The same port as used by the server
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('Could not open socket')
    sys.exit(1)
with s:
    s.sendall(b'Hi')
    data = s.recv(1024)
print('Received', repr(data))
