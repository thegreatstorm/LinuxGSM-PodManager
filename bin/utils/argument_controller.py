import argparse


def argument_controller():
    # Plugins may have to been done manual has mods are different per game server.
    parser = argparse.ArgumentParser('Automate your Game Server\'s!')
    parser.add_argument('--create', help='Create your game server', required=False)
    parser.add_argument('--delete', help='Delete your game server (ID,Name)', required=False, action="store_true")
    parser.add_argument('--start', help='Delete your game server (ID,Name) --config, --container needed.', required=False)
    parser.add_argument('--container', help='Select container (ID,Name)', required=False)
    parser.add_argument('--config', help='You can edit and point using --config="var/lib/confs/rustserver.conf"', required=False)
    parser.add_argument('--install', help='Install Docker Image', required=False, action='store_true')
    parser.add_argument('--list', help='List Game Servers', required=False, action='store_true')
    args = parser.parse_args()
    return args