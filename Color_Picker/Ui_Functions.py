#######################
# Signal and slot
#######################
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import colorsys as cs
from Spline_Interpolation_3 import Color_Interpolation_HSV_2D, Color_Palette_2D, Color_Palette_2D_Fixed_Sat, Color_Palette_2D_Fixed_Value
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from _Bar import _Bar

class Ui_Functions():
    def __init__(self, window):
        if hasattr(window, "ui"):
            self.ui = window.ui
        else:
            self.ui = window


        ############

        self.ui.colorDisplay = _Bar()
        self.ui.colorDisplay.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.colorDisplay.sizePolicy().hasHeightForWidth())
        self.ui.colorDisplay.setSizePolicy(sizePolicy)
        self.ui.colorDisplay.setObjectName("colorDisplay")
        self.ui.colorDisplay.setBarSolidPercent(0.9)
        self.ui.colorDisplay.setBackgroundColor('gray')
        self.ui.verticalLayout_4.addWidget(self.ui.colorDisplay)


        self.ui.subColorDisplay = _Bar()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.subColorDisplay.sizePolicy().hasHeightForWidth())
        self.ui.subColorDisplay.setBarSolidPercent(0.9)
        self.ui.subColorDisplay.setBackgroundColor('gray')
        self.ui.subColorDisplay.setSizePolicy(sizePolicy)
        self.ui.subColorDisplay.setMinimumSize(QtCore.QSize(200, 200))
        self.ui.subColorDisplay.setObjectName("subColorDisplay")
        self.ui.verticalLayout_4.addWidget(self.ui.subColorDisplay)





        self.ui.monoColorDisplay = _Bar()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.monoColorDisplay.sizePolicy().hasHeightForWidth())
        self.ui.monoColorDisplay.setBarSolidPercent(0.9)
        self.ui.monoColorDisplay.setBackgroundColor('gray')
        self.ui.monoColorDisplay.setSizePolicy(sizePolicy)
        self.ui.monoColorDisplay.setMinimumSize(QtCore.QSize(100, 100))
        self.ui.monoColorDisplay.setObjectName("subColorDisplay")
        self.ui.verticalLayout_2.addWidget(self.ui.monoColorDisplay)

        ###################################################################

        self.ui.color = QColor()
        self.ui.color.setHsv(0, 255, 255)
        self.ui.colorDisplay.setColors([self.ui.color.name()])

        self.ui.nSteps = self.ui.nStepsSlider.value()

        # Set pixel map
        self.ui.brush = QtGui.QPixmap(50, 50)
        self.ui.brush.fill(self.ui.color)

        # Signal-Slot作成
        self.ui.colorDisplay.clickedValue.connect(self.color_picker)
        self.ui.monoColorDisplay.clickedValue.connect(self.color_picker)
        self.ui.hueSlider.valueChanged['int'].connect(self.colorChanged)
        self.ui.satSlider.valueChanged['int'].connect(self.colorChanged)
        self.ui.valueSlider.valueChanged['int'].connect(self.colorChanged)
        self.ui.nStepsSlider.valueChanged['int'].connect(self.stepChanged)
        self.ui.nStepsSlider.valueChanged['int'].connect(self.ui.stepSpinBox.setValue)
        self.ui.hueSpinBox.valueChanged.connect(lambda: self.spinboxChanged(self.ui.hueSpinBox))
        self.ui.satSpinBox.valueChanged.connect(lambda: self.spinboxChanged(self.ui.satSpinBox))
        self.ui.valueSpinBox.valueChanged.connect(lambda: self.spinboxChanged(self.ui.valueSpinBox))
        self.ui.stepSpinBox.valueChanged.connect(lambda: self.spinboxChanged(self.ui.stepSpinBox))
        self.ui.preset_color_1.clicked.connect(lambda: self.setColor(self.ui.preset_color_1.text()))
        self.ui.preset_color_2.clicked.connect(lambda: self.setColor(self.ui.preset_color_2.text()))
        self.ui.preset_color_3.clicked.connect(lambda: self.setColor(self.ui.preset_color_3.text()))
        self.ui.preset_color_4.clicked.connect(lambda: self.setColor(self.ui.preset_color_4.text()))
        self.ui.preset_color_5.clicked.connect(lambda: self.setColor(self.ui.preset_color_5.text()))
        self.ui.preset_color_6.clicked.connect(lambda: self.setColor(self.ui.preset_color_6.text()))
        self.ui.preset_color_7.clicked.connect(lambda: self.setColor(self.ui.preset_color_7.text()))
        self.ui.preset_color_8.clicked.connect(lambda: self.setColor(self.ui.preset_color_8.text()))
        self.ui.preset_color_9.clicked.connect(lambda: self.setColor(self.ui.preset_color_9.text()))
        self.ui.preset_color_10.clicked.connect(lambda: self.setColor(self.ui.preset_color_10.text()))
        self.ui.preset_color_11.clicked.connect(lambda: self.setColor(self.ui.preset_color_11.text()))
        self.ui.preset_color_12.clicked.connect(lambda: self.setColor(self.ui.preset_color_12.text()))
        self.ui.preset_color_13.clicked.connect(lambda: self.setColor(self.ui.preset_color_13.text()))
        self.ui.preset_color_14.clicked.connect(lambda: self.setColor(self.ui.preset_color_14.text()))
        self.ui.preset_color_15.clicked.connect(lambda: self.setColor(self.ui.preset_color_15.text()))
        self.ui.preset_color_16.clicked.connect(lambda: self.setColor(self.ui.preset_color_16.text()))
        self.ui.preset_color_17.clicked.connect(lambda: self.setColor(self.ui.preset_color_17.text()))
        self.ui.preset_color_18.clicked.connect(lambda: self.setColor(self.ui.preset_color_18.text()))
        self.ui.preset_color_19.clicked.connect(lambda: self.setColor(self.ui.preset_color_19.text()))
        self.ui.preset_color_20.clicked.connect(lambda: self.setColor(self.ui.preset_color_20.text()))
        self.ui.preset_color_21.clicked.connect(lambda: self.setColor(self.ui.preset_color_21.text()))
        self.ui.preset_color_22.clicked.connect(lambda: self.setColor(self.ui.preset_color_22.text()))
        self.ui.preset_color_23.clicked.connect(lambda: self.setColor(self.ui.preset_color_23.text()))
        self.ui.preset_color_24.clicked.connect(lambda: self.setColor(self.ui.preset_color_24.text()))

        self.display_color_update()
        self.ui.nStepsSlider.setValue(8)

    #######################
    # functions for slots
    #######################

    def setSteps(self, steps):
        self.ui.nStepsSlider.setValue(steps)
    def colorChanged(self, main_update=True):
        self.ui.color.setHsv(self.ui.hueSlider.value(), self.ui.satSlider.value(), self.ui.valueSlider.value())
        self.setColor(self.ui.color)
        # self.ui.colorDisplay.setBackgroundColor(self.ui.color)
        self.ui.subColorDisplay.setBackgroundColor(self.ui.color)
        if main_update:
            self.display_color_update()


    def stepChanged(self):
        self.ui.nSteps = self.ui.nStepsSlider.value()
        self.display_color_update()

    def display_color_update(self):
        t = time.time()

        # print(self.ui.hueSlider.value() / 360)
        code_bottom_left = [self.ui.hueSlider.value(), 255, 0]
        code_bottom_right = [self.ui.hueSlider.value(), 0, 0]
        code_top_left = [self.ui.hueSlider.value(), 0, 255]
        code_top_right = [self.ui.hueSlider.value(), 255, 255]


        # colors = Color_Palette_2D(16)
        colors = Color_Palette_2D_Fixed_Sat(self.ui.nStepsSlider.value(), self.ui.satSlider.value())
        colors = Color_Palette_2D_Fixed_Value(self.ui.nStepsSlider.value(), 255)

        self.ui.colorDisplay.setColors(colors)
        colors = Color_Interpolation_HSV_2D(code_top_right, code_top_left, code_bottom_left, code_bottom_right,
                                            self.ui.nStepsSlider.value())
        self.ui.monoColorDisplay.setColors(colors)
        # print("Calul : " + str(time.time() - t))

    def color_picker(self, value):
        self.ui.hueSlider.blockSignals(True)
        self.ui.satSlider.blockSignals(True)
        self.ui.valueSlider.blockSignals(True)
        self.setColor(value)
        self.display_color_update()
        self.ui.hueSlider.blockSignals(False)
        self.ui.satSlider.blockSignals(False)
        self.ui.valueSlider.blockSignals(False)
        self.ui.subColorDisplay.setBackgroundColor(value)


    def spinboxChanged(self, object):
        if object == self.ui.hueSpinBox:
            self.ui.hueSlider.setValue(self.ui.hueSpinBox.value())
        elif object == self.ui.satSpinBox:
            self.ui.satSlider.setValue(self.ui.satSpinBox.value())
        elif object == self.ui.valueSpinBox:
            self.ui.valueSlider.setValue(self.ui.valueSpinBox.value())
        elif object == self.ui.stepSpinBox:
            self.ui.nStepsSlider.setValue(self.ui.stepSpinBox.value())

    def setColor(self, color):
        self.ui.color = QColor(color)
        self.ui.hueSpinBox.setValue(QColor(color).hue())
        self.ui.satSpinBox.setValue(QColor(color).saturation())
        self.ui.valueSpinBox.setValue(QColor(color).value())
        self.ui.hueSlider.setValue(QColor(color).hue())
        self.ui.satSlider.setValue(QColor(color).saturation())
        self.ui.valueSlider.setValue(QColor(color).value())

    ########################
    # Key Setting (ASCII)###
    ########################
    def key_event(self, event):
        # event.key() to get keyboard input
        print(event.key())
        key = event.key()
        if 48 <= key <= 57:
            self.ui.update_pass(int(chr(key)))

        # 16777220 is Enter key code
        if key == 16777220:
            self.ui.mousePressEvent()
