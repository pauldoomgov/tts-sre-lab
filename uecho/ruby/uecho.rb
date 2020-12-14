require 'webrick'
server = WEBrick::HTTPServer.new(:Port => 8080)
server.mount_proc('/') {|request, response|
  path = request.request_uri.path.to_s
  estring = path[(path.start_with?('/') ? 1 : 0)..]
  response.body = "<html><head><title>Unstoppable Echo</title></head><body><h1>#{estring} right back at ya!</h1></body></html>"
}
trap("INT") {server.shutdown}
server.start
