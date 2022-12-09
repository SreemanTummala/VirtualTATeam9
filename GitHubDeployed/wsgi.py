#!/usr/bin/python3.6

import sys
import logging

logging.basicConfig(level=logging.DEBUG, filename='/var/www/html/BackendFrontend/log/BackendFrontend.log', format='%(asctime)s %(message)s')

#def application(environ, start_response):
#    status = '200 OK'
#    output = b'Hellow World!'
#
#    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
#    return [output]

sys.path.insert(0,'/var/www/html/BackendFrontend/')
sys.path.insert(0, '/var/www/html/BackendFrontend/python3-virtualenv/lib/python3.6/site-packages')
from app import app as application
