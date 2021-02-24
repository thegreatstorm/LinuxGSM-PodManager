import os
from bin.servers.servers import RustServer, Valheim


class Servers:
    def __init__(self, image=None, app_settings=None, user_input=None, container=None, config_json=None, config_file=None):
        self.image = image
        self.app_settings = app_settings
        self.user_input = user_input
        self.config_json = config_json
        self.container = container

        if image is None:
            self.image = ""
        else:
            self.image = image

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

        if config_file is None:
            self.config_file = ""
        else:
            self.config_file = config_file

    def create(self):
        if self.user_input == "rustserver":
            server = RustServer(app_settings=self.app_settings, image=self.image)
            server.install()
        elif self.user_input == "valheim":
            server = Valheim(app_settings=self.app_settings, image=self.image)
            server.install()
        else:
            print("User Input not in the list.")

    def start(self):
        if self.user_input == "rustserver":
            server = RustServer(app_settings=self.app_settings, image=self.image)
            server.start()
        elif self.user_input == "valheim":
            server = Valheim(app_settings=self.app_settings, image=self.image)
            server.start()
        else:
            print("User Input not in the list.")

    def delete(self):
        command = "docker rm -f {}".format(self.container)
        os.system(command)