import socket
import consts

from time import time


class Client(socket.socket):

    def __init__(self):
        super().__init__()

        self.server_addr = consts.SERVER_ADRESS

    def _connect_to_server(self) -> tuple:
        try:
            self.connect(self.server_addr)
            return (True,)
        except Exception as ex:
            return False, ex

    def _disconnect(self):
        try:
            self.send("disconnect".encode())
        except:
            pass

        self.close()
        super().__init__()

    def _send_str(self, *args, sep=" "):
        send_str = ""
        for i in args:
            send_str += i + sep
        send_str = send_str[:-1]

        self.send(send_str.encode())

    def ping(self):
        _c = self._connect_to_server()

        if not _c[0]:
            return -1

        _t = time()

        self._send_str("ping")

        try:
            self.recv(1024)
        except:
            return -1

        _elapsed_time = time() - _t

        self._disconnect()

        return _elapsed_time


if __name__ == '__main__':
    conn = Client()
    ping_time = conn.ping()

    if ping_time >= 0:
        print("Answer time:", ping_time)
    else:
        print("Unknown error")