import time
import threading

# TODO: use a stopwatch class

class State(object):

    TICKS_PER_LOG_INTERVAL = 10000000
    total_ticks = 0L
    clock_previous = 0.0

    @classmethod
    def log_state_info(cls):
        clock_current = time.clock()
        clock_delta = clock_current - cls.clock_previous
        ticks_per_second = cls.TICKS_PER_LOG_INTERVAL / clock_delta
        micros_per_tick = 1000000. / ticks_per_second
        print "clock: %s, ticks: %s, clock delta: %s, ticks per sec: %s, micros per tick: %s" % (clock_current, State.total_ticks,
                                                                            clock_delta, ticks_per_second, micros_per_tick)
        cls.clock_previous = clock_current

    @classmethod
    def tick(cls):
        cls.total_ticks += 1
        if cls.total_ticks % cls.TICKS_PER_LOG_INTERVAL == 0:
            cls.log_state_info()

def tick_thread():
    print "Starting tick..."
    while True:
        State.tick()

def start():
    print "Starting the engine..."
    tick = threading.Thread(name='TICK', target=tick_thread)
    tick.start()
