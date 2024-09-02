from http.server import BaseHTTPRequestHandler
from app.services.message_service import MessageService
from app.utils.validation import validate_message_request, InvalidRequestError
import json

class MessageController(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == '/message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data)
                validate_message_request(data)

                response_data = MessageService.process_message(data)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode('utf-8'))
            except InvalidRequestError as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Internal server error"}).encode('utf-8'))
