from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor

simModelPort = 9000

class MyClientProtocol(WebSocketClientProtocol):
    def onConnect(self, response):
        print(f"Connected to server: {response.peer}")

    def onOpen(self):
        print("WebSocket connection open")

        # Send initial message, e.g., requesting parameters
        self.sendMessage("Please provide simulation parameters.".encode('utf-8'))

    def onMessage(self, payload, isBinary):
        # Handle parameters sent by the server and run simulation
        # Send the simulation result file using self.sendMessage(data, isBinary=True) if needed

    def onClose(self, wasClean, code, reason):
        print(f"WebSocket connection closed: {reason}")

if __name__ == '__main__':
    factory = WebSocketClientFactory(f"ws://localhost:{simModelPort}")
    factory.protocol = MyClientProtocol
    reactor.connectTCP("localhost", 9000, factory)
    reactor.run()
