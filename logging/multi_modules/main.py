"""
Refer to:
https://docs.python.org/2/howto/logging-cookbook.html#using-logging-in-multiple-modules
https://docs.python.org/2/library/logging.handlers.html#filehandler
"""

import logging 
import log1
import auxiliary_module

log1.logging_config()

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

logger.info('xxw-creating an instance of auxiliary_module.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
auxiliary_module.some_function()
logger.info('done with auxiliary_module.some_function()')
