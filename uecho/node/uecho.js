// Adapted from https://rosettacode.org/wiki/Hello_world/Web_server#JavaScript
var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('<html><head><title>Unstoppable Echo</title></head><body><h1>' + req.url.replace(/^\/+/, '') + ' right back at ya!</h1></body></html>');
}).listen(8080, '127.0.0.1');
