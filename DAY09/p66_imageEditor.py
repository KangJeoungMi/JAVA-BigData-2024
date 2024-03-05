# file : p66_imageEditor.py
# desc : PyQt 이미지 에디터
'''
qrc 파일을 사용하려면
> pyrcc5 "resources.qrc" -o "resources_rc.py"
'''

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
# 리소스 파일 추가
import resource_rc
# openCv 추가
import cv2

class WinApp(QMainWindow):   # QWidget이 아님!
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()
        
    def initUI(self):
        uic.loadUi('./day09/pyNewPaint.ui', self)
        self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.setWindowTitle('이미지 에디터 v0.5')
        ## 이미지 추가 / 여러가지 UI에 대한 초기화
        pixmap = QPixmap('./DAY09/imgs/panda.jpg').scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        
        self.BColor = Qt.red # 빨강이 기본
         
        
       # UI 초기화 끝 
        self.show()
        
    def initSignal(self):
        # 메뉴/툴바 액션에 대한 시그널 처리함수 선언
        self.action_NEW.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Exit.triggered.connect(self.actionExitClicked)
        self.actionRED_Red.triggered.connect(self.actionPenRedClicked)
        self.actionGreen_Green.triggered.connect(self.actionPenGreenClicked)
        self.actionBLUE_Blue.triggered.connect(self.actionPenBlueClicked)
        self.action_action.triggered.connect(self.actionAboutClicked)
        # 변환메뉴 추가
        self.action_G.triggered.connect(self.actionGrayscaleClicked)
        
                
    def actionGrayscaleClicked(self):
        return
        
        
    def actionNewClicked(self):
        canvas = QPixmap(self.lblCanvas.width(),self.lblCanvas.height())
        canvas.fill(QColor('white'))
        self.lblCanvas.setPixmap(canvas)
                 
    def actionOpenClicked(self):
        image = QFileDialog.getOpenFileName(self,'이미지 열기','','Image file(*.jpg; *.png; *gif;)')
        imagepath = image[0]
        pixmap = QPixmap(imagepath).scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.lblCanvas.adjustSize()
        
    def actionSaveClicked(self):
        filePath, _ =QFileDialog.getSaveFileName(self,'이미지 저장','','Image file(*.jpg; *.png; *gif;)')
        if filePath == '': return
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(filePath )
        
    def actionExitClicked(self):
       exit(0)
        
    def actionPenRedClicked(self):
        self.BColor = Qt.red
        
    def actionPenGreenClicked(self):
        self.BColor = Qt.green
        
    def actionPenBlueClicked(self):
        self.BColor = Qt.blue
        
    def actionAboutClicked(self):
        QMessageBox.about(self, '알림', '프로그램 정보')
        
    def mouseMoveEvent(self,e) -> None:
        print(e.x(),e.y()-50)
        brush = QPainter(self.lblCanvas.pixmap()) # lblCanvas에 브러쉬 하나 생성
        brush.setPen(QPen(self.BColor,3.5, style=Qt.SolidLine,cap=Qt.RoundCap))        
        brush.drawPoint(e.x(),e.y()-50)
        brush.end()
        self.update()
        
        
    def closeEvent(self, a0: QCloseEvent | None) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: QCloseEvent.accept()
        else:QCloseEvent.ignore()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())