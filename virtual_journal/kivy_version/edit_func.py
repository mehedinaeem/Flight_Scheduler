from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import os

class EditWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(EditWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.folder_path = "D:/Flight_Scheduler/virtual_journal/store_file"

        if not os.path.exists(self.folder_path):
            print("Error: Folder does not exist.")
            exit()

        file_names = os.listdir(self.folder_path)

        self.folder_label = Label(text="Folder: " + self.folder_path)
        self.add_widget(self.folder_label)

        self.file_label = Label(text="Select a file")
        self.add_widget(self.file_label)

        self.file_list = BoxLayout(orientation='vertical', size_hint_y=None)
        self.file_list.bind(minimum_height=self.file_list.setter('height'))

        for file_name in file_names:
            file_button = Button(text=file_name, size_hint_y=None, height=40)
            file_button.bind(on_press=self.edit_selected_file)
            self.file_list.add_widget(file_button)

        self.add_widget(self.file_list)

    def edit_selected_file(self, instance):
        selected_file_name = instance.text

        file_path = os.path.join(self.folder_path, selected_file_name)
        if not os.path.isfile(file_path):
            print("Error: File does not exist.")
            return

        with open(file_path, "r+") as f:
            contents = f.read()

        edit_popup = Popup(title="Edit File: " + selected_file_name, size_hint=(None, None), size=(400, 300))
        edit_layout = BoxLayout(orientation='vertical')

        text_input = TextInput(text=contents, multiline=True)
        edit_layout.add_widget(text_input)

        save_button = Button(text="Save", size_hint=(None, None), size=(100, 40))
        save_button.bind(on_press=lambda instance: self.save_file(file_path, text_input.text, edit_popup))
        edit_layout.add_widget(save_button)

        edit_popup.content = edit_layout
        edit_popup.open()

    def save_file(self, file_path, text, popup):
        with open(file_path, "w") as f:
            f.write(text)

        popup.dismiss()

class EditApp(App):
    def build(self):
        return EditWindow()

if __name__ == '__main__':
    EditApp().run()
