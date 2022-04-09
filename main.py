from kivy.app import App
from ftplib import FTP


class ServerApp(App):
    ftp = None

    def build(self):
        self.ftp = FTP('89.223.37.253')


if __name__ == "__main__":
    ServerApp().run()
