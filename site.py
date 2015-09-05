#!/usr/local/bin/python3.4
import cherrypy
from twilio.util import TwilioCapability
import twilio.twiml

# Account Sid and Auth Token can be found in your account dashboard
ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

# TwiML app outgoing connections will use
APP_SID = 'APZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'

CALLER_ID = '+12345678901'
CLIENT = 'jenny'

class Root(object):

    @cherrypy.expose
    def token(self):
      account_sid = os.environ.get("ACCOUNT_SID", ACCOUNT_SID)
      auth_token = os.environ.get("AUTH_TOKEN", AUTH_TOKEN)
      app_sid = os.environ.get("APP_SID", APP_SID)

      capability = TwilioCapability(account_sid, auth_token)

      # This allows outgoing connections to TwiML application
      if request.values.get('allowOutgoing') != 'false':
         capability.allow_client_outgoing(app_sid)

      # This allows incoming connections to client (if specified)
      client = request.values.get('client')
      if client != None:
        capability.allow_client_incoming(client)

      # This returns a token to use with Twilio based on the account and capabilities defined above
      return capability.generate()

    @cherrypy.expose
    def welcome(self):
        resp = twilio.twiml.Response()
        resp.say("Welcome to Twilio")
        return str(resp)


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
    'log.error_file': '/home/jbutterf/logs/user/error_twilio.log'
})
cherrypy.quickstart(Root())
