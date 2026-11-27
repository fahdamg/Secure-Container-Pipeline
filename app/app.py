
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SecurityApp(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            response = {
                "application": "Secure Container Pipeline",
                "status": "healthy",
                "security": "Container security monitoring enabled"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), SecurityApp)
    print("Secure Container Pipeline running on port 5000")
    server.serve_forever()
