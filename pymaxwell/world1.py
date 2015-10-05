from random import randint
from utils import StringBuilder


class World1:

    WORLD_NAME = "World1"
    NUM_PARTICLES = 200
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
        pass


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
            self.add_particle(Particle(x_rand, y_rand))
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
            sb.append("(%s,%s)" % (particle.x, particle.y))
            if (i+1) % 20 == 0:
                sb.append("\n    ")

        return sb.__str__()


class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
