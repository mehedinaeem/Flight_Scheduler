from tkinter import * 
import os 
from tkinter import messagebox 
 
class window(Frame): 
    '''This class contains the widgets that allow the user to edit the file saved previously''' 
 
    def _init_(self, master=None): 
        # Initialization of frame 
        Frame._init_(self, master) 
        self.master.title("Diary") 
        self.master.geometry("400x300") 
 
        # Displaying the files in the path for the user to select. 
        Label(self.master, text="Select a file").pack() 
        path = "D:\\Flight_Scheduler\\virtual_journal\\store_file" 
        self.file_names = os.listdir(path) 
        self.file_listbox = Listbox(self.master) 
        self.file_listbox.pack() 
        for i in range(0, len(self.file_names)): 
            self.file_listbox.insert(END, self.file_names[i]) 
 
        # Edit button bound with "edit_file" function which allows the user to edit the selected file. 
        edit_button = Button(self.master, text="Edit File", width=20, command=self.edit_file).pack() 
 
    def edit_file(self): 
        '''This function opens the file specified by the user to edit it. If the file is not present then it shows an error''' 
        selected_index = self.file_listbox.curselection() 
         
        if selected_index: 
            selected_file = self.file_names[selected_index[0]] 
            full_path = os.path.join("D:\\Flight_Scheduler\\virtual_journal\\store_file" + selected_file) 
 
            f = open(full_path, "r") 
            content = f.read() 
            edit_window = Tk() 
            t = Text(edit_window) 
            t.pack() 
            edit_window.title(selected_file) 
            t.insert("end", content) 
 
            # Saves the edited file. 
            def save_file(): 
                F = open(full_path, "w+") 
                F.write(t.get("1.0", END)) 
                messagebox.showinfo("Diary", "Your file is saved successfully") 
 
            save_button = Button(edit_window, text="Save", command=save_file).pack() 
        else: 
            messagebox.showinfo("Diary", "Please select a file to edit")
            
if __name__ == "__main__":
    # Create the Tkinter root window
    root = Tk()

    # Create an instance of the EditWindow class
    app = window(master=root)

    # Start the Tkinter main loop
    app.mainloop()
