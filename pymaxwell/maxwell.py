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
        self.world.show()

    def do_stop(self, line):
        if self.engine is not None:
            self.engine.engine_stop()
            self.engine = None

    def do_stats(self, line):
        if self.engine is not None:
            self.engine.engine_stats()
        else:
            print "Do not have an engine..."

    def do_gui(self, line):
        print "GUI..."
        build_gui()



###################################################################################
# This is sample code, will be removed after figuring out how Tk works

from Tkinter import *

WIDTH = 400             # OF SCREEN IN PIXELS
HEIGHT = 400            # OF SCREEN IN PIXELS
FRAMES_PER_SEC = 40     # SCREEN UPDATE RATE

def build_gui():
    print "Building GUI..."
    global graph, left, top
    root = Tk()
    root.resizable(False, False)
    root.title('Balls')
    left = (root.winfo_screenwidth() - WIDTH) / 2
    top = (root.winfo_screenheight() - HEIGHT) / 2
    root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, left, top))
    root.bind_all('<Escape>', lambda event: event.widget.quit())
    #root.bind('<Configure>', window_move)
    graph = Canvas(root, width=WIDTH, height=HEIGHT, background='white')
    #graph.after(1000 / FRAMES_PER_SEC, update)
    #graph.after(1000, activate)
    graph.pack()
    graph.update()

###################################################################################







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
