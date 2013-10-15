def momentum(mass, vel):
    """ Computes the momentum of a particle. """
    mass += 1
    return mass * vel

mass = 10.0
print momentum(mass, 0.8)
print mass

def append_one(l):
    l.append(1)

# kwargs stands for keyword args
def draw(x, y, *args, **kwargs):
    print 'Draw', x, y
    print 'Args', args
    print 'Kwargs', kwargs

draw(1,2, 3, 4, color='red', height=43)

def add(x, y):
    return x + y
    
def sub(x, y):
    return x - y

def print_then_call(f, *args):
    print 'Args', args
    return f(*args)

def logging(f):
        def wrapped_f(*args):
            print 'Args', args
            return f(*args)
        
        return wrapped_f

@logging
def mult(x, y):
    return x * y

def cached(f):
    cache = {}
    
    def cached_f(*args):
        if args in cache:
            return cache[args]
        
        result = f(*args)
        cache[args] = result
        return result

    return cached_f

import time
@cached
def div(x, y):
    time.sleep(1.5)
    return x/y