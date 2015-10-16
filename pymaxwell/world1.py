from random import uniform
from time import clock
from utils import StringBuilder


class World1:

    WORLD_NAME = "World1"
    NUM_PARTICLES = 5
    box = None
    t_previous = 0

    def __init__(self):
        print "Initializing instance of World1..."

        print "Creating box..."
        self.box = Box(Vector(0,0), 10, 10)

        print "Adding particles to the box..."
        self.box.add_particles_at_random(self.NUM_PARTICLES)

    def show(self):
        print "World1:\n%s" % self.box

    def update(self):
        t_current = clock()
        t_delta = t_current - self.t_previous
        print "\n%s: Updating world: t_delta: %s" % (t_current, t_delta)

        for particle in self.box.particles:
            particle.update_position(t_delta)

        self.show()

        self.t_previous = t_current


class Vector():
    """ A vector with the given x and y components. Generally we assume MKS, e.g., position is in meters, mass in kilos,
    time in seconds, velocity in meters/sec, etc.
    """
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def scalar_mult(self, scalar):
        return Vector(scalar*self.x, scalar*self.y)

    def __str__(self):
        return "(%s,%s}" % (self.x, self.y)


class Box():
    """ A box with given origin, and x, y lengths. The box's origin is the
    lower left corner. Expect orig to be a Vector
    """

    particles = []

    def __init__(self, orig, len_x, len_y):
        self.orig = orig
        self.len_x = float(len_x)
        self.len_y = float(len_y)
        self.x_interval = (self.orig.x, self.orig.x + len_x)
        self.y_interval = (self.orig.y, self.orig.y + len_y)

    def add_particle(self, particle):
        self.particles.append(particle)

    def add_particles_at_random(self, num_particles):
        print "x_interval", self.x_interval
        print "y_interval", self.y_interval
        for i in range(0, num_particles):
            x_rand = uniform(self.x_interval[0], self.x_interval[1])
            y_rand = uniform(self.y_interval[0], self.y_interval[1])
            self.add_particle(Particle(1, Vector(x_rand, y_rand), Vector(.1,.1)))
            print "x_rand:", x_rand, " y_rand:", y_rand

    def __str__(self):
        num_particles_per_line_in_display = 1
        num_particles = self.particles.__len__()
        sb = StringBuilder()
        sb.append("Box:")
        sb.append("\n  origin:%s, x_interval:%s, y_interval:%s" % (self.orig, self.x_interval, self.y_interval))
        sb.append("\n  number of particles: %s\n" % num_particles)

        sb.append("    ")
        for i in range(0, num_particles):
            particle = self.particles[i]
            sb.append("[p(%s), v(%s)]" % (particle.pos, particle.vel))
            if (i+1) % num_particles_per_line_in_display == 0:
                sb.append("\n    ")

        return sb.__str__()


class Particle():
    """ A circular particle with given radius, position and velocity.
    Expect pos and vel to be vectors
    """
    def __init__(self, radius, pos, vel):
        self.radius = radius
        self.pos = pos
        self.vel = vel

    def update_position(self, delta_t):
        self.pos = self.pos.__add__(self.vel.scalar_mult(delta_t))