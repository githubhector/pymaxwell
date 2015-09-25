import cmd
import traceback
import threading
import sys
import mx_engine
import world1

class MaxwellCli(cmd.Cmd):

    prompt = ">> "
    engine = mx_engine.Engine(world1.World1())

    def emptyline(self):
        pass

    def do_quit(self, line):
        self.engine.engine_stop()
        # TODO: wait for engine thread to complete
        print "Bye..."
        sys.exit()

    def do_start(self, line):
        self.engine.engine_start()

    def do_stop(self, line):
        self.engine.engine_stop()

    def do_stats(self, line):
        self.engine.engine_stats()

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
