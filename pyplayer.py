# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# ­*­coding: utf­8 ­*­
from PyQt4.QtGui import*
from PyQt4.QtCore import*
from PyQt4.phonon import Phonon
import sys
class window(QMainWindow):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        _VERSION_=0.1
        #-----------window setting--------------
        self.setWindowTitle('QPlayer')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(50, 50, 700,680)
        self.setFixedSize(700,680)
        
        #self.setStyleSheet('background-color:#383636;')
        #--------ToolBar setting-------------------------
        toolbar=self.addToolBar('')
        open=QAction(QIcon('open.png'),'open file',self)
        About=QAction('About',self)
        quit=QAction('Quit',self)
        toolbar.addAction(open)
        toolbar.addAction(About)
        toolbar.addAction(quit)
        open.triggered.connect(self.open_file)
        quit.triggered.connect(self.exiting)
        toolbar.setMovable(False)
        toolbar.setFocusPolicy(True)
	#---------Phonon source--------------------
        self.media = Phonon.MediaObject(self)
        self.media.stateChanged.connect(self.statech)
        self.video= Phonon.VideoWidget(self)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        self.video.setGeometry(20,50,660,400)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)
        #---------Slider--------------------------
        self.slider=Phonon.SeekSlider(self)
        self.slider.setMediaObject(self.media)
        self.slider.setGeometry(20,460,660,20)
        #--------Frame------------------------
        self.frame=QFrame(self)
        self.frame.setGeometry(20,498,660,20)
        self.frame.setStyleSheet("background-color:#1A2938;")
        
        #--------Label -----------------
        self.label=QLabel(self)
        self.label.move(20,495)
        self.label.setText("<font color='White'>Volume :</font>")
        #----------Volume----------------------------------------
        self.volumeslider=Phonon.VolumeSlider(self)
        self.volumeslider.setAudioOutput(self.audio)
        self.volumeslider.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.volumeslider.setGeometry(195,500,150,20)
        #-----------Button play---------------------
        self.button_play=QPushButton('Play',self)
        self.button_play.move(20,530)
        self.button_play.clicked.connect(self.playing)
        self.button_play.setStyleSheet('background-color:#070D14;')
	#----------------------------------------------------------
        
	#-------Button pause-------------------
        
        self.button_paus=QPushButton('Pause',self)
        self.button_paus.move(130,530)
        self.button_paus.clicked.connect(self.pausing)
        self.button_paus.setStyleSheet('background-color:#D73434;')
        #----------Button FullScreen watch----------------------
        self.button_full=QPushButton('Fullscreen',self)
        self.button_full.move(240,530)
        self.button_full.clicked.connect(self.fullscreen)
        self.show()
    #---------Open File Dialogue-----------------------
    def open_file(self,newState):
        if self.media.state() == Phonon.PlayingState:
            self.media.play()
            self.button_play.setEnabled(True)
            
        else:
            path = QFileDialog.getOpenFileName(self)
            if path:
                
                self.media.setCurrentSource(Phonon.MediaSource(path))
        
    #----------------------------------------------------------------
    def statech(self,newstate,oldstate):
        try:
            if newstate == Phonon.PlayingState:
                self.button_play.setEnabled(False)
            elif (newstate != Phonon.LoadingState and newstate != Phonon.BufferingState):
                self.button_play.setEnabled(True)
                
            if newstate == Phonon.ErrorState:
                pass
        except AttributeError:
            pass

        
                
    #-------------Quit Main Window setting--------------------            
    def exiting(self):
        self.media.stop()
        self.close()
    #------Play media setting----------------------------
    def playing(self):
        self.media.play()
        self.button_play.setFocusPolicy(False)
    #------Pause Media-------------------------------------
    def pausing(self):
        self.media.pause()
    #---------Full screen setting---------------------
    def fullscreen(self):
        self.video.setGeometry(20,50,680,680)
        self.slider.move(20,560)
        self.volumeslider.move(195,585)
        self.label.move(20,580)
        self.frame.move(20,585)
        self.button_play.move(20,630)
        self.button_paus.move(130,630)
        self.button_full.move(240,630)

#------------Execute all function(app)------------------        
if __name__ == '__main__':
    app = QApplication([])
    gui = window()
    app.exec_()