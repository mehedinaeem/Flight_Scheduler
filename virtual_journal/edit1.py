# Modules imported
from tkinter import *
import os
from tkinter import messagebox

class window(Frame):
    '''This class contains the widgets that allow the user to edit the file saved previously'''

    def __init__(self, master=None):
        # Initialization of the frame
        Frame.__init__(self, master)
        self.master.title("Diary")
        self.master.geometry("400x300")

        # Displaying the files in the path for the user to select.
        Label(self.master, text="Select a file").pack()
        path = r"D:\Flight_Scheduler\virtual_journal\store_file"
        self.file_names = os.listdir(path)
        self.srch_box = Entry(self.master)
        self.srch_box.pack()
        file_list = Listbox(self.master)
        file_list.pack()
        for i in range(0, len(self.file_names)):
            a = str(i + 1) + ") " + self.file_names[i]
            file_list.insert(END, a)

        # Edit button bound with "edit_file" function which allows the user to edit the selected file.
        edit_button = Button(self.master, text="Edit File", width=20, command=self.edit_file)
        edit_button.pack()

    def edit_file(self):
        '''This function opens the file specified by the user to edit it. If the file is not present, then it shows an error.'''
        self.file_name = self.srch_box.get()
        if self.file_name in self.file_names:
            file_path = os.path.join(path, self.file_name)
            with open(file_path, "r") as f:
                content = f.read()
            edit_window = Tk()
            t = Text(edit_window)
            t.pack()
            edit_window.title(self.file_name)
            t.insert("end", content)

            # Saves the edited file.
            def save_file():
                with open(file_path, "w+") as F:
                    F.write(t.get("1.0", END))
                messagebox.showinfo("Diary", "Your file is saved successfully")

            save_button = Button(edit_window, text="Save", command=save_file)
            save_button.pack()
        else:
            messagebox.showinfo("Diary", "File doesn't exist")
