import socket
from sdes import sdes_decrypt

HOST = '127.0.0.1'
PORT = 65432

key = "1010000010"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("Cloud is waiting for data...")
    conn, addr = s.accept()

    with conn:
        print("Connected by", addr)
        data = conn.recv(1024).decode()

        print("Encrypted Received:", data)

        decrypted = sdes_decrypt(data, key)
        print("Decrypted Data:", decrypted)
