from kivymd.app import MDApp
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder



class KivyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('kivyapp.kv')


class MobileView(MDScreen):
    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()

if __name__ == '__main__':
    KivyApp().run()
