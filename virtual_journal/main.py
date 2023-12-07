#Modules used 
#These modules are inbuilt python modules.
from tkinter import *
from tkinter import messagebox
import os
import time

#These modules are user-defined python modules. Each module has its own function.
from write_func import WriteWindow
from read_func import ReadWindow
from edit_func import EditWindow

def directory():
    '''This function sets the directory to the defined path. This path 
    is where all your files will be saved.'''
    path="D:\\Flight_Scheduler\\virtual_journal\\store_file"

class LoginInterface(Frame):
    '''This class contains the login section of the app. The user has 
    to enter a password to access the main application.'''
    def __init__(self, master=None):
        # Initiating the frame
        Frame.__init__(self, master)
        self.master=master
        self.security()

    # Function that holds the widgets of the login window
    def security(self):
        self.master.title("LOGIN")
        self.pack(fill=BOTH, expand=1)
        lbl = Label(self, text="PASSWORD").grid(column=0, row=0)

        # Entry to get input from the user
        self.pwrd = Entry(self, show="*")
        self.pwrd.focus_set()
        self.pwrd.grid(column=1, row=0)

        # Login button bound to a function named login
        login = Button(self, text="login", width=20, command=self.login)
        login.grid(column=1, row=2)

    def login(self):
        '''This function, which is bound to the "login" Button, checks if the
        password given by the user is correct. If it is correct, it directs the user to the main application.'''

        # If the password given is correct, the following gets executed
        if self.pwrd.get() == "ULA":
            # Destroys the present login window
            a.destroy()

            # Initiates the main application
            b = Tk()
            b.geometry("500x500")
            app_b = Journal(b)  # Journal is a class mentioned below
            app_b.mainloop()  # Main loop for the program should run until we close

        # If the given password is wrong, then an error is shown
        else:
            messagebox.showinfo("ERROR ", "retry wrong password")

class Journal(Frame):
    '''This class contains the frame and widgets which make up the main application.
    The main application contains three buttons Write, Read, Edit respectively.'''

    # Initiating frame of the window
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.master.title("DIARY")
        self.pack(fill=BOTH, expand=1)

        # Write button bound to write function.
        write_button = Button(self, text="Write", width=100, height=10, command=self.write)
        write_button.pack()

        # Read button bound to read function.
        read_button = Button(self, text="Read", width=100, height=10, command=self.read)
        read_button.pack()

        # Edit button bound to edit function.
        edit_button = Button(self, text="Edit", width=100, height=10, command=self.edit)
        edit_button.pack()

    def write(self):
        '''This function calls the function defined in the "write_func" module.
        This module is a user-defined module. This module enables users to write their thoughts and save it in the respective directory.'''

        a = Tk()
        B = WriteWindow(a)
        B.mainloop()

    def read(self):
        '''This function calls the function defined in the "read_func" module.
        This module is a user-defined module. This module enables users to read the files they have saved previously.'''

        a = Tk()
        B = ReadWindow(a)
        B.mainloop()

    def edit(self):
        '''This function calls the function defined in the "edit_func" module.
        This module is a user-defined module. This module enables the user to revisit and edit the files they have saved previously.'''

        a = Tk()
        B = EditWindow(a)
        B.mainloop()

if __name__ == "__main__":
    # Creating the instance of the LoginInterface class and running the program
    a = Tk()
    a.geometry("250x50")
    app = LoginInterface(a)
    app.mainloop()
