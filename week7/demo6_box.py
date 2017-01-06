from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('demo6_box.kv')
        self.root.ids.output_label.text = "Hello "
        return self.root


BoxLayoutDemo().run()
