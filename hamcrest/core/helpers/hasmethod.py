__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

def hasmethod(obj, methodname):
    """Does obj have a method named methodname?"""

    if not hasattr(obj, methodname):
        return False
    method = getattr(obj, methodname)
    return callable(method)
