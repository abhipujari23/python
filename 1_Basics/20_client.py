import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("127.0.0.1", 9999))

except ConnectionRefusedError:
    print("Server is not running please start the server to connect.")
    exit(0)

message = s.recv(1024)
s.close()

print(message.decode('ascii'))