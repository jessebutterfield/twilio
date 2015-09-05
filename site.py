#!/usr/local/bin/python3.4
import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self, **args):
            return '<Response><Sms>Stop masturbating in the shower. There is a drought.</Sms></Response>'

    @cherrypy.expose
    def reply(self, **args):
            return '<Response><Sms>Something less work inappropriate.</Sms></Response>'

cherrypy.config.update({
    'environment': 'production',
    'log.screen': False,
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 16166,
})
cherrypy.quickstart(Root())
