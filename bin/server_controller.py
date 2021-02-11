
from bin.servers.servers import rustserver, minecraft


def create_game_server(app_settings, game_server):
    if game_server == "rustserver":
        rustserver()
    elif game_server == "minecraft":
        minecraft()
    else:
        print("game_server not in the list.")