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
        self.checkLinkButton.clicked.connect(self.updateVideoData)
        self.formatSelectList.clicked.connect(self.getVideoF)
        self.formatSelectList2.clicked.connect(self.getAudioF)
        self.videoOnlyCheck.setDisabled(True)
        self.audioOnlyCheck.setDisabled(True)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        
    def updateVideoData(self):
        def formatUpdate():
            formats = r.get('formats', [r])
            for i in formats:
                if i['resolution'] != 'audio only':
                    self.formatSelectList.insertItem(0, i['format_id'] + " - " + i['format_note'] + " (" + i['ext'] + ")")
                elif i['resolution'] == 'audio only':
                    self.formatSelectList2.insertItem(0, i['format_id'] + " - " + i['format_note'] + " (" + i['ext'] + ")")
    
        try:
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
                formatUpdate()
            
        except:
            pass

    
    def getVideoF(self):
        videoF = self.formatSelectList.currentItem().text()
        videoF = videoF[0:3]
        return videoF

    def getAudioF(self):
        audioF = self.formatSelectList2.currentItem().text()
        audioF = audioF[0:3]
        return audioF
    
    def combineFormat(self):
        videoF = self.getVideoF()
        audioF = self.getAudioF()
        comboF = videoF + "+" + audioF
        return comboF

    def closeEvent(self, event):
        os.remove('tempThumbnail.jpg')

    def getLink(self):
        link = self.enterLink.text()
        return link

    def checkLinkValid(self):
        self.formatSelectList.clear()
        self.formatSelectList2.clear()
        self.videoOnlyCheck.setDisabled(False)
        self.audioOnlyCheck.setDisabled(False)
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
        location = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        location = location + '/%(title)s.%(ext)s'
        return location

    def video_exclusiveCheck(self):
        if self.videoOnlyCheck.isChecked() == True:
            self.formatSelectList.setDisabled(False)
            self.audioOnlyCheck.setChecked(False)
            self.formatSelectList2.setDisabled(True)
            if self.formatSelectList2.currentItem() != None:
                self.formatSelectList2.setCurrentItem(None)
        elif self.videoOnlyCheck.isChecked() == False:
            self.bothCheckOff()

    def audio_exclusiveCheck(self):
        if self.audioOnlyCheck.isChecked() == True:
            self.formatSelectList2.setDisabled(False)
            self.videoOnlyCheck.setChecked(False)
            self.formatSelectList.setDisabled(True)
            if self.formatSelectList.currentItem() != None:
                self.formatSelectList.setCurrentItem(None)
        elif self.audioOnlyCheck.isChecked() == False:
            self.bothCheckOff()
    
    def bothCheckOff(self):
        if self.videoOnlyCheck.isChecked() == False and self.audioOnlyCheck.isChecked() == False:
            self.formatSelectList.setDisabled(False)
            self.formatSelectList2.setDisabled(False)

    def progressUpdate(self, response):
        if 'playlist_count' in response['info_dict']:
            downloaded = 0
            if response["status"] == "downloading":
                speed = response["speed"]
                if speed != None:
                    speed = int(speed)
                    speed = speed/1024**2
                    speed = round(speed, 2)
                elif speed is None:
                    pass
                downloaded += 1
            if downloaded == response['info_dict']['playlist_count']:
                self.downloadProgress.setValue(100)
                print('worked')
            else:
                pass
        else:
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
                self.downloadProgress.setValue(int(downloaded_percent))
                self.speedLabel.setText(str(speed) + " MiB/s")
            elif response['status'] == "finished":
                self.downloadProgress.setValue(100)

    def getOptions(self, location):
        if self.audioOnlyCheck.isChecked() == False and self.videoOnlyCheck.isChecked() == False:
            try:
                comboF = self.combineFormat()
                ydl_opts = {
                    'format': comboF,
                    'outtmpl': location,
                    "progress_hooks": [self.progressUpdate],
                    'noplaylist': True
                }
                return ydl_opts
            except:
                ydl_opts = {
                    'format': 'bestvideo+bestaudio',
                    'outtmpl': location,
                    "progress_hooks": [self.progressUpdate],
                    'noplaylist': True
                }
                return ydl_opts

        elif self.audioOnlyCheck.isChecked() == True:
            try:
                audioF = self.getAudioF()
                ydl_opts = {
                    'format': audioF,
                    'outtmpl': location,
                    'extractaudio': True,
                    "progress_hooks": [self.progressUpdate],
                }
                return ydl_opts
            except:
                ydl_opts = {
                    'format': 'bestaudio',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }],
                    'outtmpl': location,
                    'extractaudio': True,
                    "progress_hooks": [self.progressUpdate],
                }
                return ydl_opts

        elif self.videoOnlyCheck.isChecked() == True:
            try:
                videoF = self.getVideoF()
                ydl_opts = {
                    'format': videoF,
                    'outtmpl': location,
                    "progress_hooks": [self.progressUpdate],
                    'noplaylist': True
                }
                return ydl_opts
            except:
                ydl_opts = {
                    'format': 'bestvideo',
                    'outtmpl': location,
                    'extractaudio': True,
                    "progress_hooks": [self.progressUpdate],
                }
                return ydl_opts


app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())
window = Ui()

if __name__ == '__main__':
    app.exec_()
