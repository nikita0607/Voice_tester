import socket
import consts

from threading import Thread


class Server(socket.socket):

    def __init__(self):
        super().__init__()

        self.adress = consts.SERVER_ADRESS
        self.run = True

    def start(self):
        Thread(target=self._start, daemon=True).start()

    def _start(self):

        self.bind(self.adress)
        self.listen(1)

        while self.run:
            sock, adr = self.accept()

            Thread(target=self._listen_client, args=(sock, adr), daemon=True).start()

    def _listen_client(self, sock: socket.socket, adr):

        try:
            while self.run:
                msg = sock.recv(1024).decode()

                if msg == "ping":
                    sock.send("pong".encode())

                elif msg == "disconnect":
                    break
        except Exception as ex:
            print("Excpetion:", ex)
            

if __name__ == '__main__':
    server = Server()
    server.start()

    while 1:
        pass