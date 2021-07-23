# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HSV_Checker_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QColor, QIcon
from KClass.Spline_Interpolation_3 import Color_Interpolation, Color_Interpolation_2D, Color_Interpolation_HSV_2D
import colorsys as cs
import time


class _Bar(QtWidgets.QWidget):
    clickedValue = QtCore.pyqtSignal(str)

    def __init__(self, colors=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor('grey')
        self._padding = 4.0  # n-pixel gap around edge.
        self.nSteps = None
        self.padding = 5
        self.colors = []
        if not colors:
            return

        self.nSteps = len(colors)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)
        if self.colors:
            width = self.size().width()
            height = self.size().height()
            d_width = width - self.padding * 2
            d_height = height - self.padding * 2

            step_size_width = d_width / self.nSteps
            step_size_height = d_height / self.nSteps

            if isinstance(self.colors, str):
                brush.setColor(QColor(self.colors))
                rect = QtCore.QRect(self.padding,
                                    self.padding ,
                                    d_width,
                                    d_height)
                painter.fillRect(rect, brush)
            else:
                t = time.time()
                for i in range(self.nSteps):
                    for j in range(self.nSteps):
                        brush.setColor(QColor(self.colors[j][i]))
                        rect = QtCore.QRect(self.padding + step_size_width * i - 1,
                                            self.padding + step_size_height * j - 1,
                                            step_size_width + 1,
                                            step_size_height + 1)
                        painter.fillRect(rect, brush)
                # print("Paint : " + str(time.time() - t))
        painter.end()

    def _trigger_refresh(self):
        self.update()

    def setColors(self, colors):
        if isinstance(colors, str):
            self.nSteps = 1
        if isinstance(colors, list):
            self.nSteps = len(colors)
        self.colors = colors
        self.update()

    def setBarSolidPercent(self, f):
        self._bar_solid_percent = float(f)
        self.update()

    def setBackgroundColor(self, color):
        self._background_color = QtGui.QColor(color)
        self.update()

    def setNotchesVisible(self, b):
        return self._dial.setNotchesVisible(b)

    def mouseMoveEvent(self, e):
        if not self.colors:
            return
        width = self.size().width()
        height = self.size().height()
        d_width = width - self.padding * 2
        d_height = height - self.padding * 2

        step_size_width = d_width / self.nSteps
        step_size_height = d_height / self.nSteps
        mouse_x = e.x()
        mouse_y = e.y()

        x_ind = int((mouse_x - self.padding + 1) / step_size_width)
        y_ind = int((mouse_y - self.padding + 1) / step_size_height)
        # print("x ind : " + str(x_ind))
        # print("y ind : " + str(y_ind))

        if 0 <= x_ind < self.nSteps and 0 <= y_ind < self.nSteps:
            color = self.colors[y_ind][x_ind]
            print(color)
            self.clickedValue.emit(color)

    def mousePressEvent(self, e):
        if not self.colors:
            return
        width = self.size().width()
        height = self.size().height()
        d_width = width - self.padding * 2
        d_height = height - self.padding * 2

        step_size_width = d_width / self.nSteps
        step_size_height = d_height / self.nSteps
        mouse_x = e.x()
        mouse_y = e.y()

        x_ind = int((mouse_x - self.padding + 1) / step_size_width)
        y_ind = int((mouse_y - self.padding + 1) / step_size_height)
        # print("x ind : " + str(x_ind))
        # print("y ind : " + str(y_ind))

        if 0 <= x_ind < self.nSteps and 0 <= y_ind < self.nSteps:
            color = self.colors[y_ind][x_ind]
            print(color)
            self.clickedValue.emit(color)


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(928, 718)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        ############
        self.colorDisplay = _Bar()
        self.colorDisplay.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorDisplay.sizePolicy().hasHeightForWidth())
        self.colorDisplay.setSizePolicy(sizePolicy)
        self.colorDisplay.setObjectName("colorDisplay")
        self.colorDisplay.setBarSolidPercent(0.9)
        self.colorDisplay.setBackgroundColor('gray')
        ############
        self.horizontalLayout_2.addWidget(self.colorDisplay)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hueLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hueLabel.sizePolicy().hasHeightForWidth())
        self.hueLabel.setSizePolicy(sizePolicy)
        self.hueLabel.setObjectName("hueLabel")
        self.horizontalLayout_3.addWidget(self.hueLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.hueSpinBox = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hueSpinBox.sizePolicy().hasHeightForWidth())
        self.hueSpinBox.setSizePolicy(sizePolicy)
        self.hueSpinBox.setMaximum(360)
        self.hueSpinBox.setObjectName("hueSpinBox")
        self.horizontalLayout_3.addWidget(self.hueSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.hueSlider = QtWidgets.QSlider(Form)
        self.hueSlider.setMaximum(360)
        self.hueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hueSlider.setObjectName("hueSlider")
        self.verticalLayout_2.addWidget(self.hueSlider)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.satLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.satLabel.sizePolicy().hasHeightForWidth())
        self.satLabel.setSizePolicy(sizePolicy)
        self.satLabel.setObjectName("satLabel")
        self.horizontalLayout_4.addWidget(self.satLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.satSpinBox = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.satSpinBox.sizePolicy().hasHeightForWidth())
        self.satSpinBox.setSizePolicy(sizePolicy)
        self.satSpinBox.setMaximum(255)
        self.satSpinBox.setProperty("value", 255)
        self.satSpinBox.setObjectName("satSpinBox")
        self.horizontalLayout_4.addWidget(self.satSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.satSlider = QtWidgets.QSlider(Form)
        self.satSlider.setMaximum(255)
        self.satSlider.setProperty("value", 255)
        self.satSlider.setOrientation(QtCore.Qt.Horizontal)
        self.satSlider.setObjectName("satSlider")
        self.verticalLayout_2.addWidget(self.satSlider)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.valueValue = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueValue.sizePolicy().hasHeightForWidth())
        self.valueValue.setSizePolicy(sizePolicy)
        self.valueValue.setObjectName("valueValue")
        self.horizontalLayout_5.addWidget(self.valueValue)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.valueSpinBox = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueSpinBox.sizePolicy().hasHeightForWidth())
        self.valueSpinBox.setSizePolicy(sizePolicy)
        self.valueSpinBox.setMaximum(255)
        self.valueSpinBox.setProperty("value", 255)
        self.valueSpinBox.setObjectName("valueSpinBox")
        self.horizontalLayout_5.addWidget(self.valueSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.valueSlider = QtWidgets.QSlider(Form)
        self.valueSlider.setMaximum(255)
        self.valueSlider.setProperty("value", 255)
        self.valueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.valueSlider.setObjectName("valueSlider")
        self.verticalLayout_2.addWidget(self.valueSlider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nStepsLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nStepsLabel.sizePolicy().hasHeightForWidth())
        self.nStepsLabel.setSizePolicy(sizePolicy)
        self.nStepsLabel.setObjectName("nStepsLabel")
        self.horizontalLayout.addWidget(self.nStepsLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.stepSpinBox = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepSpinBox.sizePolicy().hasHeightForWidth())
        self.stepSpinBox.setSizePolicy(sizePolicy)
        self.stepSpinBox.setMinimum(1)
        self.stepSpinBox.setMaximum(200)
        self.stepSpinBox.setObjectName("stepSpinBox")
        self.horizontalLayout.addWidget(self.stepSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.nStepsSlider = QtWidgets.QSlider(Form)
        self.nStepsSlider.setMinimum(1)
        self.nStepsSlider.setMaximum(200)
        self.nStepsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nStepsSlider.setObjectName("nStepsSlider")
        self.verticalLayout_2.addWidget(self.nStepsSlider)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        ############
        self.subColorDisplay = _Bar()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subColorDisplay.sizePolicy().hasHeightForWidth())
        self.subColorDisplay.setBarSolidPercent(0.9)
        self.subColorDisplay.setBackgroundColor('gray')
        self.subColorDisplay.setSizePolicy(sizePolicy)
        self.subColorDisplay.setMinimumSize(QtCore.QSize(100, 100))
        self.subColorDisplay.setObjectName("subColorDisplay")
        ############

        self.verticalLayout_2.addWidget(self.subColorDisplay)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        ###################################################################
        self.nStepsSlider.setMaximum(200)

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.color = QColor()
        self.color.setHsv(0, 255, 255)
        self.colorDisplay.setColors([self.color.name()])
        self.subColorDisplay.setBackgroundColor(self.color)


        self.nSteps = self.nStepsSlider.value()


        # Set pixel map
        self.brush = QtGui.QPixmap(50, 50)
        self.brush.fill(self.color)

        # Signal-Slot作成
        self.colorDisplay.clickedValue.connect(self.color_picker)
        self.hueSlider.valueChanged['int'].connect(self.colorChanged)
        self.satSlider.valueChanged['int'].connect(self.colorChanged)
        self.valueSlider.valueChanged['int'].connect(self.colorChanged)
        self.nStepsSlider.valueChanged['int'].connect(self.stepChanged)
        self.nStepsSlider.valueChanged['int'].connect(self.stepSpinBox.setValue)
        self.hueSpinBox.valueChanged.connect(lambda : self.spinboxChanged(self.hueSpinBox))
        self.satSpinBox.valueChanged.connect(lambda: self.spinboxChanged(self.satSpinBox))
        self.valueSpinBox.valueChanged.connect(lambda: self.spinboxChanged(self.valueSpinBox))
        self.stepSpinBox.valueChanged.connect(lambda: self.spinboxChanged(self.stepSpinBox))

        self.display_color_update()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.hueLabel.setText(_translate("Form", "Hue"))
        self.satLabel.setText(_translate("Form", "Saturation"))
        self.valueValue.setText(_translate("Form", "Value"))
        self.nStepsLabel.setText(_translate("Form", "Steps"))


    def colorChanged(self, main_update=True):
        self.color.setHsv(self.hueSlider.value(), self.satSlider.value(), self.valueSlider.value())
        self.setColor(self.color)
        # self.colorDisplay.setBackgroundColor(self.color)
        self.subColorDisplay.setBackgroundColor(self.color)
        if main_update:
            self.display_color_update()
        # print(self.itemsData())


    def stepChanged(self):
        self.nSteps = self.nStepsSlider.value()
        self.display_color_update()

    def display_color_update(self):
        t = time.time()

        print(self.hueSlider.value() / 360)
        r, g, b = cs.hsv_to_rgb(self.hueSlider.value() / 360, 1, 1)
        code_bottom_left = '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))

        r, g, b = cs.hsv_to_rgb(self.hueSlider.value() / 360, 0.01, 255)
        code_top_left = '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))

        r, g, b = cs.hsv_to_rgb(self.hueSlider.value() / 360, 1, 255)
        code_top_right = '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))

        colors = Color_Interpolation_2D(code_top_right, code_top_left, code_bottom_left, code_bottom_left, self.nStepsSlider.value())

        self.colorDisplay.setColors(colors)
        # print("Calul : " + str(time.time() - t))

    def color_picker(self, value):
        self.hueSlider.blockSignals(True)
        self.satSlider.blockSignals(True)
        self.valueSlider.blockSignals(True)
        self.setColor(value)
        self.hueSlider.blockSignals(False)
        self.satSlider.blockSignals(False)
        self.valueSlider.blockSignals(False)
        self.subColorDisplay.setBackgroundColor(value)

    def spinboxChanged(self, object):
        if object == self.hueSpinBox:
            self.hueSlider.setValue(self.hueSpinBox.value())
        elif object == self.satSpinBox:
            self.satSlider.setValue(self.satSpinBox.value())
        elif object == self.valueSpinBox:
            self.valueSlider.setValue(self.valueSpinBox.value())
        elif object == self.stepSpinBox:
            self.nStepsSlider.setValue(self.stepSpinBox.value())


    def selectPreset(self, index):
        self.setColor(self.presetModel.index(index, 0).data())

    def setColor(self, color):
        self.color = QColor(color)
        self.hueSpinBox.setValue(QColor(color).hue())
        self.satSpinBox.setValue(QColor(color).saturation())
        self.valueSpinBox.setValue(QColor(color).value())
        self.hueSlider.setValue(QColor(color).hue())
        self.satSlider.setValue(QColor(color).saturation())
        self.valueSlider.setValue(QColor(color).value())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())
