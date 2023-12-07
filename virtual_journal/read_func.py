import os
from tkinter import *

class ReadWindow(Frame):
    def __init__(self, master=None):
        #intilisation of the frame
        Frame.__init__(self,master)
        self.master=master
        self.master.title("Diary")
        self.master.geometry("400x300")
        
        
        # Get the folder path from the user
        folder_path = "D:\\Flight_Scheduler\\virtual_journal\\store_file"
        
        
        # #-------------------------
        # #Display all the files present in the directory
        # Label(self.master,text="Select a file").pack(side=TOP)
        # folder_path = "D:\\Flight_Scheduler\\virtual_journal\\store_file"
        # self.file_names=os.listdir(folder_path)
        # self.srch_box=Entry(self.master)
        # self.srch_box.pack()
        # file_list=Listbox(self.master)
        # file_list.pack()
        # for i in range(0,len(self.file_names)):
        #     a=str(i+1)+") "+self.file_names[i]
        #     file_list.insert(END,a)
            
            

        # Check if the folder exists
        if not os.path.exists(folder_path):
            print("Error: Folder does not exist.")
            exit()

        # Get the file names in the folder
        file_names = os.listdir(folder_path)

        # Create a label to display the folder path
        Label(self.master,text="Select a file").pack(side=TOP)

        # folder_label = Label(self.master, text="Folder: " + folder_path)
        # folder_label.pack()

        # Create a listbox to display the available files
        file_list = Listbox(self.master)
        file_list.pack()
        for file_name in file_names:
            file_list.insert(END, file_name)

        # Define the function to read the selected file
        def read_selected_file():
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

            # Open the selected file and read its contents
            with open(file_path, "r") as f:
                contents = f.read()

            # Display the file contents in a new window
            read_window = Toplevel(self.master)
            read_window.title(selected_file_name)
            text_widget = Text(read_window)
            text_widget.pack()
            text_widget.insert("end", contents)
            text_widget.config(state=DISABLED)

        # Create a button to read the selected file
        read_button = Button(self.master, text="Read",width=15, command=read_selected_file)
        read_button.pack()
        
        #-------------------------
    #     read_button=Button(self.master,text="Read",width=20,command=self.read_file).pack(side=BOTTOM)
    # def read_file(self):
    #     self.file_name=self.srch_box.get()
    

if __name__ == "__main__":
    # Create the Tkinter root window
    root = Tk()

    # Create an instance of the ReadWindow class
    app = ReadWindow(master=root)

    # Start the Tkinter main loop
    app.mainloop()
