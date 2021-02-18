#!/usr/bin/python3

# Base Imports
import argparse
import os
import shutil
import json
import urllib.request

# Custom Code
from bin.utils.argument_controller import argument_controller
from bin.utils.configuration_controller import config_controller, get_game_config
from bin.server_controller import Servers
from bin.servers.ansible import Ansible


app_settings = {}
# Grabs path where this script was ran.
script_dir = os.path.dirname(os.path.abspath(__file__))
prefix_dir = os.path.abspath(os.path.join(script_dir))

# =============== Arguments =============================
args = argument_controller()
# =============== Arguments =============================

# ================ Configuration Piece ===================
config_settings = config_controller(script_dir, "var/conf/default.conf", "var/conf/local.conf")
app_name = config_settings.get('general', 'app_name')
version = config_settings.get('general', 'version')
description = config_settings.get('general', 'description')
app_settings["app_name"] = config_settings.get('general', 'app_name')
app_settings["version"] = config_settings.get('general', 'version')
app_settings["description"] = config_settings.get('general', 'description')
app_settings["game_list"] = config_settings.get('general', 'game_list')
app_settings["docker_image"] = config_settings.get('docker', 'image')
app_settings["app_dir"] = prefix_dir


# ================ Configuration Piece ===================

print("Welcome to {}".format(app_name))
print(description)
print("<{}>".format(version))
print("========================================================")
print("")

if args.install:
    print("Installing Dockerfile: {1}/var/lib/docker/{0}/Dockerfile".format(app_settings["docker_image"], app_settings["app_dir"]))
    print("--------------------------------------------------------")
    command = "docker build -t storm-pod:latest . -f {1}/var/lib/docker/{0}/Dockerfile".format(app_settings["docker_image"], app_settings["app_dir"])
    os.system(command)
    print("Docker Image Installed: {}:latest".format(app_settings["docker_image"]))

if args.start and args.start is not None:
    print("Starting Game Server")
    print("--------------------------------------------------------")
    user_input = args.start
    if args.config and args.config is not None:
        config_file = args.config
        game_config = get_game_config(config_file)
        if args.container and args.container is not None:
            container = args.container
            ansible_vars = Ansible(config=game_config)
            ansible_vars = ansible_vars.convert_config_json()
            server = Servers(user_input=user_input, container=container, config_json=ansible_vars)
            server.start()
        else:
            print("No container id Provided. --container=\"<id/name>\"")
            exit(1)
    else:
        print("Make sure you use --config <config-file>")

if args.create and args.create is not None:
    print("Creating Docker Container")
    print("--------------------------------------------------------")
    user_input = args.create
    server = Servers(app_settings=app_settings, user_input=user_input)
    server.create()

if args.delete and args.delete is not None:
    user_input = args.delete
    print("Deleting Docker Container: {}".format(user_input))
    print("--------------------------------------------------------")
    if args.container and args.container is not None:
        container = args.container
        server = Servers(container=container)
        server.delete()
    else:
        print("No container Provided. --container=\"<id>\"")
        exit(1)

if args.list:
    print("Game Server Containers List")
    print("Make sure you keep me updated do a git pull!")
    print("--------------------------------------------------------")
    game_list = app_settings["game_list"]
    game_list = game_list.split(',')
    for game in game_list:
        print(game)

