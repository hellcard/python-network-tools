import socket, sys

try:
    host_target = sys.argv[1]
    port_target = int(sys.argv[2])
except IndexError:
    print('Please, enter:\n $ python3 UDP-client.py <host> <port>')
    exit(-1)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # af_inet = use IPv4 ; sock_dgram = use UDP socket

client.sendto(b'hello from UDP-client :)')

response = client.recv(4096)

print(response.decode())
client.close()