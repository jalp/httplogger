""" Logger http handler example
"""

import logging
from logging.handlers import HTTPHandler
import socket


class HTTPHandler(HTTPHandler):
    wanted = ['created', 'levelname', 'clientip', 'user', 'msg']

    def mapLogRecord(self, record):
        # Dict comprehension for 2.6
        return dict((name, getattr(record, name, "#Unknown")) for name in self.wanted)
        # Dict comprehension for > 2.7
        #return {name: getattr(record, name, "#Unknown") for name in self.wanted}


FORMAT = '%(asctime)-15s %(levelname)s %(clientip)s %(user)-4s %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger('foo')
http_handler = HTTPHandler(
    'localhost:8888',
    '/remotelog',
    method='POST',
)
logger.addHandler(http_handler)

logger.info('testing remote logging')

d = {'clientip': socket.gethostbyname(socket.getfqdn()), 'user': 'FOO'}
logger.warning('Protocol problem: {0}'.format('connection reset'), extra=d)
logger.error('Exception in class foo: {0}'.format('Attribute error exception'), extra=d)
# There is an error in httphandler with interpolated data!!!
logger.error('Exception in class foo: %s', 'Attribute error exception', extra=d)
