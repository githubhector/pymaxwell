import cmd
import traceback
import threading
import sys
import mx_engine

class MaxwellCli(cmd.Cmd):

    prompt = "$ "
    engine = mx_engine.Engine()

    def emptyline(self):
        pass

    def do_quit(self, line):
        "Exit the python interpreter"
        print "Bye..."
        sys.exit()

    def do_start(self, line):
        "Start the Maxwell engine"
        self.engine.engine_start()

    def do_stop(self, line):
        "Stop the Maxwell engine"
        self.engine.engine_stop()

    def do_stats(self, line):
        "Report statistics -- yes do that"
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
