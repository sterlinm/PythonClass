def momentum(mass, vel):
    return mass * vel

def energy(mass, vel):
    return 0.5 * mass * vel**2.0

mass1 = 1.0
vel1 = 0.5

mass2 = 3.0
vel2 = 0.7

print 'Particle 1:'
print 'Mass:', mass1
print 'Velocity:', vel1
print 'Momentum:', momentum(mass1, vel1)
print 'Energy:', energy(mass1, vel1)

print
print

print 'Particle 12:'
print 'Mass:', mass2
print 'Velocity:', vel2
print 'Momentum:', momentum(mass2, vel1)
print 'Energy:', energy(mass2, vel2)

# An alternative would be to use a dictionary for the attributes of the particle

def momentum_dict(particle):
    return particle['mass'] * particle['vel']

def energy_dict(particle):
    return 0.5 * particle['mass'] * particle['vel']**2.0

def init(mass, vel):
    return {'mass': mass, 'vel': vel}

particles = [init(1.0, 0.5), init(3.0, 0.7)]

print momentum_dict(particles[0])

# Instead we can use a class

#class Particle(object):
#    
#    def __init__(self, mass, vel):
#        self.mass = mass
#        self.vel = vel
#    
#    def momentum(self):
#        return self.mass * self.vel
#    
#    def energy(self):
#        return 0.5 * self.mass * self.vel**2.
        

class Particle(object):
    
    def __init__(self, mass, vel):
        self.__mass = mass
        self.__vel = vel
        self.__momentum = mass * vel
        self.__energy = 0.5 * mass * vel**2.0
    
    def set_mass(self, value):
        self.__mass = value
        self.__momentum = self.__mass * self.__vel
        self.__energy = 0.5 * self.__mass * self.__vel**2.0
    
    def set_vel(self, value):
        self.__vel = value
        self.__momentum = self.__mass * self.__vel
        self.__energy = 0.5 * self.__mass * self.__vel**2.0
    
    def get_mass(self):
        return self.__mass
    
    def get_vel(self):
        return self.__vel
    
    def get_momentum(self):
        return self.__momentum
    
    def get_energy(self):
        return self.__energy
    
    mass = property(get_mass, set_mass)
    vel = property(get_vel, set_vel)
    momentum = property(get_momentum)
    energy = property(get_energy)

# Magic Methods
# __repr__
# __add__
# __magic__

# Properties
class MyClass(object):
    
    def __init__(self):
        self._half_a = 14
    
    def get_a(self):
        print "In the getter"
        return self._half_a * 2
    
    def set_a(self, value):
        print "In the setter"
        self._half_a = value / 2.0
    
    a = property(get_a, set_a)

class MyClass(object):
    
    def __init__(self):
        self._half_a = 14
    
    @property
    def a(self):
        print "In the getter"
        return self._half_a * 2
    
    @a.setter
    def a(self, value):
        print "In the setter"
        

c = MyClass()