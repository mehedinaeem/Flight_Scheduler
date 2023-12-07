from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
import os

class ReadWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(ReadWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.folder_path = "D:/Flight_Scheduler/virtual_journal/store_file"

        if not os.path.exists(self.folder_path):
            print("Error: Folder does not exist.")
            exit()

        file_names = os.listdir(self.folder_path)

        self.file_label = Label(text="Select a file")
        self.add_widget(self.file_label)

        self.file_list = ScrollView()
        self.add_widget(self.file_list)

        self.file_box = BoxLayout(orientation='vertical', size_hint_y=None)
        self.file_box.bind(minimum_height=self.file_box.setter('height'))

        for file_name in file_names:
            file_button = Button(text=file_name, size_hint_y=None, height=40)
            file_button.bind(on_press=self.read_selected_file)
            self.file_box.add_widget(file_button)

        self.file_list.add_widget(self.file_box)

    def read_selected_file(self, instance):
        selected_file_name = instance.text

        file_path = os.path.join(self.folder_path, selected_file_name)
        if not os.path.isfile(file_path):
            print("Error: File does not exist.")
            return

        with open(file_path, "r") as f:
            contents = f.read()

        read_popup = Popup(title=selected_file_name, content=Label(text=contents),
                           size_hint=(None, None), size=(400, 300))
        read_popup.open()

class ReadApp(App):
    def build(self):
        return ReadWindow()

if __name__ == '__main__':
    ReadApp().run()
