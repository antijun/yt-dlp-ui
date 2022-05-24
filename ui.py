import sys
import os
from yt_dlp import YoutubeDL
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self)
        self.show()
        self.downloadButton.clicked.connect(self.startDownload)
        self.videoOnlyCheck.toggled.connect(self.video_exclusiveCheck)
        self.audioOnlyCheck.toggled.connect(self.audio_exclusiveCheck)
        self.setDownload.clicked.connect(self.set_downloadLocation)

    def getLink(self):
        link = self.enterLink.text()
        return link

    def startDownload(self):
        URL = self.getLink()
        with YoutubeDL(self.getOptions(self.set_downloadLocation())) as ydl:
            ydl.download(URL)

    def set_downloadLocation(self):
        location = 'downloads/%(title)s.%(ext)s'
        return location

    def video_exclusiveCheck(self):
        if self.videoOnlyCheck.isChecked() == True:
            self.audioOnlyCheck.setChecked(False)

    def audio_exclusiveCheck(self):
        if self.audioOnlyCheck.isChecked() == True:
            self.videoOnlyCheck.setChecked(False)

    def getOptions(self, location):
        if self.audioOnlyCheck.isChecked() == True:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': location,
                'extractaudio': True,
                'audioformat': "mp3",
                'noplaylist': True
            }
            return ydl_opts
        elif self.videoOnlyCheck.isChecked() == True:
            ydl_opts = {
                'format': 'bestvideo/best',
                'outtmpl': location,
                'videoformat': "mp4",
                'noplaylist': True
            }
            return ydl_opts


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
