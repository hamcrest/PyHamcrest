from __future__ import print_function
from hamcrest import *

try:
    class MyTest(object):
        pass
except TypeError:
    print('Object class defined at {0}'.format(getattr(object, '__file__', 'NOWHERE')))
    raise
