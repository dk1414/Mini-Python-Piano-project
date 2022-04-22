
from PyQt5 import QtCore, QtGui, QtWidgets
from pygame import mixer
import time

#designates different sound channels for each note
noteChannels = {'A':0,
                'B':1,
                'C':2,
                'D':3,
                'E':4,
                'F':5,
                'G':6,
                'Ab':7,
                'Bb':8,
                'Db':9,
                'Eb':10,
                'Gb':11}

#initializing sound mixer
mixer.init()
mixer.set_num_channels(12)

#plays sound when called, arguments determine what sound file is played and which sound channel each note goes to
def sound(note,octave,sustain):
    channel = 0

    if sustain:
        channel = noteChannels[note]

    mixer.Channel(channel).play(mixer.Sound(f'sounds/{note}{octave}.mp3'))
    print(f'{note}{octave}.mp3')

#gui stuff
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 417)
        MainWindow.setMaximumSize(650, 417)
        MainWindow.setStyleSheet("background-color: rgb(171, 171, 171);")
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QPushButton:hover{background-color:red;}")

        #default piano settings, playback will store the notes played when start recording is pressed and their respective timestamps
        self.octave = 4
        self.recording = False
        self.playBack = []
        self.sustain = False

        self.sustainButton = QtWidgets.QPushButton(self.centralwidget)
        self.sustainButton.setGeometry(QtCore.QRect(570, 47, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sustainButton.setFont(font)
        self.sustainButton.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.sustainButton.setObjectName("sustainButton")
        self.sustainButton.clicked.connect(lambda: self.clickedSustain())


        whiteKeysStyle = "background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n"







        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 75, 271))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(whiteKeysStyle)

        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.clickedKey(self.pushButton.text(),self.recording))


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 120, 75, 271))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(whiteKeysStyle)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.clickedKey(self.pushButton_2.text(),self.recording))

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 120, 75, 271))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(whiteKeysStyle)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.clickedKey(self.pushButton_3.text(),self.recording))

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 120, 75, 271))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(whiteKeysStyle)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.clickedKey(self.pushButton_4.text(),self.recording))

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 120, 75, 271))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(whiteKeysStyle)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.clickedKey(self.pushButton_5.text(),self.recording))

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 120, 75, 271))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_6.setStyleSheet(whiteKeysStyle)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.clickedKey(self.pushButton_6.text(),self.recording))

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 120, 75, 271))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(whiteKeysStyle)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.clickedKey(self.pushButton_7.text(),self.recording))

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 120, 41, 151))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: self.clickedKey(self.pushButton_8.text(),self.recording))

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 120, 41, 151))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.clickedKey(self.pushButton_9.text(),self.recording))

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 120, 41, 151))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: self.clickedKey(self.pushButton_10.text(),self.recording))

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(355, 120, 41, 151))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda: self.clickedKey(self.pushButton_11.text(),self.recording))

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(425, 120, 41, 151))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda: self.clickedKey(self.pushButton_12.text(),self.recording))

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 229, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.TransposeL = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TransposeL.setFont(font)
        self.TransposeL.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.TransposeL.setObjectName("TransposeL")
        self.TransposeL.clicked.connect(lambda: (self.changeOctave(-1)) if self.octave > 1 else None)

        self.horizontalLayout.addWidget(self.TransposeL)

        self.TransposeR = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.TransposeR.setFont(font)
        self.TransposeR.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.TransposeR.setObjectName("TransposeR")
        self.TransposeR.clicked.connect(lambda: (self.changeOctave(1)) if self.octave < 7 else None)

        self.horizontalLayout.addWidget(self.TransposeR)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(260, 20, 291, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.StartRecording = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.StartRecording.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.StartRecording.setObjectName("StartRecording")
        self.StartRecording.clicked.connect(lambda: self.clickedRecord())

        self.horizontalLayout_2.addWidget(self.StartRecording)

        self.StopRecording = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.StopRecording.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.StopRecording.setObjectName("StopRecording")
        self.StopRecording.clicked.connect(lambda: self.clickedStop())

        self.horizontalLayout_2.addWidget(self.StopRecording)

        self.Playback = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Playback.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.Playback.setObjectName("Playback")
        self.Playback.clicked.connect(lambda: self.clickedPlayback())

        self.horizontalLayout_2.addWidget(self.Playback)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_12.raise_()
        self.pushButton_11.raise_()
        self.pushButton_10.raise_()
        self.pushButton_9.raise_()
        self.pushButton_8.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini Piano"))
        self.pushButton.setText(_translate("MainWindow", "C"))
        self.pushButton_2.setText(_translate("MainWindow", "D"))
        self.pushButton_3.setText(_translate("MainWindow", "F"))
        self.pushButton_4.setText(_translate("MainWindow", "E"))
        self.pushButton_5.setText(_translate("MainWindow", "A"))
        self.pushButton_6.setText(_translate("MainWindow", "G"))
        self.pushButton_7.setText(_translate("MainWindow", "B"))
        self.pushButton_8.setText(_translate("MainWindow", "Db"))
        self.pushButton_9.setText(_translate("MainWindow", "Eb"))
        self.pushButton_10.setText(_translate("MainWindow", "Gb"))
        self.pushButton_11.setText(_translate("MainWindow", "Ab"))
        self.pushButton_12.setText(_translate("MainWindow", "Bb"))
        self.label.setText(_translate("MainWindow", "Shift Octave"))
        self.TransposeL.setText(_translate("MainWindow", "<"))
        self.TransposeR.setText(_translate("MainWindow", ">"))
        self.label_2.setText(_translate("MainWindow", "Record"))
        self.StartRecording.setText(_translate("MainWindow", "Start"))
        self.StopRecording.setText(_translate("MainWindow", "Stop"))
        self.Playback.setText(_translate("MainWindow", "Playback"))
        self.sustainButton.setText(_translate("MainWindow", "Sustain"))

    #function connected to each key, calls sound, and if recording, it adds notes played to the playback list
    def clickedKey(self,note,recording):

        if recording:
            self.playBack.append([note,time.time()])

        sound(note, self.octave,self.sustain)

    #starts recording
    def clickedRecord(self):
        if len(self.playBack) > 0:
            self.playBack = []

        self.recording = True

    #ends recording
    def clickedStop(self):
        self.recording = False

    #plays notes in the playback list separated by the difference of their timestamps
    def clickedPlayback(self):


        for i,note in enumerate(self.playBack):
            interval = 0


            if i != len(self.playBack) - 1:

                nextNote = self.playBack[i + 1]

                interval = nextNote[1] - note[1]


            sound(note[0],self.octave,self.sustain)
            time.sleep(interval)



    #shifts octave
    def changeOctave(self,num):
        self.octave = self.octave + num

    #changes sustain
    def clickedSustain(self):
        self.sustain = not self.sustain
        print(self.sustain)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
