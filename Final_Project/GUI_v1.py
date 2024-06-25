from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1000)
        MainWindow.setStyleSheet("""
            QWidget{
                background-color: #3C3C3C;                    
            }
            QLabel{
                color:white;
                font-size:16px;
                font-weight:bold;
                border:2px solid #FFE4CA;
                text-align:center;
            }
            QLineEdit {
                border: 2px solid gray;
                border-radius: 10px;
                font-size:16px;
                padding: 0 8px;
                background: #FFEEDD;
                selection-background-color: darkgray;
            }
            QMenuBar {
                background-color: qlineargradient(x1:0, y1:0, x2:10, y2:5,
                                                stop:0 	#F0F0F0, stop:1 #000000	);
                spacing: 5px;
            }
            QMenuBar::item {
                padding: 1px 6px;
                background: transparent;
                border-radius: 4px;
            }
            QMenuBar::item:selected {
                background: #5B5B5B;
            }
            QMenuBar::item:pressed {
                background: #FFBB77;
            }
        """)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1200, 250))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_Ky = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Ky.setObjectName("label_Ky")
        self.gridLayout.addWidget(self.label_Ky, 2, 2, 1, 1)
        self.lineEdit_Ky = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Ky.setObjectName("lineEdit_Ky")
        self.gridLayout.addWidget(self.lineEdit_Ky, 2, 3, 1, 1)
        
        # 讓使用者輸入參數的UI
        self.label_ny = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ny.setObjectName("label_ny")
        self.gridLayout.addWidget(self.label_ny, 4, 0, 1, 1)
        self.lineEdit_ny = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ny.setObjectName("lineEdit_ny")
        self.gridLayout.addWidget(self.lineEdit_ny, 4, 1, 1, 1)
        
        self.label_nx = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_nx.setObjectName("label_nx")
        self.gridLayout.addWidget(self.label_nx, 3, 0, 1, 1)
        self.lineEdit_nx = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_nx.setObjectName("lineEdit_nx")
        self.gridLayout.addWidget(self.lineEdit_nx, 3, 1, 1, 1)
        
        self.label_ly = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ly.setObjectName("label_ly")
        self.gridLayout.addWidget(self.label_ly, 2, 0, 1, 1)
        self.lineEdit_Ly = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Ly.setObjectName("lineEdit_Ly")
        self.gridLayout.addWidget(self.lineEdit_Ly, 2, 1, 1, 1)
        self.lineEdit_Ly.setReadOnly(True)
        self.lineEdit_Ly.setStyleSheet("""
            QLineEdit[readOnly="true"] { color: gray }
        """)
        
        self.label_Kx = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Kx.setObjectName("label_Kx")
        self.gridLayout.addWidget(self.label_Kx, 1, 2, 1, 1)
        self.lineEdit_Kx = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Kx.setObjectName("lineEdit_Kx")
        self.gridLayout.addWidget(self.lineEdit_Kx, 1, 3, 1, 1)
        
        self.label_b = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_b.setObjectName("label_b")
        self.gridLayout.addWidget(self.label_b, 3, 4, 1, 1)
        self.lineEdit_b = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.gridLayout.addWidget(self.lineEdit_b, 3, 5, 1, 1)
        
        self.label_lx = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_lx.setObjectName("label_lx")
        self.gridLayout.addWidget(self.label_lx, 1, 0, 1, 1)
        self.lineEdit_Lx = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Lx.setObjectName("lineEdit_Lx")
        self.gridLayout.addWidget(self.lineEdit_Lx, 1, 1, 1, 1)

        self.label_nt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_nt.setObjectName("label_nt")
        self.gridLayout.addWidget(self.label_nt, 1, 4, 1, 1)
        self.lineEdit_nt = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_nt.setObjectName("lineEdit_nt")
        self.gridLayout.addWidget(self.lineEdit_nt, 1, 5, 1, 1)
        
        self.label_dt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_dt.setObjectName("label_dt")
        self.gridLayout.addWidget(self.label_dt, 2, 4, 1, 1)
        self.lineEdit_dt = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_dt.setObjectName("lineEdit_dt")
        self.gridLayout.addWidget(self.lineEdit_dt, 2, 5, 1, 1)
        
        self.label_wx = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wx.setObjectName("label_wx")
        self.gridLayout.addWidget(self.label_wx, 3, 2, 1, 1)
        self.lineEdit_wx = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_wx.setObjectName("lineEdit_wx")
        self.gridLayout.addWidget(self.lineEdit_wx, 3, 3, 1, 1)
        
        self.label_wy = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wy.setObjectName("label_wy")
        self.gridLayout.addWidget(self.label_wy, 4, 2, 1, 1)
        self.lineEdit_wy = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_wy.setObjectName("lineEdit_wy")
        self.gridLayout.addWidget(self.lineEdit_wy, 4, 3, 1, 1)
        
        self.label_Q = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Q.setObjectName("label_Q")
        self.gridLayout.addWidget(self.label_Q, 1, 6, 1, 1)
        self.lineEdit_Q = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Q.setObjectName("lineEdit_Q")
        self.gridLayout.addWidget(self.lineEdit_Q, 1, 7, 1, 1)

        self.label_rw = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_rw.setObjectName("label_rw")
        self.gridLayout.addWidget(self.label_rw, 2, 6, 1, 1)
        self.lineEdit_rw = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_rw.setObjectName("lineEdit_rw")
        self.gridLayout.addWidget(self.lineEdit_rw, 2, 7, 1, 1)
        
        self.label_h0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_h0.setObjectName("label_h0")
        self.gridLayout.addWidget(self.label_h0, 3, 6, 1, 1)
        self.lineEdit_h0 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_h0.setObjectName("lineEdit_h0")
        self.gridLayout.addWidget(self.lineEdit_h0, 3, 7, 1, 1)
        
        self.label_Ss = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Ss.setObjectName("label_Ss")
        self.gridLayout.addWidget(self.label_Ss, 4, 4, 1, 1)
        self.lineEdit_Ss = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Ss.setObjectName("lineEdit_Ss")
        self.gridLayout.addWidget(self.lineEdit_Ss, 4, 5, 1, 1)
        
        self.label_slider = QtWidgets.QLabel(self.centralwidget)
        self.label_slider.setGeometry(QtCore.QRect(400, 800, 80, 30))
        self.label_slider.setStyleSheet("""
            QLabel{
                font-size: 20px;
                font-weight: bold;
                color: white;
            }
        """)
        self.label_slider.setObjectName("label_slider")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(500, 800, 600, 30))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 10px;
                background: #D0D0D0	;
                margin: 4px 0;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #8f8f91;
                border: 1px solid #5c5c5c;
                width: 18px;
                height: 28px;
                margin: -10px 0;
                border-radius: 9px;
            }
            QSlider::handle:horizontal:hover {
                background: black;
                border: 1px solid #3c3c3c;
            }
            QSlider::sub-page:horizontal {
                background: #ffb556;
                border: 1px solid #777;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::add-page:horizontal {
                background: #e0e0e0;
                border: 1px solid #777;
                height: 8px;
                border-radius: 4px;
            }
        """)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1300, 80, 180, 60))
        # self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        # self.gridLayout.addWidget(self.pushButton, 4, 7, , 2)
        self.pushButton.setStyleSheet("""
            QPushButton{
                background-color: white;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: black;
                font: 20px;
                min-width: 10em;
                padding: 6px;                          
            }
            QPushButton:hover{
                background-color: #FFFF93;
                border-width: 4px;                  
            }
            QPushButton:pressed{
                background-color: #EA0000;
            }
        """)

        # 進度條
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(500, 860, 600, 30))
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #000;
                border-radius: 5px;
                text-align:center;
                height: 30px;
                width:80px;
            }
            QProgressBar::chunk {
                background-color: #CD96CD;
                width: 10px;
                margin: 0.5px;
            }
        """)

        # 三維模擬
        self.verticalLayoutWidget_plot = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_plot.setGeometry(QtCore.QRect(40, 260, 500, 500))
        self.verticalLayout_plot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_plot)
        self.verticalLayout_plot.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_plot.setObjectName("verticalLayout_plot")

        # 二維模擬剖面
        self.verticalLayoutWidget_slice = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_slice.setGeometry(QtCore.QRect(550, 260, 500, 500))
        self.verticalLayout_slice = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_slice)
        self.verticalLayout_slice.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_slice.setObjectName("verticalLayout_slice")

        self.verticalLayoutWidget_theis = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_theis.setGeometry(QtCore.QRect(1060, 260, 500, 500))
        self.verticalLayout_theis = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_theis)
        self.verticalLayout_theis.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_theis.setObjectName("verticalLayout_theis")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menu.addAction(self.actionSave)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "地下水水位模擬系統"))
        MainWindow.setWindowIcon(QIcon('main.ico')) 
        self.label_Ky.setText(_translate("MainWindow", "Ky(含水層y向導水係數)："))
        self.label_ny.setText(_translate("MainWindow", "ny(含水層y方向空間步數)："))
        self.label_nx.setText(_translate("MainWindow", "nx(含水層x方向空間步數)："))
        self.label_b.setText(_translate("MainWindow", "b(含水層厚度)："))
        self.label_lx.setText(_translate("MainWindow", "Lx(含水層x方向長度)："))
        self.label_Kx.setText(_translate("MainWindow", "Kx(含水層x向導水係數)："))
        self.label_ly.setText(_translate("MainWindow", "Ly(含水層y方向長度)："))
        self.label_nt.setText(_translate("MainWindow", "nt(時間步數)："))
        self.label_dt.setText(_translate("MainWindow", "dt(時間步長)："))
        self.label_wx.setText(_translate("MainWindow", "wx(水井x座標)："))
        self.label_wy.setText(_translate("MainWindow", "wy(水井y座標)："))
        self.label_Q.setText(_translate("MainWindow", "Q(抽水量)："))
        self.label_rw.setText(_translate("MainWindow", "rw(井的半徑)："))
        self.label_h0.setText(_translate("MainWindow", "h0(初始水位高度)："))
        self.label_Ss.setText(_translate("MainWindow", "Ss(比儲率)："))
        self.pushButton.setText(_translate("MainWindow", "模擬"))
        self.menu.setTitle(_translate("MainWindow", "檔案"))
        self.actionSave.setText(_translate("MainWindow", "Save As"))
        self.lineEdit_b.setText(_translate("MainWindow", "50"))
        self.lineEdit_dt.setText(_translate("MainWindow", "0.1")) 
        self.lineEdit_Lx.setText(_translate("MainWindow", "1000"))
        self.lineEdit_Ly.setText(_translate("MainWindow", "1000"))
        self.lineEdit_nx.setText(_translate("MainWindow", "100"))
        self.lineEdit_ny.setText(_translate("MainWindow", "100"))
        self.lineEdit_nt.setText(_translate("MainWindow", "200"))
        self.lineEdit_Ss.setText(_translate("MainWindow", "1e-4"))
        self.lineEdit_Kx.setText(_translate("MainWindow", "1e-4")) 
        self.lineEdit_Ky.setText(_translate("MainWindow", "1e-4")) 
        self.lineEdit_Q.setText(_translate("MainWindow", "0.1"))
        self.lineEdit_wx.setText(_translate("MainWindow", "50"))
        self.lineEdit_wy.setText(_translate("MainWindow", "50"))
        self.lineEdit_rw.setText(_translate("MainWindow", "0.1"))
        self.lineEdit_h0.setText(_translate("MainWindow", "50"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
