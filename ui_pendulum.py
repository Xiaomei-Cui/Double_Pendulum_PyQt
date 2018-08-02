from PyQt5 import QtWidgets, QtGui, QtCore

import math


class Ui_Pendulum():
    def __init__(self, QGraphicsScene):
        self.scene = QGraphicsScene

    def draw_pendulum(self, double_pendulum):
        self.length1 = double_pendulum.pendulum1.length * 100
        self.length2 = double_pendulum.pendulum2.length * 100
        self.rect_width = 5
        self.diameter = 20

        self.outline = QtGui.QPen(QtCore.Qt.transparent)
        self.brush1 = QtGui.QBrush(QtCore.Qt.green)
        self.brush2 = QtGui.QBrush(QtCore.Qt.blue)

        self.rect1 = QtWidgets.QGraphicsRectItem(-self.rect_width/2,
                                                 0,
                                                 self.rect_width,
                                                 self.length1)
        self.rect1.setPen(self.outline)
        self.rect1.setBrush(self.brush1)
        self.rect1.setTransformOriginPoint(0, 0)

        self.circle1 = QtWidgets.QGraphicsEllipseItem(-self.diameter/2,
                                                      self.length1-self.diameter/2,
                                                      self.diameter,
                                                      self.diameter,
                                                      self.rect1)
        self.circle1.setPen(self.outline)
        self.circle1.setBrush(self.brush1)

        self.rect2 = QtWidgets.QGraphicsRectItem(-self.rect_width/2,
                                                 self.length1,
                                                 self.rect_width,
                                                 self.length2,
                                                 self.rect1)
        self.rect2.setPen(self.outline)
        self.rect2.setBrush(self.brush2)
        self.rect2.setTransformOriginPoint(0, self.length1)
        self.rect2.setFlag(QtWidgets.QGraphicsItem.ItemStacksBehindParent, True)

        self.circle2 = QtWidgets.QGraphicsEllipseItem(-self.diameter/2,
                                                      self.length1+self.length2-self.diameter/2,
                                                      self.diameter,
                                                      self.diameter,
                                                      self.rect2)
        self.circle2.setPen(self.outline)
        self.circle2.setBrush(self.brush2)

        self.rect1.setRotation(math.degrees(double_pendulum.pendulum1.theta))
        self.rect2.setRotation(math.degrees(double_pendulum.pendulum2.theta -
                                            double_pendulum.pendulum1.theta))

        self.scene.addItem(self.rect1)

    def delete_pendulum(self):
        self.scene.removeItem(self.rect1)
        del self.rect1
