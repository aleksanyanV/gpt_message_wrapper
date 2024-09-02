from http.server import HTTPServer
from app.controllers.message_controller import MessageController

def run(server_class=HTTPServer, handler_class=MessageController, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
