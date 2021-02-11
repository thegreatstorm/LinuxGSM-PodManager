#!/usr/bin/python3

# Base Imports
import argparse
import os
import shutil
import json

# Custom Code
from bin.utils.argument_controller import argument_controller
from bin.utils.configuration_controller import config_controller
from bin.server_controller import create_game_server


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
app_settings["game_list"] = config_settings.get('general', 'game_list')
app_settings["app_name"] = config_settings.get('general', 'app_name')
app_settings["version"] = config_settings.get('general', 'version')
app_settings["description"] = config_settings.get('general', 'description')
app_settings["app_dir"] = prefix_dir


# ================ Configuration Piece ===================

print("Welcome to {}".format(app_name))
print(description)
print("<{}>".format(version))
print("========================================================")
print("")

if args.install:
    if args.install is not None:
        user_input = args.install
        print("Installing Dockerfile: {1}/playbooks/{0}/Dockerfile".format(user_input, app_settings["app_dir"]))
        print("--------------------------------------------------------")
        command = "docker build -t {0}:latest . -f {1}/playbooks/{0}/Dockerfile".format(user_input, app_settings["app_dir"])
        os.system(command)
        print("Docker Image Installed: {}:latest".format(user_input))

if args.create:
    if args.create is not None:
        print("Creating Docker Container")
        print("--------------------------------------------------------")
        user_input = args.create
        create_game_server(app_settings, user_input)

if args.list:
    print("Docker Containers List")
    print("--------------------------------------------------------")
    for x in os.listdir('{}/playbooks/'.format(prefix_dir)):
      print(x)
    print(" ")
    print("Game Server Containers List")
    print("--------------------------------------------------------")
    game_list = app_settings["game_list"].split(',')
    for x in game_list:
        print(x)