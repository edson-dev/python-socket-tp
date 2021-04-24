import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

memory = []
def analize_sintatica(cmd):
    if cmd[0] == 'INSERT' or cmd[0] == '0':
        if cmd[1:]:
            memory.append(cmd[1:])
        print(memory)
        result = "200 OK"
    elif cmd[0] == 'SELECT*' or cmd[0] == '1':
        print(memory)
        result = str(memory)
    elif cmd[0] == '/help':
        result = 'INSERT:OBJECT(Attributes Spited by :) or SELECT*'
    elif cmd[0] == 'exit':
        result = 'exit'
    else:
        result = 'Invalid Comand(type /help to see the comand list)!'
    return bytes(str(result), 'utf-8')

def database(data,addr):
    #print(f'entry{addr}-{data}')
    cmd = data.decode().split(":")
    #print(f'{cmd}')
    return analize_sintatica(cmd)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if data == 'exit':
                break
            response = database(data, addr)
            try:
                conn.sendall(response)
            except socket.error as e:
                print("Client offline!")
                break


