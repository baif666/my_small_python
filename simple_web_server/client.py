import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} part {}'.format(*server_address))
sock.connect(server_address)

message = b'This is a message and it will be send back'

try:
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        print('Received {!r}'.format(data))
        amount_received += len(data)

finally:
    print('Clean up connection')
    sock.close()
