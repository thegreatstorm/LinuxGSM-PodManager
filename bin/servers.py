from subprocess import check_output, Popen
import socket
import threading
import os

from bin.utils.system_controller import random_port, random_password


def command_prefix(container, command, user):
    main_command = 'docker exec -u {0} -t {1} sh -c "{2}"'.format(user, container, command)

    return main_command


class Servers:
    def __init__(self, image=None, container=None, config_json=None, app_dir=None, config_file=None, game_server=None):
        self.container = container
        self.config_json = config_json
        self.app_dir = app_dir

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

        if app_dir is None:
            self.app_dir = ""
        else:
            self.app_dir = app_dir

        if config_file is None:
            self.config_file = ""
        else:
            self.config_file = config_file

        if game_server is None:
            self.game_server = ""
        else:
            self.game_server = game_server

    def create(self):
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
            commands.append("echo 'export server_port={}' >> /etc/bashrc".format(game_port))
            commands.append("echo 'export rcon_port={}' >> /etc/bashrc".format(rcon_port))
            commands.append("echo 'export app_port={}' >> /etc/bashrc".format(app_port))
            commands.append("echo 'echo -e \'Welcome to Storm Pods! Server Port: {} Rcon Port: {} Mobile Port: {} \'' >> /etc/bashrc".format(game_port,rcon_port,app_port))
            commands.append('git clone https://github.com/thegreatstorm/ansiblepods.git /opt/ansiblepods > /dev/null')
            commands.append('ansible-playbook /opt/ansiblepods/linuxgsm/requirements/{0}.yml --extra-vars \'game_server={0}\''.format(self.game_server))
            commands.append('ansible-playbook /opt/ansiblepods/linuxgsm/setup.yml --extra-vars \'game_server={}\''.format(self.game_server))
            commands.append('ansible-playbook /opt/ansiblepods/linuxgsm/install.yml --extra-vars \'game_server={}\''.format(self.game_server))
            commands.append('chmod -R 777 /opt')

            for command in commands:
                command = command_prefix(data["container_id"], command, 'root')
                os.system(command)

            print("To access container: docker exec -u {} -it {} /bin/bash".format(self.game_server, container_id))

        except Exception as e:
            print("Failed to create container: {}".format(str(e)))
            data["status"] = "Failed to create container. {}".format(str(e))

        return data

    def start(self):
        # Currently disabled until environment variables figured out.
        command = "docker cp {0} {1}:/home/{2}/lgsm/config-lgsm/rustserver/rustserver.cfg".format(self.config_file, self.container, self.game_server)
        os.system(command)
        command = "ansible-playbook /opt/ansiblepods/linuxgsm/rustserver/start.yml"
        command = command_prefix(self.container, command, 'rustserver')
        print(command)
        os.system(command)

    def delete(self):
        command = "docker rm -f {}".format(self.container)
        os.system(command)
