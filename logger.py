""" Logger http handler example
"""

import logging
import logging.handlers
import socket


FORMAT = '%(asctime)-15s %(clientip)s %(user)-4s %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger('foo')
http_handler = logging.handlers.HTTPHandler(
    'localhost:5000',
    '/remotelog',
    method='POST',
)
logger.addHandler(http_handler)

logger.info('testing remote logging')

d = {'clientip': socket.gethostbyname(socket.getfqdn()), 'user': 'FOO'}
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

logger.error('Exception in class foo: %s', 'Atribut error exception', extra=d)
