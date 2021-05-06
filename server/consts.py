from socket import gethostname, gethostbyname_ex

SERVER_ADRESS = ("localhost", 25565) # (gethostbyname_ex(gethostname())[-1][0], 25565)