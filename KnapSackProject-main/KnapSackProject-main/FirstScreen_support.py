import sys

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def run():
    sys.stdout.flush()

def destroy_window():

    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import FirstScreen
    FirstScreen.vp_start_gui()




