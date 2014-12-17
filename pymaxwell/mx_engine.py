import time
import threading
import sys

class Engine(object):

    TICKS_PER_LOG_INTERVAL = 1000000
    total_ticks = 0L
    clock_previous = 0.0
    engine_started = False

    def log_state_info(self):
        clock_current = time.clock()
        clock_delta = clock_current - self.clock_previous
        ticks_per_second = self.TICKS_PER_LOG_INTERVAL / clock_delta
        micros_per_tick = 1000000. / ticks_per_second
        self.clock_previous = clock_current
        print "clock: %s, ticks: %s, clock delta: %s, ticks per sec: %s, micros per tick: %s" % (clock_current, Engine.total_ticks,
                                                                            clock_delta, ticks_per_second, micros_per_tick)

    def tick(self):
        self.total_ticks += 1
        if self.total_ticks % self.TICKS_PER_LOG_INTERVAL == 0:
            self.log_state_info()

    def tick_loop_thread(self):
        print "Starting engine thread..."
        while self.engine_started:
            self.tick()
        print "Exiting engine thread..."

    def engine_start(self):
        print "Starting engine..."
        self.engine_started = True
        threading.Thread(target=self.tick_loop_thread).start()

    def engine_stop(self):
        print "Stopping engine..."
        self.engine_started = False


