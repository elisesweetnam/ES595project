import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect( ("http://192.168.0.36/movement/", 80) )

if len(sys.argv) > 1:
    message = ' '.join(sys.argv[1:])
else:
    message = 'hello' # lower case

# send our message to the server
sock.send(message.encode()) # very handy
# receive any response fro mserver
data = sock.recv(4096) # up to 4096
print(data)
sock.close()
