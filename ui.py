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

    def getLink(self):
        link = self.enterLink.toPlainText()
        return link

    def startDownload(self):
        URL = self.getLink()
        with YoutubeDL(self.getOptions()) as ydl:
            ydl.download(URL)

    def video_exclusiveCheck(self):
        if self.videoOnlyCheck.isChecked() == True:
            self.audioOnlyCheck.setChecked(False)

    def audio_exclusiveCheck(self):
        if self.audioOnlyCheck.isChecked() == True:
            self.videoOnlyCheck.setChecked(False)

    def getOptions(self):
        if self.audioOnlyCheck.isChecked() == True:
            ydl_opts = {
                'format': 'bestaudio/best',
                'extractaudio': True,
                'audioformat': "mp3",
                'noplaylist': True
            }
        elif self.videoOnlyCheck.isChecked() == True:
            ydl_opts = {
                'format': 'bestvideo/best',
                'videoformat': "mp4",
                'noplaylist': True
            }
            return ydl_opts


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
