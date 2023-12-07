from tkinter import *
import os
from tkinter import messagebox

class window(Frame):
    '''This class contains the widgets that allows the user to read the files stored previously'''
    def __init__(self, master=None):
        # Initialization of the frame
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary")
        self.master.geometry("400x300")

        # Display all the files present in the directory
        Label(self.master, text="Select a file").pack(side=TOP)
        path = "D:\\Flight_Scheduler\\virtual_journal\\store_file"
        self.file_names = os.listdir(path)
        self.srch_box = Entry(self.master)
        self.srch_box.pack()
        file_list = Listbox(self.master)
        file_list.pack()
        for i in range(0, len(self.file_names)):
            a = str(i + 1) + ") " + self.file_names[i]
            file_list.insert(END, a)

        # Read button binded to the function "read_file" which displays the content in the file.
        read_button = Button(self.master, text="Read", width=20, command=self.read_file).pack(side=BOTTOM)

    def read_file(self):
        self.file_name = self.srch_box.get()

        if self.file_name and (self.file_name in self.file_names):
            file_path = os.path.join("D:\\Flight_Scheduler\\virtual_journal\\store_file", self.file_name)

            try:
                with open(file_path, "r") as f:
                    contents = f.read()
            except FileNotFoundError:
                messagebox.showinfo("Diary", "File doesn't exist")
            else:
                read_window = Toplevel(self.master)
                read_window.title(self.file_name)
                text_widget = Text(read_window)
                text_widget.pack()
                text_widget.insert("end", contents)
                text_widget.config(state=DISABLED)
        else:
            messagebox.showinfo("Diary", "File doesn't exist")

# Create the main application window
root = Tk()

# Create an instance of the window class
app = window(root)

# Run the application
root.mainloop()
