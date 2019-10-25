from tornado import websocket
import tornado.ioloop

PORT = 66666


class EchoWebSocket(websocket.WebSocketHandler):
    clients = set()

    def open(self):
        print('Websocket opened')
        self.clients.add(self)

    def on_message(self, message):
        # Echo message to client
        #  self.write_message(f'Incoming message {message}')
        # Broadcast message to all clients
        [c.write_message(f'{message}') for c in self.clients]

    def on_close(self):
        print("websocket closed")
        self.clients.remove(self)


application = tornado.web.Application([(r"/", EchoWebSocket), ])

if __name__ == "__main__":
    application.listen(66666)
    tornado.ioloop.IOLoop.instance().start()
