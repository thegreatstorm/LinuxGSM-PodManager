import argparse


def argument_controller():
    # Plugins may have to been done manual has mods are different per game server.
    parser = argparse.ArgumentParser('Automate your Rust Server!')
    parser.add_argument('--create', help='Create Game Container `os` Required', required=False)
    parser.add_argument('--os', help='Select Docker Image', required=False)
    parser.add_argument('--install', help='Install Docker Image (Value)', required=False)
    parser.add_argument('--list', help='Create Container (Value)', required=False, action='store_true')
    args = parser.parse_args()
    return args