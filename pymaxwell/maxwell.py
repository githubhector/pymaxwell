import cmd
import traceback
import threading
import sys
import mx_engine
import world1

class MaxwellCli(cmd.Cmd):

    prompt = ">> "
    engine = None
    world = None

    def emptyline(self):
        pass

    def do_quit(self, line):
        if self.engine is not None:
            self.engine.engine_stop()
        print "Bye..."
        sys.exit()

    def do_start(self, line):
        self.world = world1.World1()
        self.engine = mx_engine.Engine(self.world)
        self.engine.engine_start()

    def do_world(self, line):
        pass

    def do_stop(self, line):
        if self.engine is not None:
            self.engine.engine_stop()
            self.engine = None

    def do_stats(self, line):
        if self.engine is not None:
            self.engine.engine_stats()
        else:
            print "Do not have an engine..."

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
