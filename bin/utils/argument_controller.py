import argparse
import os


from bin.servers import Servers


def argument_controller():
    # Plugins may have to been done manual has mods are different per game server.
    parser = argparse.ArgumentParser('Automate your Game Server\'s!')
    parser.add_argument('--create', help='Create your game server', required=False)
    parser.add_argument('--delete', help='Delete your game server (ID,Name)', required=False, action="store_true")
    parser.add_argument('--container', help='Select container (ID,Name)', required=False)
    parser.add_argument('--install', help='Install Docker Image', required=False, action='store_true')
    parser.add_argument('--list', help='List Game Servers', required=False, action='store_true')

    # Disabled Arguments until we figure out how to get start to work.
    # parser.add_argument('--start', help='Start your game server (ID,Name) --config, --container needed.', required=False)
    # parser.add_argument('--config', help='You can edit and point using --config="var/lib/confs/rustserver.conf"', required=False)
    args = parser.parse_args()
    return args


def arguments(args, app_settings):
    # This was moved from the main file pod-gs.py to prevent constant permission change and deletation of pod-gs.py

    # If the user types in --install
    if args.install:
        print("Installing Dockerfile: {1}/var/lib/docker/{0}/Dockerfile".format(app_settings["docker_image"], app_settings["app_dir"]))
        print("--------------------------------------------------------")
        command = "docker build -t {0}:latest . -f {1}/var/lib/docker/{0}/Dockerfile".format(
            app_settings["docker_image"], app_settings["app_dir"])
        os.system(command)
        print("Docker Image Installed: {}:latest".format(app_settings["docker_image"]))

    '''
    # Haven't figured out how to start the rust server remotely with environment variables, I'm trying to avoid a database to store info.
    if args.start and args.start is not None:
        print("Starting Game Server")
        print("--------------------------------------------------------")
        user_input = args.start
        if args.config and args.config is not None:
            config_file = args.config
            if args.container and args.container is not None:
                container = args.container
                server = Servers(user_input=user_input, container=container, config_file=config_file)
                server.start()
            else:
                print("No container id Provided. --container=\"<id/name>\"")
                exit(1)
        else:
            print("Make sure you use --config <config-file>")
    '''

    # If the user types in --create="<gameserver>"
    if args.create and args.create is not None:
        print("Creating Docker Container")
        print("--------------------------------------------------------")
        user_input = args.create
        server = Servers(app_settings=app_settings, image=app_settings["docker_image"], user_input=user_input)
        server.create()

    # If the user types in --delete --container="<id/name>"
    if args.delete and args.delete is not None:
        if args.container and args.container is not None:
            print("Deleting Docker Container: {}".format(args.container))
            print("--------------------------------------------------------")
            container = args.container
            server = Servers(container=container)
            server.delete()
        else:
            print("No container Provided. --container=\"<id/name>\"")
            exit(1)

    # Gets list of supported server containers --list
    if args.list:
        print("Game Server Containers List")
        print("Make sure you keep me updated do a git pull!")
        print("--------------------------------------------------------")
        game_list = app_settings["game_list"]
        game_list = game_list.split(',')
        for game in game_list:
            print(game)