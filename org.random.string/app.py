# -*- coding: utf-8 -*-
___author___ = "Morando Nicolò"
___version___ = "0.1.2"


import cherrypy
import os
from jinja2 import Environment, FileSystemLoader
import random
import string


'''
declaration of the field of use, of the python code (cherry)
'''
enviroment = Environment(loader = FileSystemLoader('html'))


'''
creation of the class that generates random strings, receiving the length
'''
class BasicStringGenerator(object):
    @cherrypy.expose
    def index(self):
         return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="0" name="length" />
              <button type="submit">button</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length = 0):
        somestring = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = somestring
        return somestring

    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']


'''
writing the code configuration.
documentation link: https://docs.cherrypy.org/en/latest/config.html
'''
config = {
        '/': {
            'tools.sessions.on': True
        }
    }


'''
code execution, with creation of an instance, configured on the local host: http://127.0.0.1:8080/
'''
cherrypy.quickstart(BasicStringGenerator(), '/', config)
