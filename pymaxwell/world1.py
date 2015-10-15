from random import randint
from utils import StringBuilder


class World1:

    WORLD_NAME = "World1"
    NUM_PARTICLES = 2
    box = None

    def __init__(self):
        print "Initializing instance of World1..."

        print "Creating box..."
        self.box = Box((0,0), 100, 50)

        print "Adding particles to the box..."
        self.box.add_particles_at_random(self.NUM_PARTICLES)

    def show(self):
        print "World1:\n%s" % self.box

    def update(self):
        for particle in self.box.particles:
            particle.update_position(1)


class Vector():
    """ A vector with the given x and y components
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def scalar_mult(self, scalar):
        return Vector(scalar*self.x, scalar*self.y)


class Box():
    """ A box with given origin, and x, y lengths. The box's origin is the
    lower left corner. Expect orig to be a pair (x,y)
    """

    particles = []

    def __init__(self, orig, len_x, len_y):
        self.orig = orig
        self.len_x = len_x
        self.len_y = len_y
        self.x_interval = (orig[0], orig[0] + len_x)
        self.y_interval = (orig[1], orig[1] + len_y)

    def add_particle(self, particle):
        self.particles.append(particle)

    def add_particles_at_random(self, num_particles):
        print "x_interval", self.x_interval
        print "y_interval", self.y_interval
        for i in range(0, num_particles):
            x_rand = randint(self.x_interval[0], self.x_interval[1])
            y_rand = randint(self.y_interval[0], self.y_interval[1])
            self.add_particle(Particle(1, Vector(x_rand, y_rand), Vector(0,0)))
            print "x_rand:", x_rand, " y_rand:", y_rand

    def __str__(self):
        num_particles = self.particles.__len__()
        sb = StringBuilder()
        sb.append("Box:")
        sb.append("\n  origin:%s, x_interval:%s, y_interval:%s" % (self.orig, self.x_interval, self.y_interval))
        sb.append("\n  number of particles: %s\n" % num_particles)

        sb.append("    ")
        for i in range(0, num_particles):
            particle = self.particles[i]
            sb.append("[p(%s,%s), v(%s,%s)]" % (particle.pos[0], particle.pos[1], particle.vel[0], particle.vel[1]))
            if (i+1) % 20 == 0:
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