import sys
import os
from yt_dlp import YoutubeDL
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
import urllib.request
import qdarkstyle


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self)
        self.show()
        self.setWindowTitle("yt-dlp Media Downloader")
        self.downloadButton.setEnabled(False)
        self.downloadButton.clicked.connect(self.startDownload)
        self.videoOnlyCheck.toggled.connect(self.video_exclusiveCheck)
        self.audioOnlyCheck.toggled.connect(self.audio_exclusiveCheck)
        self.setDownload.clicked.connect(self.set_downloadLocation)
        self.checkLinkButton.clicked.connect(self.updateVideoData)
        self.setDownload.clicked.connect(self.set_downloadLocation)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)

    def updateVideoData(self):
        # try:
        r = self.checkLinkValid()

        if r['extractor_key'] == 'YoutubeTab' or r['extractor_key'] == 'BandcampAlbum':
            urllib.request.urlretrieve(
                r['entries'][0]['thumbnail'], "tempThumbnail.jpg")
            thumbnail = QPixmap("tempThumbnail.jpg")
            thumbnail = thumbnail.scaled(288, 162)
            self.imageLabel.setPixmap(thumbnail)
            self.titleLabel.setText(r['title'])
            self.titleLabel.setWordWrap(True)
            if r['extractor_key'] == 'YoutubeTab':
                self.lengthLabel.setText(
                    ("Playlist Count: ") + str(r['playlist_count']))
                self.uploaderLabel.setText(("Uploader: ") + r['uploader'])
                date = str(r['modified_date'])
                splitDate = date[:4] + "-" + date[4:6] + "-" + date[6:8]
                self.dateLabel.setText(("Last Modified: ") + splitDate)
                self.sourceLabel.setText(
                    ("Source Website: ") + r['extractor_key'])
            elif r['extractor_key'] == 'BandcampAlbum':
                self.lengthLabel.setText(
                    ("Track Count: ") + str(r['playlist_count']))
                self.uploaderLabel.setText(
                    ("Artist: ") + r['entries'][0]['uploader'])
                date = str(r['entries'][0]['upload_date'])
                splitDate = date[:4] + "-" + date[4:6] + "-" + date[6:8]
                self.dateLabel.setText(("Release Date: ") + splitDate)
                self.sourceLabel.setText(
                    ("Source Website: ") + r['extractor_key'])
        else:
            urllib.request.urlretrieve(r['thumbnail'], "tempThumbnail.jpg")
            thumbnail = QPixmap("tempThumbnail.jpg")
            thumbnail = thumbnail.scaled(288, 162)
            self.imageLabel.setPixmap(thumbnail)
            self.titleLabel.setText(r['title'])
            self.titleLabel.setWordWrap(True)
            self.lengthLabel.setText(("Duration: ") + r['duration_string'])
            self.uploaderLabel.setText(("Uploader: ") + r['uploader'])
            date = str(r['upload_date'])
            splitDate = date[:4] + "-" + date[4:6] + "-" + date[6:8]
            self.dateLabel.setText(("Upload Date: ") + splitDate)
            self.sourceLabel.setText(
                ("Source Website: ") + r['extractor_key'])

        self.formatSelectList.insertItem(0, "1080p (mp4)")
        self.formatSelectList.insertItem(1, "1080p (webm)")

        #URL = self.getLink()
        #ydl = YoutubeDL()
        # ydl_opts = {
        #    'listformats': True,
        # }
        # with YoutubeDL(ydl_opts) as ydl:
        #    ydl.download(URL)
        # except:
        # print("problem")

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
            self.downloadButton.setEnabled(True)
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

    def specify_downloadLocation(self):
        pass

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
                speed = round(speed, 2)
            elif speed is None:
                pass
            downloaded_percent = (
                response["downloaded_bytes"]*100)/response["total_bytes"]
            self.downloadProgress.setValue(downloaded_percent)
            self.speedLabel.setText(str(speed) + " MiB/s")
        elif response['status'] == "finished":
            self.downloadProgress.setValue(100)

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
                "progress_hooks": [self.progressUpdate],
                'audioformat': "mp3",
                'noplaylist': True
            }
            return ydl_opts

        elif self.videoOnlyCheck.isChecked() == True:
            ydl_opts = {
                'format': 'bestvideo/best',
                'outtmpl': location,
                "progress_hooks": [self.progressUpdate],
                'videoformat': "mp4",
                'noplaylist': True
            }
            return ydl_opts


app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())
window = Ui()
app.exec_()
