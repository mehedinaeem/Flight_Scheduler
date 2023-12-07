import os
from tkinter import *
from tkinter import messagebox

class EditWindow(Frame):
    def __init__(self, master=None):
        # Initialization of the frame
        Frame.__init__(self, master)
        self.master.title("Diary Editor")

        # Get the folder path from the user
        folder_path = "D:\\Flight_Scheduler\\virtual_journal\\store_file"

        # Check if the folder exists
        if not os.path.exists(folder_path):
            print("Error: Folder does not exist.")
            exit()

        # Get the file names in the folder
        file_names = os.listdir(folder_path)

        # Create a label to display the folder path
        folder_label = Label(self.master, text="Folder: " + folder_path)
        folder_label.pack()

        # Create a listbox to display the available files
        file_list = Listbox(self.master)
        file_list.pack()
        for file_name in file_names:
            file_list.insert(END, file_name)

        # Create an edit button
        edit_button = Button(self.master, text="Edit",width='15', command=lambda: self.edit_selected_file(file_list, folder_path))
        edit_button.pack()

    def edit_selected_file(self, file_list, folder_path):
        # Get the selected file name
        selected_file_name = file_list.get(file_list.curselection())

        # Check if a file is selected
        if not selected_file_name:
            return

        # Check if the selected file exists
        file_path = os.path.join(folder_path, selected_file_name)
        if not os.path.isfile(file_path):
            print("Error: File does not exist.")
            return

        # Open the selected file in edit mode
        with open(file_path, "r+") as f:
            contents = f.read()

        # Create an editing window
        edit_window = Toplevel(self.master)
        edit_window.title("Edit File: " + selected_file_name)
        text_widget = Text(edit_window)
        text_widget.pack()
        text_widget.insert("end", contents)

        # Add a save button to apply changes
        save_button = Button(edit_window, text="Save",width='15', command=lambda: self.save_file(file_path, text_widget.get("1.0", END)))
        save_button.pack()

    def save_file(self, file_path, text):
        # Save the modified contents to the file
        with open(file_path, "w") as f:
            f.write(text)

        # Display a message indicating successful editing
        messagebox.showinfo("Edit Successful", "File edited successfully.")

        

if __name__ == "__main__":
    # Create the Tkinter root window
    root = Tk()

    # Create an instance of the EditWindow class
    app = EditWindow(master=root)

    # Start the Tkinter main loop
    app.mainloop()
