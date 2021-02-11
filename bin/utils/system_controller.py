import socket
import random


def random_port():
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = "0"
    while True:
        port = random.randint(28000, 50000)
        location = ("0.0.0.0", int(port))
        result = a_socket.connect_ex(location)
        if result != 0:
            break

    a_socket.close()
    return port


def random_password():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password_length = 8
    new_password = "".join(random.sample(s, password_length))
    return new_password