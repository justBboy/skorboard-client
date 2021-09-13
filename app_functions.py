CONNECTED_USERS_DICT = {}
CONNECTED_CLIENTS_DICT = {}
ROOMS = {}


def connect_user(user):
    CONNECTED_USERS_DICT[user] = user

def connect_client(user):
    CONNECTED_CLIENTS_DICT[user] = user

def get_connected_clients():
    return list(CONNECTED_CLIENTS_DICT.values())

def remove_connected(id):
    try:
        CONNECTED_USERS_DICT.pop(id)
        CONNECTED_CLIENTS_DICT.pop(id)
    except:
        pass