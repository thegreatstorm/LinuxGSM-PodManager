
from bin.servers.servers import rustserver


def create_game_server(app_settings, game_server):
    if game_server == "rustserver":
        rustserver()
    else:
        print("game_server not in the list.")