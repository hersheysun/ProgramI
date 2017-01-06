from kivy.app import App
from kivy.app import Widget
from kivy.lang import Builder
class Demo1(App):
    def build(self):#self means this build()belong to Demo1
        self.title = "hellow, world"
        self.root= Widget()
        return self.root

class Demo2(App):
    def build(self):
        self.title="Demo"
        self.root= Builder.load_file("kivy_demo.kv")
        return self.root
#Demo1().run()
Demo2().run()