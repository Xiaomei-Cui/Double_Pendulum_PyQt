from PyQt5 import QtWidgets, QtCore

import math

from ui_mainwindow import Ui_MainWindow
from pendulum import pendulum, double_pendulum
from ui_pendulum import Ui_Pendulum
import rk4


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.scene.setSceneRect(-self.ui.graphicsView.width()/2+1,
                                -self.ui.graphicsView.height()/2+1,
                                self.ui.graphicsView.width()-2,
                                self.ui.graphicsView.height()-2)
        self.ui_pendulum = Ui_Pendulum(self.scene)

        self.timer = QtCore.QTimer(self)

        self.initialize_simulation()
        QtWidgets.QApplication.processEvents()

        self.ui.m1_SpinBox.setEnabled(True)
        self.ui.m2_SpinBox.setEnabled(True)
        self.ui.l1_SpinBox.setEnabled(True)
        self.ui.l2_SpinBox.setEnabled(True)
        self.ui.theta1_SpinBox.setEnabled(True)
        self.ui.theta2_SpinBox.setEnabled(True)
        self.ui.vel1_SpinBox.setEnabled(True)
        self.ui.vel2_SpinBox.setEnabled(True)
        self.ui.g_SpinBox.setEnabled(True)
        self.ui.m1_Slider.setEnabled(True)
        self.ui.m2_Slider.setEnabled(True)
        self.ui.l1_Slider.setEnabled(True)
        self.ui.l2_Slider.setEnabled(True)
        self.ui.theta1_Slider.setEnabled(True)
        self.ui.theta2_Slider.setEnabled(True)
        self.ui.vel1_Slider.setEnabled(True)
        self.ui.vel2_Slider.setEnabled(True)
        self.ui.g_Slider.setEnabled(True)
        self.ui.StartButton.setEnabled(True)
        self.ui.PauseButton.setEnabled(False)
        self.ui.ResumeButton.setEnabled(False)
        self.ui.StopButton.setEnabled(False)
        self.ui.DefaultButton.setEnabled(True)

        self.timer.timeout.connect(self.update_simulation)

    def initialize_simulation(self):
        self.pendulum1 = pendulum(self.ui.m1_SpinBox.value(),
                                  self.ui.l1_SpinBox.value(),
                                  math.radians(self.ui.theta1_SpinBox.value()),
                                  math.radians(self.ui.vel1_SpinBox.value()))
        self.pendulum2 = pendulum(self.ui.m2_SpinBox.value(),
                                  self.ui.l2_SpinBox.value(),
                                  math.radians(self.ui.theta2_SpinBox.value()),
                                  math.radians(self.ui.vel2_SpinBox.value()))
        self.double_pendulum = double_pendulum(self.pendulum1,
                                               self.pendulum2,
                                               self.ui.g_SpinBox.value())

        self.ui_pendulum.draw_pendulum(self.double_pendulum)

    def update_simulation(self):
        self.ui_pendulum.delete_pendulum()
        self.double_pendulum = rk4.rk4(self.double_pendulum)
        self.ui_pendulum.draw_pendulum(self.double_pendulum)

    def start_simulation(self):
        self.timer.start(20)

    def pause_simulation(self):
        self.timer.stop()

    def resume_simulation(self):
        self.timer.start(20)

    def stop_simulation(self):
        self.timer.stop()
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_m1_Slider_valueChanged(self, position):
        self.ui.m1_SpinBox.setValue(float(position)/100)

    def on_m1_SpinBox_valueChanged(self, arg1):
        self.ui.m1_Slider.setValue(float(arg1)*100)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_m2_Slider_valueChanged(self, position):
        self.ui.m2_SpinBox.setValue(float(position)/100)

    def on_m2_SpinBox_valueChanged(self, arg1):
        self.ui.m2_Slider.setValue(float(arg1)*100)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_l1_Slider_valueChanged(self, position):
        self.ui.l1_SpinBox.setValue(float(position)/100)

    def on_l1_SpinBox_valueChanged(self, arg1):
        self.ui.l1_Slider.setValue(float(arg1)*100)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_l2_Slider_valueChanged(self, position):
        self.ui.l2_SpinBox.setValue(float(position)/100)

    def on_l2_SpinBox_valueChanged(self, arg1):
        self.ui.l2_Slider.setValue(float(arg1)*100)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_theta1_Slider_valueChanged(self, position):
        self.ui.theta1_SpinBox.setValue(float(position)/10-180)

    def on_theta1_SpinBox_valueChanged(self, arg1):
        self.ui.theta1_Slider.setValue(float(arg1)*10+1800)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_theta2_Slider_valueChanged(self, position):
        self.ui.theta2_SpinBox.setValue(float(position)/10-180)

    def on_theta2_SpinBox_valueChanged(self, arg1):
        self.ui.theta2_Slider.setValue(float(arg1)*10+1800)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_vel1_Slider_valueChanged(self, position):
        self.ui.vel1_SpinBox.setValue(float(position)/10-200)

    def on_vel1_SpinBox_valueChanged(self, arg1):
        self.ui.vel1_Slider.setValue(float(arg1)*10+2000)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_vel2_Slider_valueChanged(self, position):
        self.ui.vel2_SpinBox.setValue(float(position)/10-200)

    def on_vel2_SpinBox_valueChanged(self, arg1):
        self.ui.vel2_Slider.setValue(float(arg1)*10+2000)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_g_Slider_valueChanged(self, position):
        self.ui.g_SpinBox.setValue(float(position)/100)

    def on_g_SpinBox_valueChanged(self, arg1):
        self.ui.g_Slider.setValue(float(arg1)*100)
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()

    def on_DefaultButton_clicked(self):
        self.ui_pendulum.delete_pendulum()
        self.initialize_simulation()
        QtWidgets.QApplication.processEvents()

        self.ui.m1_SpinBox.setValue(1.00)
        self.ui.m2_SpinBox.setValue(1.00)
        self.ui.l1_SpinBox.setValue(1.00)
        self.ui.l2_SpinBox.setValue(1.00)
        self.ui.theta1_SpinBox.setValue(90.0)
        self.ui.theta2_SpinBox.setValue(90.0)
        self.ui.vel1_SpinBox.setValue(0.00)
        self.ui.vel2_SpinBox.setValue(0.00)
        self.ui.g_SpinBox.setValue(9.80)

    def on_StartButton_clicked(self):
        self.start_simulation()
        QtWidgets.QApplication.processEvents()

        self.ui.m1_SpinBox.setEnabled(False)
        self.ui.m2_SpinBox.setEnabled(False)
        self.ui.l1_SpinBox.setEnabled(False)
        self.ui.l2_SpinBox.setEnabled(False)
        self.ui.theta1_SpinBox.setEnabled(False)
        self.ui.theta2_SpinBox.setEnabled(False)
        self.ui.vel1_SpinBox.setEnabled(False)
        self.ui.vel2_SpinBox.setEnabled(False)
        self.ui.g_SpinBox.setEnabled(False)
        self.ui.m1_Slider.setEnabled(False)
        self.ui.m2_Slider.setEnabled(False)
        self.ui.l1_Slider.setEnabled(False)
        self.ui.l2_Slider.setEnabled(False)
        self.ui.theta1_Slider.setEnabled(False)
        self.ui.theta2_Slider.setEnabled(False)
        self.ui.vel1_Slider.setEnabled(False)
        self.ui.vel2_Slider.setEnabled(False)
        self.ui.g_Slider.setEnabled(False)
        self.ui.StartButton.setEnabled(False)
        self.ui.PauseButton.setEnabled(True)
        self.ui.StopButton.setEnabled(True)
        self.ui.DefaultButton.setEnabled(False)

    def on_PauseButton_clicked(self):
        self.pause_simulation()
        QtWidgets.QApplication.processEvents()

        self.ui.PauseButton.setEnabled(False)
        self.ui.ResumeButton.setEnabled(True)

    def on_ResumeButton_clicked(self):
        self.resume_simulation()
        QtWidgets.QApplication.processEvents()

        self.ui.PauseButton.setEnabled(True)
        self.ui.ResumeButton.setEnabled(False)

    def on_StopButton_clicked(self):
        self.stop_simulation()
        QtWidgets.QApplication.processEvents()

        self.ui.m1_SpinBox.setEnabled(True)
        self.ui.m2_SpinBox.setEnabled(True)
        self.ui.l1_SpinBox.setEnabled(True)
        self.ui.l2_SpinBox.setEnabled(True)
        self.ui.theta1_SpinBox.setEnabled(True)
        self.ui.theta2_SpinBox.setEnabled(True)
        self.ui.vel1_SpinBox.setEnabled(True)
        self.ui.vel2_SpinBox.setEnabled(True)
        self.ui.g_SpinBox.setEnabled(True)
        self.ui.m1_Slider.setEnabled(True)
        self.ui.m2_Slider.setEnabled(True)
        self.ui.l1_Slider.setEnabled(True)
        self.ui.l2_Slider.setEnabled(True)
        self.ui.theta1_Slider.setEnabled(True)
        self.ui.theta2_Slider.setEnabled(True)
        self.ui.vel1_Slider.setEnabled(True)
        self.ui.vel2_Slider.setEnabled(True)
        self.ui.g_Slider.setEnabled(True)
        self.ui.StartButton.setEnabled(True)
        self.ui.PauseButton.setEnabled(False)
        self.ui.ResumeButton.setEnabled(False)
        self.ui.StopButton.setEnabled(False)
        self.ui.DefaultButton.setEnabled(True)
