#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    entry = 'Client started\nEnter the comands:\nINSERT:$NOME:$SEXO:$IDADE, SELECT* , /help or exit'
    print(entry)
    while True:
        entry = input()
        s.sendall(bytes(entry, 'utf-8'))
        data = s.recv(1024)
        print(f'Received:{str(repr(data))}')
        if entry == 'exit':
            break
