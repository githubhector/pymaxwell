import time
import threading

class Engine:

    TICKS_PER_STATS_UPDATE = 1000000
    MICROS_PER_SECOND = 1000000
    total_ticks = 0L
    time_previous_update = 0.0
    ticks_per_second = 0.0
    micros_per_tick = 0.0
    engine_started = False
    engine_start_time = 0.0
    world = None

    def __init__(self, world):
        self.engine_start_time = time.time()
        self.world = world

    def tick_loop(self):
        while self.engine_started:
            self.tick()
        print "Exiting engine thread..."

    def tick(self):
        self.total_ticks += 1
        if self.total_ticks % self.TICKS_PER_STATS_UPDATE == 0:
            self.update_stats()
        self.world_update()

    def update_stats(self):
        time_now = time.time()
        time_delta_since_previous_update = time_now - self.time_previous_update
        self.ticks_per_second = self.TICKS_PER_STATS_UPDATE / time_delta_since_previous_update
        self.micros_per_tick = self.MICROS_PER_SECOND / self.ticks_per_second
        self.time_previous_update = time_now

    def engine_start(self):
        print "Starting engine for world: ", self.world.world_name
        self.world_init()
        self.engine_started = True
        self.engine_start_time = time.time()
        threading.Thread(target=self.tick_loop).start()

    def engine_stop(self):
        self.engine_started = False

    def engine_stats(self):
        if self.engine_started:
            time_now = time.time()
            engine_time = time_now - self.engine_start_time
            print "Engine time: %.1f, ticks: %d, ticks per sec: %.1f, micros per tick: %.4f" % (engine_time, self.total_ticks,
                                                                            self.ticks_per_second, self.micros_per_tick)
        else:
            print "Engine not running..."

    def world_init(self):
        print "Initializing world..."

    def world_update(self):
        pass
        #print "Updating world..."


