import socket, sys

try:
    host_target = sys.argv[1]
    port_target = int(sys.argv[2])
except IndexError:
    print('Please, enter:\n $ python3 TCP-client.py <host> <port>')
    exit(-1)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af_inet = use IPv4 ; sock_stream = use TC scoket

client.connect((host_target, port_target))

client.send(b'hello from TCP-client :)')

response = client.recv(4096)
print(response.decode())
client.close()