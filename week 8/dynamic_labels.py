"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
"""
from kivy.app import App
from kivy.lang import Builder


KV = '''
BoxLayout:
    orientation: 'vertical'
    id: main
'''

class NameApp(App):
    def build(self):
        root = Builder.load_string(KV)
        names = ["A", "B", "C"] 

   for name in names:
        from kivy.uix.label import Label
        label = Label(text=name)
        root.ids.main.add_widget(label)
        
        return root

if __name__ == '__main__':
    NameApp().run()
