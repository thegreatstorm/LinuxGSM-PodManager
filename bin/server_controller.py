import os
from bin.servers.servers import RustServer


class Servers:
    def __init__(self, app_settings=None, user_input=None, container=None, config_json=None):
        self.image = "linuxgsm"
        self.app_settings = app_settings
        self.user_input = user_input
        self.config_json = config_json
        self.container = container

        if app_settings is None:
            self.app_settings = ""
        else:
            self.app_settings = app_settings

        if user_input is None:
            self.user_input = ""
        else:
            self.user_input = user_input

        if container is None:
            self.container = ""
        else:
            self.container = container

        if config_json is None:
            self.config_json = ""
        else:
            self.config_json = config_json

    def create(self):
        if self.user_input == "rustserver":
            server = RustServer(self.image)
            server.install()
        else:
            print("User Input not in the list.")

    def start(self):
        if self.user_input == "rustserver":
            server = RustServer(container=self.container, config_json=self.config_json)
            server.start()
        else:
            print("User Input not in the list.")

    def delete(self):
        command = "docker rm -f {}".format(self.container)
        os.system(command)