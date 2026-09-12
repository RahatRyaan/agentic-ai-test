#!/usr/bin/env python3
"""Lightweight microservice for workstation pipeline testing."""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler

def compute_metrics():
    """Returns sample agentic telemetry."""
    return {
        "status": "healthy",
        "service": "agentic-test-pipeline",
        "version": "1.0.0",
        "engine": "python3.14",
    }

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/health"):
            data = json.dumps(compute_metrics()).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Suppress noisy request logging during tests
        return

def run_server(host="127.0.0.1", port=8080):
    server = HTTPServer((host, port), RequestHandler)
    print(f"Server started on http://{host}:{port}")
    return server

if __name__ == "__main__":
    server = run_server(host="0.0.0.0", port=8080)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
