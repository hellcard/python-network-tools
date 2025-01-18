import socket, sys, threading

try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
except IndexError:
    print('Plese enter IP and PORT\n $ python3 TCP-server.py <IP> <PORT>')
    exit(-1)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # use IPv4 & TCP-socket
    server.bind((IP, PORT))
    server.listen(4)

    print(f'[+] Listening: {IP} : {PORT}')

    while 1:
        client, addr = server.accept()
        print(f'[+] Accepted connection from: {addr[0]} : {addr[1]}')
        client_handler = threading.Thread(target = handler, args=(client,))
        client_handler.start()

def handler(socket_client):
    with socket_client as s:
        req = s.recv(4096)
        print(f'[+] Recv: {req.decode('utf-8')}')
        s.send(b'good')

if __name__ == '__main__':
    main()