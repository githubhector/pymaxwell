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

class Box():
    """ A box with given origin, and given x and y lengths. The origin is the
    lower left corner
    """
    def __init__(self, orig, len_x, len_y):
        self.orig = orig
        self.len_x = len_x
        self.len_y = len_y

class Particle():
    def __init__(self):
        pass

class Point():
    """ A point at a given coordinate
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y