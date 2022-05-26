import sys
import os
from yt_dlp import YoutubeDL
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
import urllib.request


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self)
        self.show()
        self.setWindowTitle("yt-dlp Media Downloader")
        self.downloadButton.clicked.connect(self.startDownload)
        self.videoOnlyCheck.toggled.connect(self.video_exclusiveCheck)
        self.audioOnlyCheck.toggled.connect(self.audio_exclusiveCheck)
        self.setDownload.clicked.connect(self.set_downloadLocation)
        self.checkLinkButton.clicked.connect(self.updateVideoData)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        
    def updateVideoData(self):
        r = self.checkLinkValid()
        urllib.request.urlretrieve(r['thumbnail'], "tempThumbnail.jpg")
        thumbnail = QPixmap("tempThumbnail.jpg")
        thumbnail = thumbnail.scaled(288, 162)
        self.imageLabel.setPixmap(thumbnail)
    
        URL = self.getLink()
        ydl = YoutubeDL()
        ydl_opts = {
            'listformats': True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URL)
        self.formatSelectList.insertItem(0, "1080p (mp4)")
        self.formatSelectList.insertItem(1, "1080p (webm)")

    def closeEvent(self, event):
        os.remove('tempThumbnail.jpg')
    
    def getLink(self):
        link = self.enterLink.text()
        return link

    def checkLinkValid(self):
        URL = self.getLink()
        ydl = YoutubeDL()
        try:
            infoList = ydl.extract_info(URL, download=False)
            return infoList
        except:
            errorBox = QMessageBox()
            errorBox.setWindowTitle("Error")
            errorBox.setText("Invalid Link!")
            errorBox.setIcon(QMessageBox.Critical)
            errorBox.exec_()

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

    def progressUpdate(self, response):
        if response["status"] == "downloading":
            speed = response["speed"]
            if speed != None:
                speed = int(speed)
                speed = speed/1024**2
            elif speed is None:
                pass
            downloaded_percent = (response["downloaded_bytes"]*100)/response["total_bytes"]
            self.downloadProgress.setValue(downloaded_percent)
            self.speedLabel.setText(str(speed) + "Mb/s")

    def getOptions(self, location):
        if self.audioOnlyCheck.isChecked() == False and self.videoOnlyCheck.isChecked() == False:
            ydl_opts = {
                'outtmpl': location,
                "progress_hooks": [self.progressUpdate],
            }
            return ydl_opts

        elif self.audioOnlyCheck.isChecked() == True:
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
