class World1:

    WORLD_NAME = "World1"
    NUM_PARTICLES = 5

    def __init__(self):
        print "Initializing instance of World1..."
        print "Creating particles list..."
        self.particles = list()
        for i in range(0, self.NUM_PARTICLES):
            print i
            self.particles.append(Particle())

    def update(self):
        pass


class Particle(object):
    pass

