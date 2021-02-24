#!/usr/bin/python3

# Base Imports
import os

# Custom Code
from bin.utils.argument_controller import argument_controller, arguments
from bin.utils.configuration_controller import config_controller

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

# Start Argument check
arguments(args, app_settings)

