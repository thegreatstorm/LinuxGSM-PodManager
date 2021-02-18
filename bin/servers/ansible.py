import json


class Ansible:
    def __init__(self, config=None, json_config=None, playbook=None, game_type=None):
        self.config = config
        self.json_config = json_config
        self.playbook = playbook
        self.game_type = game_type

        if config is None:
            self.config = ""
        else:
            self.config = config

        if json_config is None:
            self.json_config = ""
        else:
            self.json_config = json_config

        if playbook is None:
            self.playbook = ""
        else:
            self.playbook = playbook

        if game_type is None:
            self.game_type = ""
        else:
            self.game_type = game_type

    def convert_config_json(self):
        json_config = json.dumps(self.config)
        return json_config

    def ansible_command(self):
        command = "ansible-playbook /opt/ansiblepods/{}/{} --extra-vars '{}'".format(self.game_type, self.playbook, self.json_config)
        return command