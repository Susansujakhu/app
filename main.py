import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from data import DataBase
import datetime
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Add_User(Screen):
    namee = ObjectProperty(None)
    address = ObjectProperty(None)
    contact = ObjectProperty(None)
    salary = ObjectProperty(None)

    def adduser(self):
        db.add_users(self.namee.text, self.address.text, self.contact.text, self.salary.text)
        #sm.current = "view"
        pop = Popup(title='Success',
            content=Label(text='User Successfully Added'),
            size_hint=(None, None), size=(200, 200))
        pop.open()

        self.reset()

    def reset(self):
        self.namee.text = ""
        self.address.text = ""
        self.contact.text = ""
        self.salary.text = ""
    




class View_User(Screen):
    #sm.current = "view"
    '''
    def on_enter(self):
        rows = db.count_rows()

        for i in range(rows):
            i += 1
            name, address, contact, salary = db.view_users(i)
            self.add_widget(Label(text = name))
            print(name)
    
'''
    def __init__(self, **kwargs):
        super(View_User,self).__init__()
        rows = db.count_rows()
        for i in range(rows):
            i += 1
            name, address, contact, salary = db.view_users(i)
            self.ids.container_y.add_widget(Label(text=name))
            self.ids.container_y.add_widget(Label(text=address))
            self.ids.container_y.add_widget(Label(text=contact))
            self.ids.container_y.add_widget(Label(text=salary))

        self.ids.delete_btn.text = "Delete"
        self.ids.edit_btn.text = "Edit"



    


class WindowManager(ScreenManager):
    pass
db = DataBase()

sm = WindowManager()
kv = Builder.load_file("my.kv")


screens = [Add_User(name="add"), View_User(name="view")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "add"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()