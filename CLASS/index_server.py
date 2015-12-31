import http.server
import socketserver

PORT = 5555


class IndexHandler(http.server.SimpleHTTPRequestHandler):
    """Always show the index no matter what the requested path."""

    def parse_request(self, *args, **kwargs):
        super().parse_request(*args, **kwargs)
        self.path = "index.html"
        return True


httpd = socketserver.TCPServer(("", PORT), IndexHandler)
print("serving at port", PORT)
httpd.serve_forever()
