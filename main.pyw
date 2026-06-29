import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
from bs4 import BeautifulSoup
import re
import urllib3

url = 'https://sts-h.goesn.kr/sts-h/main.do'
res = requests.get(url, verify=False)
pattern = r'\([^)]*\)|\+|\.|ㆍ'

def meal_list():
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
    if not soup.find('dd', class_='meal_list'):
        return "오늘은 급식이 없습니다."
    else:
        todayMeal = soup.find('dd', class_='meal_list').string
        todayMeal = re.sub(pattern=pattern, repl='', string=todayMeal)
        todayMeal = re.sub(r"\s+&", '&', todayMeal)
        todayMeal = re.sub(r"\s+:.*", '\n', todayMeal)
        todayMeal = re.sub(r"\s+", '\n', todayMeal)
        todayMeal = todayMeal + "\n"
        todayMeal = todayMeal.rstrip('\n')
        return todayMeal

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)
            
    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

        
    def init_ui(self):
        layout = QVBoxLayout()
        self.setWindowTitle('오늘의 급식')
        
        label_widget = QLabel(meal_list())
        label_widget.setStyleSheet("color: #fff; font-weight:bold;border:3px solid #fff; background-color: rgba( 0, 0, 0, 0.5 );padding:13px;")
        #font = label_widget.font()
        #font.setPointSize(25)
        #label_widget.setFont(font)
        label_widget.setFont(QFont('굴림', 25))
        #label_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        
        layout.addWidget(label_widget)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setLayout(layout)
        self.resize(1, 1)
        #self.move(1420, 0)
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    
    main = Main()
    sys.exit(app.exec_())
