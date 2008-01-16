def hasmethod(obj, methodname):
    if not hasattr(obj, methodname):
        return False
    method = getattr(obj, methodname)
    return callable(method)
