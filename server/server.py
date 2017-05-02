# coding=UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

#import tornado  
from tornado import ioloop , web , httpserver , websocket , options 
#import handler function 
import handler
import os
#set server settings 
server_settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"xsrf_cookies": True,
	"autoreload": True,
    #"login_url": "/accounts/login",
    "debug":True,
    "template_path":os.path.join(os.path.dirname(__file__),"templates"),
}

#the handlers list
handlers=[
	(r"/?",handler.MainHandler),
	(r"/upload",handler.WavFileHandler)
]


options.define("port", default=8080, help="the application will be run on the given port", type=int)

if __name__ == "__main__":
	options.parse_command_line()
	app_server = httpserver.HTTPServer(web.Application(handlers,**server_settings))
	app_server.listen(options.options.port)
	ioloop.IOLoop.current().start()