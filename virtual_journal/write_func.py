# Modules imported
from tkinter import *
import time
import os
from tkinter import messagebox

def directory():
    '''This function sets the directory to the defined path. This path 
    is where all your files will be saved.'''
    path = r"D:\Flight_Scheduler\virtual_journal\store_file"
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

directory()

class WriteWindow(Frame):
    '''This class contains the widgets that will allow the user to write into files'''
    def __init__(self, master=None):
        # Initialization of the frame
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary")
        title = Label(self.master, text="Title").pack()

        # Entry box to get the title of the file from the user.
        self.title_box = Entry(self.master)
        self.title_box.pack()

        scrollbar = Scrollbar(self.master).pack(side=RIGHT, fill=Y)  # Scrollbar
        Label(self.master, text="Content").pack()

        # Text for the user to write their thoughts
        self.content_box = Text(self.master)
        self.content_box.pack()

        # This button is bound to the function "save_file" which saves the file in the specified path
        save_button = Button(self.master, text="Save", width=10, command=self.save_file).pack()

    def save_file(self):
        '''This function saves the content written by the user as a text file'''

        # localtime = time.asctime(time.localtime(time.time()))
        # date = localtime[8:11]
        # month = localtime[4:7]
        # year = localtime[20:24]
        file_name = self.title_box.get() + ".txt" #+ " " + date + month + year + ".txt"
        with open(file_name, "w+") as f:
            f.write(self.content_box.get("1.0", END))
        messagebox.showinfo("Diary", "Your file is saved successfully!!")

if __name__ == "__main__":
    # Create the Tkinter root window
    root = Tk()

    # Create an instance of the WriteWindow class
    app = WriteWindow(master=root)

    # Start the Tkinter main loop
    app.mainloop()
