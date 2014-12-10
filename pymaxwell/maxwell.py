import time
import cmd
import traceback
import threading
import sys

# TODO: use a stopwatch class
# TODO: figure out why autocompletion isn't working

class State(object):

    TICKS_PER_LOG_INTERVAL = 1000000
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


class MaxwellCli(cmd.Cmd):

    prompt = "$ "

    def emptyline(self):
        pass

    def do_quit(self, line):
        "Exit the python interpreter"
        print "Bye..."
        sys.exit()

    def do_start(self, line):
        "Start the simulation"
        print "Starting the simulation..."
        tick = threading.Thread(name='TICK', target=tick_thread)
        tick.start()


def tick_thread():
    print "Starting tick..."
    while True:
        State.tick()

def cli_thread():
    print "Starting CLI..."
    while True:
        try:
            MaxwellCli().cmdloop()
        except Exception as e:
            print "Exception: %s" % e
            traceback.print_exc()



if __name__ == '__main__':
    cli = threading.Thread(name='CLI', target=cli_thread)
    cli.start()
