# noinspection PyShadowingBuiltins,PyUnusedLocal

def validate(val):
    # type safety
    if isinstance(val, str):
        if val.isdigit():
            val = int(val)
        else:
            raise TypeError("input %r must be an integer" % val)
    # range
    if val < 0 or val > 100:
        raise AssertionError("input %r must be within range 0-100" % val)
    return val

def sum(x, y):
    x = validate(x)
    y = validate(y)    
    return x + y

