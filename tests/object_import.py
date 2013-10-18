from hamcrest import *

try:
    class MyTest(object):
        pass
except TypeError:
    print 'Object class defined at ' + getattr(object, '__file__', 'NOWHERE')
    raise
