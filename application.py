#!/use/bin/env python 

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define,options
import handlers

define("port",default=8888,help='run on the given port',type=int)

settings = {
}

application = tornado.web.Application([
    (r'/',handlers.HelloHandler)
],**settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
