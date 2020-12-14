#!/usr/bin/env python3

# Based on https://rosettacode.org/wiki/Hello_world/Web_server#Python
import threading
 
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
 
class EchoHTTPRequestHandler(BaseHTTPRequestHandler):
 
  message = '<html><head><title>Unstoppable Echo</title></head><body><h1>{} right back at ya!</h1></body></html>'
 
  def do_GET(self):
    emessage = self.message.format(self.path.lstrip('/'))
    self.send_response(200)
    self.send_header('Content-type', 'text/html; charset=UTF-8')
    self.end_headers()
    self.wfile.write(emessage.encode('utf-8'))
    self.close_connection = True
 
 
def serve(addr, port):
  with ThreadingHTTPServer((addr, port), EchoHTTPRequestHandler) as server:
    server.serve_forever(poll_interval=None)
 
 
if __name__ == '__main__':
 
  addr, port = ('localhost', 8080)
 
  threading.Thread(target=serve, args=(addr, port), daemon=True).start()
 
  try:
    while True:
      input()
 
  except KeyboardInterrupt:
    pass

