from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import os

class WriteWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(WriteWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.title_label = Label(text="Title")
        self.add_widget(self.title_label)

        self.title_box = TextInput()
        self.add_widget(self.title_box)

        self.content_label = Label(text="Content")
        self.add_widget(self.content_label)

        self.content_box = TextInput()
        self.add_widget(self.content_box)

        self.save_button = Button(text="Save")
        self.save_button.bind(on_press=self.save_file)
        self.add_widget(self.save_button)

    def save_file(self, instance):
        folder_path = "D:/Flight_Scheduler/virtual_journal/store_file"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = os.path.join(folder_path, self.title_box.text + ".txt")
        with open(file_name, "w+") as f:
            f.write(self.content_box.text)

        success_popup = Popup(title='Diary', content=Label(text="Your file is saved successfully!!"),
                              size_hint=(None, None), size=(300, 200))
        success_popup.open()

class WriteApp(App):
    def build(self):
        return WriteWindow()

if __name__ == '__main__':
    WriteApp().run()
