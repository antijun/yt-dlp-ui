# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\David\Documents\GitHub\yt-dlp-ui\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(679, 570)
        self.downloadButton = QtWidgets.QPushButton(Widget)
        self.downloadButton.setGeometry(QtCore.QRect(320, 460, 351, 61))
        self.downloadButton.setObjectName("downloadButton")
        self.formatSelectList = QtWidgets.QListWidget(Widget)
        self.formatSelectList.setGeometry(QtCore.QRect(10, 230, 291, 290))
        self.formatSelectList.setObjectName("formatSelectList")
        self.imageLabel = QtWidgets.QLabel(Widget)
        self.imageLabel.setGeometry(QtCore.QRect(10, 50, 291, 162))
        self.imageLabel.setObjectName("imageLabel")
        self.speedLabel = QtWidgets.QLabel(Widget)
        self.speedLabel.setGeometry(QtCore.QRect(320, 410, 100, 30))
        self.speedLabel.setObjectName("speedLabel")
        self.videoQualityCB = QtWidgets.QComboBox(Widget)
        self.videoQualityCB.setGeometry(QtCore.QRect(320, 310, 351, 41))
        self.videoQualityCB.setObjectName("videoQualityCB")
        self.audioOnlyCheck = QtWidgets.QCheckBox(Widget)
        self.audioOnlyCheck.setGeometry(QtCore.QRect(330, 390, 91, 22))
        self.audioOnlyCheck.setObjectName("audioOnlyCheck")
        self.downloadProgress = QtWidgets.QProgressBar(Widget)
        self.downloadProgress.setGeometry(QtCore.QRect(320, 430, 351, 23))
        self.downloadProgress.setProperty("value", 0)
        self.downloadProgress.setTextVisible(True)
        self.downloadProgress.setObjectName("downloadProgress")
        self.videoOnlyCheck = QtWidgets.QCheckBox(Widget)
        self.videoOnlyCheck.setGeometry(QtCore.QRect(330, 360, 81, 22))
        self.videoOnlyCheck.setObjectName("videoOnlyCheck")
        self.checkLinkButton = QtWidgets.QPushButton(Widget)
        self.checkLinkButton.setGeometry(QtCore.QRect(319, 270, 351, 30))
        self.checkLinkButton.setObjectName("checkLinkButton")
        self.setDownload = QtWidgets.QPushButton(Widget)
        self.setDownload.setGeometry(QtCore.QRect(370, 530, 251, 21))
        self.setDownload.setObjectName("setDownload")
        self.enterLink = QtWidgets.QLineEdit(Widget)
        self.enterLink.setGeometry(QtCore.QRect(320, 230, 351, 31))
        self.enterLink.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.enterLink.setAutoFillBackground(False)
        self.enterLink.setObjectName("enterLink")
        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(330, 50, 331, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.titleLabel = QtWidgets.QLabel(Widget)
        self.titleLabel.setGeometry(QtCore.QRect(330, 20, 331, 20))
        self.titleLabel.setText("")
        self.titleLabel.setObjectName("titleLabel")
        self.lengthLabel = QtWidgets.QLabel(Widget)
        self.lengthLabel.setGeometry(QtCore.QRect(328, 80, 331, 20))
        self.lengthLabel.setText("")
        self.lengthLabel.setObjectName("lengthLabel")
        self.uploaderLabel = QtWidgets.QLabel(Widget)
        self.uploaderLabel.setGeometry(QtCore.QRect(330, 120, 331, 20))
        self.uploaderLabel.setText("")
        self.uploaderLabel.setObjectName("uploaderLabel")
        self.dateLabel = QtWidgets.QLabel(Widget)
        self.dateLabel.setGeometry(QtCore.QRect(330, 160, 331, 16))
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")
        self.sourceLabel = QtWidgets.QLabel(Widget)
        self.sourceLabel.setGeometry(QtCore.QRect(330, 190, 331, 16))
        self.sourceLabel.setText("")
        self.sourceLabel.setObjectName("sourceLabel")
        self.line_2 = QtWidgets.QFrame(Widget)
        self.line_2.setGeometry(QtCore.QRect(330, 210, 331, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.downloadButton.setText(_translate("Widget", "Start Download"))
        self.audioOnlyCheck.setText(_translate("Widget", "Audio Only"))
        self.videoOnlyCheck.setText(_translate("Widget", "Video Only"))
        self.checkLinkButton.setText(_translate("Widget", "Check Link"))
        self.setDownload.setText(_translate("Widget", "Set Download Location"))
        self.enterLink.setText(_translate("Widget", "Enter Link"))
