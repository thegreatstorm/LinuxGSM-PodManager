from subprocess import check_output, Popen
import socket
import threading
import os

from bin.utils.system_controller import random_port, random_password


def command_prefix(container, command, user):
    main_command = 'docker exec -u {0} -t {1} sh -c "{2}"'.format(user, container, command)

    return main_command


class RustServer:
    def __init__(self, image=None, container=None, config_json=None):
        self.image = image
        self.container = container
        self.config_json = config_json

        if image is None:
            self.image = ""
        else:
            self.image = image

        if config_json is None:
            self.config_json = ""
        else:
            self.config_json = config_json

        if container is None:
            self.container = ""
        else:
            self.container = container

    def install(self):
        data = {}
        game_port = random_port()
        rcon_port = random_port()
        app_port = random_port()

        command = "docker run -td -p {0}:{0}/udp -p {0}:{0}/tcp -p {1}:{1}/tcp -p {2}:{2}/tcp {3}".format(game_port, rcon_port, app_port, self.image)

        try:
            container_id = check_output(command, shell=True).decode('ascii')
            container_id = container_id.rstrip("\n")

            data["container_id"] = container_id
            data["game_port"] = game_port
            data["rcon_port"] = rcon_port
            data["app_port"] = app_port

            print(str(data))
            # Insert New Record into database.
            commands = []
            commands.append("echo 'echo -e \'Welcome to Storm Pods! Server Port: {} Rcon Port: {} Mobile Port: {} \'' >> /etc/bashrc".format(game_port,rcon_port,app_port))
            commands.append('git clone https://github.com/thegreatstorm/ansiblepods.git /opt/ansiblepods')
            commands.append('ansible-playbook /opt/ansiblepods/linuxgsm/rustserver/requirements.yml')
            commands.append('ansible-playbook /opt/ansiblepods/linuxgsm/rustserver/setup.yml')

            for command in commands:
                command = command_prefix(data["container_id"], command, 'root')
                os.system(command)

        except Exception as e:
            print("Failed to create container: {}".format(str(e)))
            data["status"] = "Failed to create container. {}".format(str(e))

        return data

    def start(self):
        # Needs container id
        command = "ansible-playbook /opt/ansiblepods/rustserver/start.yml --extra-vars '{}'".format(self.config_json)
        command = command.replace('"', '\"')
        print(f'{command}')
        command = command_prefix(self.container, command, 'root')
        print(command)
        os.system(command)
