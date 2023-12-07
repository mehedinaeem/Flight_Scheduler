from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import os

class DiaryApp(App):
    def build(self):
        self.title = 'DIARY'
        layout = BoxLayout(orientation='vertical')

        write_button = Button(text="Write", size_hint=(1, 0.3))
        write_button.bind(on_press=self.write)
        layout.add_widget(write_button)

        return layout

    def write(self, instance):
        write_popup = Popup(title='Write', size_hint=(None, None), size=(400, 400))
        inner_layout = BoxLayout(orientation='vertical')

        title_label = Label(text='Title:')
        inner_layout.add_widget(title_label)

        title_input = TextInput()
        inner_layout.add_widget(title_input)

        content_label = Label(text='Content:')
        inner_layout.add_widget(content_label)

        content_input = TextInput()
        inner_layout.add_widget(content_input)

        save_button = Button(text="Save")
        save_button.bind(on_press=lambda x: self.save_file(title_input.text, content_input.text))
        inner_layout.add_widget(save_button)

        write_popup.content = inner_layout
        write_popup.open()

    def save_file(self, title, content):
        folder_path = "D:\\Flight_Scheduler\\virtual_journal\\store_file"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = os.path.join(folder_path, title + ".txt")
        with open(file_name, "w+") as f:
            f.write(content)

        success_popup = Popup(title='Diary', content=Label(text="Your file is saved successfully!!"),
                              size_hint=(None, None), size=(300, 200))
        success_popup.open()


if __name__ == '__main__':
    DiaryApp().run()
