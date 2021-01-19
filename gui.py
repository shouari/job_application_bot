from tkinter import *
import easyapplybot as bot
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
        self.usernameEntry = Entry(self, width= 30)
        self.usernameEntry.grid(column=1, row =0, padx=10)

        passwordLable = Label(self, text='Password', padx=5)
        passwordLable.grid(column=0, row=1)
        self.passwordEntry = Entry (self, width=30)
        self.passwordEntry.grid (column=1, row=1, padx=10)

        job_positionLable = Label(self, text='Job Position', padx=5)
        job_positionLable.grid(column=0, row=2)
        self.job_title = Entry(self, width=30)
        self.job_title.grid(column=1, row=2, padx=10)

        cityLable = Label(self, text='City', padx=5)
        cityLable.grid(column=0, row=3)
        self.city = Entry(self, width=30)
        self.city.grid(column=1, row=3, padx=10)

        countryLable = Label(self, text='Country', padx=5)
        countryLable.grid(column=0, row=4)
        self.country = Entry(self, width=30)
        self.country.grid(column=1, row=4, padx=10)


        continueButton = Button (self, text="Continue", command=self.get_data)
        continueButton.grid(column=2, row=0)

        exitButton = Button (self, text="Exit", command=self.exit_window)
        exitButton.grid (column=2, row=1)


    def get_data(self):
        data ={"username": self.usernameEntry.get(),
               "password":self.passwordEntry.get(),
               "job_title": self.job_title.get(),
               "city": self.city.get(),
               "country": self.country.get()
               }
        with open ('data.json', 'w') as fp:
            json.dump (data, fp)


    def exit_window(self):
       pass

class Page1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.minsize(400, 400)
        self.master.title("PAge 2")
        #
        self.pack(fill=Y, side=LEFT)

root = Tk ()
app = Window (root)
root.mainloop ()



