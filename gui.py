from tkinter import *
import json

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.init_window()
        self.master = master
        self.master.minsize (400, 400)

        # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title ("Job Application Bot")
        #
        self.pack(fill= Y,side=LEFT)

        usernameLable = Label(self, text='Username',padx=5)
        usernameLable.grid(column=0, row=0)

        passwordLable = Label (self, text='Password', padx=5)
        passwordLable.grid (column=0, row=1)

        self.usernameEntry = Entry(self, width= 30)
        self.usernameEntry.grid(column=1, row =0, padx=10)

        self.passwordEntry = Entry (self, width=30)
        self.passwordEntry.grid (column=1, row=1, padx=10)


        submitButton = Button (self, text="Submit", command=self.get_credential)
        submitButton.grid(column=2, row=0)

        exitButton = Button (self, text="Exit", command=self.exit_window)
        exitButton.grid (column=2, row=1)


    def get_credential(self):
        credential ={"username": self.usernameEntry.get(), "password":self.passwordEntry.get()}
        with open ('credential.json', 'w') as fp:
            json.dump (credential, fp)

    def exit_window(self):
        pass





