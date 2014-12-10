import cmd
import traceback
import threading
import sys
import mx_engine


# TODO: figure out why autocompletion isn't working

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
