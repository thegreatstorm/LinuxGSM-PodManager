
from bin.servers.servers import rustserver, minecraft, terraria


def create_game_server(app_settings, game_server, image):
    if game_server == "rustserver":
        rustserver(image)
    elif game_server == "minecraft":
        minecraft(image)
    elif game_server == "terraria":
        terraria(image)
    elif game_server == "valheim":
        terraria(image)
    else:
        print("game_server not in the list.")