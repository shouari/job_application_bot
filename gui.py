from tkinter import *

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.init_window()
        self.master = master

        # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title ("Job Application Bot")

        # allowing the widget to take the full space of the root window
        self.pack (fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file= Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command (label="Exit")

        # added "file" to our menu
        menu.add_cascade (label="File", menu=file)

        # create the file object)
        edit = Menu (menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command (label="Undo")

        # added "file" to our menu
        menu.add_cascade (label="Edit", menu=edit)

        # creating a button instance
        quitButton = Button (self, text="Quit")

        # placing the button on my window
        quitButton.place (x=0, y=0)

root = Tk ()

# size of the window
root.geometry ("400x300")
app = Window (root)
root.mainloop ()

