import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import sys
import scipy.special as sp
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from GUI_v1 import Ui_MainWindow
from PyQt5.QtGui import QIcon


"""
lx, ly : 模擬地下水空間長與寬大小(m)
b : 含水層厚度(m)
nx, ny : 空間步數(節點數)
dx, dy : 空間步長(m)
nt : 時間步數
dt : 時間步長(s)
Ss : 比儲率(m^-1)
S : 儲水係數
Tx, Ty : 透水係數(m^2/s)
Kx, Ky : 導水係數(m/s)
Q : 水井抽水量(m^3 / s)
wx : 井x座標
wy : 井y座標
rw : 井口半徑(m)
A : 井周圍的影響區域面積
h0 : 初始水面高度
"""

class GroundWater(QMainWindow, Ui_MainWindow):
    def __init__(self, lx, ly, b, nx, ny, nt, dt, Ss, Kx, Ky, Q, wx, wy, rw, h0):
        super().__init__()
        self.setupUi(self)

        # 參數設定
        self.lx = lx
        self.ly = ly
        self.b = b
        self.nx = nx
        self.ny = ny
        self.dx = lx / (nx - 1)
        self.dy = ly / (ny - 1)
        self.nt = nt
        self.dt = dt
        self.Ss = Ss
        self.S = Ss * b
        self.Kx = Kx
        self.Ky = Ky
        self.Q = Q
        self.Tx = Kx * b
        self.Ty = Ky * b
        self.wx = wx
        self.wy = wy
        self.rw = rw
        self.h0 = h0
        self.A = np.pi * rw**2

        # 初始條件
        self.h = np.full((nt+1, nx, ny), h0)
        self.h[0, :, :] = h0

        # 邊界條件
        self.h[:, 0, :] = h0
        self.h[:, -1, :] = h0
        self.h[:, :, 0] = h0
        self.h[:, :, -1] = h0

        # 按鈕定義
        self.pushButton.clicked.connect(self.start)
        
        # 滑桿設定
        self.label_slider.setText("0")
        self.horizontalSlider.setRange(0, self.nt)
        self.horizontalSlider.valueChanged.connect(self.update_plot)

        # 創建三維圖形的容器
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_plot.addWidget(self.canvas)

        # 創建二維剖面圖的容器
        self.slice_figure = plt.figure()
        self.slice_canvas = FigureCanvas(self.slice_figure)
        self.verticalLayout_slice.addWidget(self.slice_canvas)

        self.x_slice_figure = plt.figure() 
        self.x_slice_canvas = FigureCanvas(self.x_slice_figure)
        self.verticalLayout_theis.addWidget(self.x_slice_canvas)

    # "模擬"按鈕操作
    def start(self):
        mbox = QMessageBox(self)
        mbox.setStyleSheet("""
            QMessageBox {
                background-color: #f2f2f2;
                color: #333;
            }
            QMessageBox QLabel{
                font-size: 16px; 
                color: black;
                border:0px;
            }
            QMessageBox QWidget{
                background-color: #f2f2f2;
            }
            QMessageBox QPushButton {
                background-color: #0078D7;
                color: white;
                border-style: none;
                border-radius: 5px;
                padding: 6px;
                min-width: 70px;
            }
            QMessageBox QPushButton:hover {
                background-color: #0053ba;
            }
            QMessageBox QPushButton:pressed {
                background-color: #00397a;
            }
        """)
        mbox.setWindowIcon(QIcon('error.ico'))
        
        try:
            # 更新參數
            self.lx = float(self.lineEdit_Lx.text())
            self.ly = float(self.lineEdit_Ly.text())
            self.b = float(self.lineEdit_b.text())
            self.nx = int(self.lineEdit_nx.text())
            self.ny = int(self.lineEdit_ny.text())
            self.dx = self.lx / (self.nx - 1)
            self.dy = self.ly / (self.ny - 1)
            self.nt = int(self.lineEdit_nt.text())
            self.dt = float(self.lineEdit_dt.text())
            self.Ss = float(self.lineEdit_Ss.text())
            self.S = self.Ss * self.b
            self.Kx = float(self.lineEdit_Kx.text())
            self.Ky = float(self.lineEdit_Ky.text())
            self.Tx = self.Kx * self.b
            self.Ty = self.Ky * self.b
            self.wx = int(self.lineEdit_wx.text())
            self.wy = int(self.lineEdit_wy.text())
            self.rw = float(self.lineEdit_rw.text())
            self.A = np.pi * self.rw**2
            self.h0 = int(self.lineEdit_h0.text())

            #更新初始條件
            self.h = np.full((self.nt+1, self.nx, self.ny), self.h0)
            self.h[0, :, :] = self.h0

            #更新邊界條件
            self.h[:, 0, :] = self.h0
            self.h[:, -1, :] = self.h0
            self.h[:, :, 0] = self.h0 
            self.h[:, :, -1] = self.h0

            # FDM(有限差分法)計算水位高度
            try:
                self.fdm()

                try:
                    # 繪圖
                    self.horizontalSlider.setValue(0)
                    self.horizontalSlider.setRange(0, self.nt)
                    self.update_plot()
                except:
                    mbox.setWindowTitle('錯誤警告')
                    mbox.setText('繪圖遇上了點問題')
                    mbox.setIcon(QMessageBox.Warning)
                    mbox.setStandardButtons(QMessageBox.Ok)
                    mbox.exec_()

            except OverflowError:
                mbox.setWindowTitle('錯誤警告')
                mbox.setText('Overflow!\nPython int too large to convert to C long')
                mbox.setIcon(QMessageBox.Warning)
                mbox.setStandardButtons(QMessageBox.Ok)
                mbox.exec_()
        
        # 若輸入不為正確數值則跳出警告視窗
        except ValueError:
            mbox.setWindowTitle('錯誤警告')
            mbox.setText('輸入數值不正確\n請重新輸入')
            mbox.setIcon(QMessageBox.Warning)
            mbox.setStandardButtons(QMessageBox.Ok)
            mbox.exec_()

        

    # 水井函數 
    def W(self, u):
        return -sp.expi(-u)
    
    # theis公式
    def theis_solution(self, Q, T, S, r, t):
        u = r**2 * S / (4 * T * t)
        if u > 0:
            W_u = -sp.expi(-u)  # 使用scipy.special.expi來計算威爾函數
        else:
            W_u = float('1e-4')  # 如果u為0，設為1e-4以避免計算錯誤
        return (Q / (4 * np.pi * T)) * W_u

    # 有限差分法
    def fdm(self):
        T_main = max(self.Tx, self.Ty)
        total_steps = self.nt * (self.nx - 2) * (self.ny - 2)
        step_counter = 0
        for t in range(self.nt):
            for i in range(1, self.nx - 1):
                for j in range(1, self.ny - 1):
                    r = math.sqrt(((i - self.wx) * self.dx) ** 2 + ((j - self.wy) * self.dy) ** 2)

                    if r <= self.rw and t == 0:
                        s = max(self.theis_solution(self.Q, T_main, self.S, r, self.dt), 1e-4)
                        self.h[t + 1, i, j] = self.h0 - s

                    elif r <= self.rw:
                        self.h[t + 1, i, j] = (self.h[t, i, j] + ((self.Tx * self.dt) / (self.S * self.dx**2)) * (self.h[t, i + 1, j] - 2 * self.h[t, i, j] + self.h[t, i-1, j])
                                            + ((self.Ty * self.dt) / (self.S * self.dy**2)) * (self.h[t, i, j + 1] - 2 * self.h[t, i, j] + self.h[t, i, j - 1])
                                            - (self.Q * self.dt / self.S))   
                    else:
                        if j + 1 < self.ny and j - 1 >= 0:
                            self.h[t + 1, i, j] = (self.h[t, i, j] + ((self.Tx * self.dt) / (self.S * self.dx**2)) * (self.h[t, i + 1, j] - 2 * self.h[t, i, j] + self.h[t, i - 1, j])
                                                + ((self.Ty * self.dt) / (self.S * self.dy**2)) * (self.h[t, i, j + 1] - 2 * self.h[t, i, j] + self.h[t, i, j - 1]))

                    #更新進度條
                    step_counter += 1
                    progress = step_counter / total_steps * 100  
                    self.progressBar.setValue(int(progress)) 

            # 更新邊界條件
            self.h[t + 1, 0, :] = self.h0
            self.h[t + 1, -1, :] = self.h0
            self.h[t + 1, :, 0] = self.h0 
            self.h[t + 1, :, -1] = self.h0

    # 視窗畫布更新
    def update_plot(self):
        self.figure.clear()  # 清空三維畫布
        self.slice_figure.clear()  # 清空y軸二維剖面圖畫布
        self.x_slice_figure.clear()  # 清空x軸二維剖面圖畫布

        # 滑桿值取用
        self.label_slider.setText(str(self.horizontalSlider.value()))
        t_idx = self.horizontalSlider.value()
        
        h_final = self.h[t_idx, :, :]

        x = np.linspace(0, self.lx, self.nx)
        y = np.linspace(0, self.ly, self.ny)
        X, Y = np.meshgrid(x, y)

        # 更新三維視圖
        ax = self.figure.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, h_final, cmap='viridis')
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Water Head (m)')
        ax.set_title(f'Water Head at Time Step {t_idx}')
        ax.set_xlim(0, self.lx)
        ax.set_ylim(0, self.ly)
        ax.set_zlim(0, self.h0 + 1)
        self.canvas.draw()

        # 更新y軸二維剖面圖
        slice_ax = self.slice_figure.add_subplot(111)
        mid_y = self.ny // 2
        x_interp = np.linspace(0, self.lx, 10 * self.nx)
        h_interp = np.interp(x_interp, x, h_final[:, mid_y])        
        
        slice_ax.plot(x_interp, h_interp, label=f'Y = {mid_y}')
        slice_ax.axvline(x=self.wx * self.dx, color='r', linestyle='--', label='Well Position')
        slice_ax.set_xlabel('X (m)')
        slice_ax.set_ylabel('Water Head (m)')
        slice_ax.set_ylim(0, self.h0 + 1)
        slice_ax.set_title(f'2D Slice at Y = {mid_y}, Time Step {t_idx}')
        slice_ax.legend()
        self.slice_canvas.draw()

        # 更新x軸二維剖面
        x_slice_ax = self.x_slice_figure.add_subplot(111)
        mid_x = self.nx // 2
        y_interp = np.linspace(0, self.ly, 10 * self.ny)
        h_interp_x = np.interp(y_interp, y, h_final[mid_x, :])

        x_slice_ax.plot(y_interp, h_interp_x, label=f'X = {mid_x}')
        x_slice_ax.axvline(x=self.wy * self.dy, color='r', linestyle='--', label='Well Position')
        x_slice_ax.set_xlabel('Y (m)')
        x_slice_ax.set_ylabel('Water Head (m)')
        x_slice_ax.set_ylim(0, self.h0 + 1)
        x_slice_ax.set_title(f'2D Slice at X = {mid_x}, Time Step {t_idx}')
        x_slice_ax.legend()
        self.x_slice_canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 設定模擬參數
    # 此處僅給予預設值
    lx = 1000  # 含水層長度 (m)
    ly = 1000  # 含水層寬度 (m)
    b = 50     # 含水層厚度 (m)
    nx = 100   # x方向上的空間步數
    ny = 100   # y方向上的空間步數
    nt = 200   # 時間步數
    dt = 0.1   # 時間步長 (s)
    Ss = 1e-4  # 比儲率 (m^-1)
    Kx = 1e-4  # x方向上的導水係數 (m/s)
    Ky = 1e-4  # y方向上的導水係數 (m/s)
    Q = 0.01   # 水井抽水量 (m^3/s)
    wx = 50    # 井在 x 方向上的座標
    wy = 50    # 井在 y 方向上的座標
    rw = 0.1   # 井口半徑 (m)
    h0 = 10    # 初始水面高度 (m)

    # 創建主視窗
    window = GroundWater(lx, ly, b, nx, ny, nt, dt, Ss, Kx, Ky, Q, wx, wy, rw, h0)
    
    # 顯示主視窗
    window.show()
    
    sys.exit(app.exec_())
