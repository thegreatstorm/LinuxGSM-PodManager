from subprocess import check_output, Popen
import socket
import threading

from bin.utils.system_controller import random_port, random_password


def rustserver():
    data = {}
    game_port = random_port()
    rcon_port = random_port()
    ssh_port = random_port()
    app_port = random_port()

    command = "docker run -td -p {0}:{0}/udp -p {0}:{0}/tcp -p {1}:{1}/tcp -p {2}:{2}/tcp -p {3}:22 rustserver".format(game_port, rcon_port, app_port, ssh_port)

    try:
        container_id = check_output(command, shell=True).decode('ascii')
        container_id = container_id.rstrip("\n")

        data["container_id"] = container_id
        data["game_port"] = game_port
        data["rcon_port"] = rcon_port
        data["ssh_port"] = ssh_port
        data["app_port"] = app_port

        # Insert New Record into database.
        print(str(data))

    except Exception as e:
        print("Failed to create container: {}".format(str(e)))
        data["status"] = "Failed to create container. {}".format(str(e))

    return data