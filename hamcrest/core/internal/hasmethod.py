def hasmethod(obj, methodname):
    """Does obj have a method named methodname?"""
    
    if not hasattr(obj, methodname):
        return False
    method = getattr(obj, methodname)
    return callable(method)
