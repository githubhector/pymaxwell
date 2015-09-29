
class World1:

    WORLD_NAME = "World1"
    NUM_PARTICLES = 5
    box = None

    def __init__(self):
        print "Initializing instance of World1..."

        print "Creating box..."
        self.box = Box((0,0), 100, 50)

        print "Adding particles to the box..."
        self.box.add_particles_at_random(NUM_PARTICLES)

    def update(self):
        pass


class Box():
    """ A box with given origin, and x, y lengths. The box's origin is the
    lower left corner. Expect orig to be a pair (x,y)
    """
    def __init__(self, orig, len_x, len_y):
        self.orig = orig
        self.len_x = len_x
        self.len_y = len_y
        self.x_interval = (orig[0], orig[0] + len_x)
        self.y_interval = (orig[1], orig[1] + len_y)

    def add_particles_at_random(self, num_particles):
        pass


class Particle():
    def __init__(self):
        pass

