# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Color_Picker.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(676, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hueLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hueLabel.sizePolicy().hasHeightForWidth())
        self.hueLabel.setSizePolicy(sizePolicy)
        self.hueLabel.setObjectName("hueLabel")
        self.horizontalLayout_3.addWidget(self.hueLabel)
        self.hueSpinBox = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hueSpinBox.sizePolicy().hasHeightForWidth())
        self.hueSpinBox.setSizePolicy(sizePolicy)
        self.hueSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hueSpinBox.setMaximum(360)
        self.hueSpinBox.setObjectName("hueSpinBox")
        self.horizontalLayout_3.addWidget(self.hueSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.hueSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hueSlider.sizePolicy().hasHeightForWidth())
        self.hueSlider.setSizePolicy(sizePolicy)
        self.hueSlider.setMaximum(360)
        self.hueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hueSlider.setObjectName("hueSlider")
        self.verticalLayout_3.addWidget(self.hueSlider)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.satLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.satLabel.sizePolicy().hasHeightForWidth())
        self.satLabel.setSizePolicy(sizePolicy)
        self.satLabel.setObjectName("satLabel")
        self.horizontalLayout_4.addWidget(self.satLabel)
        self.satSpinBox = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.satSpinBox.sizePolicy().hasHeightForWidth())
        self.satSpinBox.setSizePolicy(sizePolicy)
        self.satSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.satSpinBox.setMaximum(255)
        self.satSpinBox.setProperty("value", 255)
        self.satSpinBox.setObjectName("satSpinBox")
        self.horizontalLayout_4.addWidget(self.satSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.satSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.satSlider.sizePolicy().hasHeightForWidth())
        self.satSlider.setSizePolicy(sizePolicy)
        self.satSlider.setMaximum(255)
        self.satSlider.setProperty("value", 255)
        self.satSlider.setOrientation(QtCore.Qt.Horizontal)
        self.satSlider.setObjectName("satSlider")
        self.verticalLayout_3.addWidget(self.satSlider)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.valueValue = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueValue.sizePolicy().hasHeightForWidth())
        self.valueValue.setSizePolicy(sizePolicy)
        self.valueValue.setObjectName("valueValue")
        self.horizontalLayout_5.addWidget(self.valueValue)
        self.valueSpinBox = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueSpinBox.sizePolicy().hasHeightForWidth())
        self.valueSpinBox.setSizePolicy(sizePolicy)
        self.valueSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.valueSpinBox.setMaximum(255)
        self.valueSpinBox.setProperty("value", 255)
        self.valueSpinBox.setObjectName("valueSpinBox")
        self.horizontalLayout_5.addWidget(self.valueSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.valueSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueSlider.sizePolicy().hasHeightForWidth())
        self.valueSlider.setSizePolicy(sizePolicy)
        self.valueSlider.setMaximum(255)
        self.valueSlider.setProperty("value", 255)
        self.valueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.valueSlider.setObjectName("valueSlider")
        self.verticalLayout_3.addWidget(self.valueSlider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nStepsLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nStepsLabel.sizePolicy().hasHeightForWidth())
        self.nStepsLabel.setSizePolicy(sizePolicy)
        self.nStepsLabel.setObjectName("nStepsLabel")
        self.horizontalLayout.addWidget(self.nStepsLabel)
        self.stepSpinBox = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepSpinBox.sizePolicy().hasHeightForWidth())
        self.stepSpinBox.setSizePolicy(sizePolicy)
        self.stepSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.stepSpinBox.setMinimum(1)
        self.stepSpinBox.setMaximum(200)
        self.stepSpinBox.setObjectName("stepSpinBox")
        self.horizontalLayout.addWidget(self.stepSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.nStepsSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nStepsSlider.sizePolicy().hasHeightForWidth())
        self.nStepsSlider.setSizePolicy(sizePolicy)
        self.nStepsSlider.setMinimum(1)
        self.nStepsSlider.setMaximum(50)
        self.nStepsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nStepsSlider.setObjectName("nStepsSlider")
        self.verticalLayout_3.addWidget(self.nStepsSlider)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setHorizontalSpacing(11)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.preset_color_20 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_20.sizePolicy().hasHeightForWidth())
        self.preset_color_20.setSizePolicy(sizePolicy)
        self.preset_color_20.setStyleSheet("background-color: rgb(255, 216, 177);\n"
"color: rgb(255, 216, 177);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_20.setObjectName("preset_color_20")
        self.gridLayout.addWidget(self.preset_color_20, 9, 2, 1, 1)
        self.preset_color_8 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_8.sizePolicy().hasHeightForWidth())
        self.preset_color_8.setSizePolicy(sizePolicy)
        self.preset_color_8.setStyleSheet("background-color: rgb(230, 25, 75);\n"
"color: rgb(230, 25, 75);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_8.setObjectName("preset_color_8")
        self.gridLayout.addWidget(self.preset_color_8, 3, 0, 1, 1)
        self.preset_color_16 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_16.sizePolicy().hasHeightForWidth())
        self.preset_color_16.setSizePolicy(sizePolicy)
        self.preset_color_16.setStyleSheet("background-color: rgb(145, 30, 180);\n"
"color: rgb(145, 30, 180);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_16.setObjectName("preset_color_16")
        self.gridLayout.addWidget(self.preset_color_16, 4, 5, 1, 1)
        self.preset_color_7 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_7.sizePolicy().hasHeightForWidth())
        self.preset_color_7.setSizePolicy(sizePolicy)
        self.preset_color_7.setStyleSheet("background-color: rgb(245, 130, 49);\n"
"color: rgb(245, 130, 49);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_7.setObjectName("preset_color_7")
        self.gridLayout.addWidget(self.preset_color_7, 3, 2, 1, 1)
        self.preset_color_17 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_17.sizePolicy().hasHeightForWidth())
        self.preset_color_17.setSizePolicy(sizePolicy)
        self.preset_color_17.setStyleSheet("background-color: rgb(193, 64, 244);\n"
"color: rgb(193, 64, 244);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_17.setObjectName("preset_color_17")
        self.gridLayout.addWidget(self.preset_color_17, 4, 8, 1, 1)
        self.preset_color_19 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_19.sizePolicy().hasHeightForWidth())
        self.preset_color_19.setSizePolicy(sizePolicy)
        self.preset_color_19.setStyleSheet("background-color: rgb(250, 190, 212);\n"
"color: rgb(250, 190, 212);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_19.setObjectName("preset_color_19")
        self.gridLayout.addWidget(self.preset_color_19, 9, 0, 1, 1)
        self.preset_color_6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_6.sizePolicy().hasHeightForWidth())
        self.preset_color_6.setSizePolicy(sizePolicy)
        self.preset_color_6.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_6.setObjectName("preset_color_6")
        self.gridLayout.addWidget(self.preset_color_6, 2, 9, 1, 1)
        self.preset_color_18 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_18.sizePolicy().hasHeightForWidth())
        self.preset_color_18.setSizePolicy(sizePolicy)
        self.preset_color_18.setStyleSheet("background-color:rgb(240, 50, 230);\n"
"color: rgb(240, 50, 230);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_18.setObjectName("preset_color_18")
        self.gridLayout.addWidget(self.preset_color_18, 4, 9, 1, 1)
        self.preset_color_14 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_14.sizePolicy().hasHeightForWidth())
        self.preset_color_14.setSizePolicy(sizePolicy)
        self.preset_color_14.setStyleSheet("background-color: rgb(66, 212, 244);\n"
"color: rgb(66, 212, 244);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_14.setObjectName("preset_color_14")
        self.gridLayout.addWidget(self.preset_color_14, 4, 2, 1, 1)
        self.preset_color_11 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_11.sizePolicy().hasHeightForWidth())
        self.preset_color_11.setSizePolicy(sizePolicy)
        self.preset_color_11.setStyleSheet("background-color: rgb(60, 180, 75);\n"
"color: rgb(60, 180, 75);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_11.setObjectName("preset_color_11")
        self.gridLayout.addWidget(self.preset_color_11, 3, 8, 1, 1)
        self.preset_color_10 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_10.sizePolicy().hasHeightForWidth())
        self.preset_color_10.setSizePolicy(sizePolicy)
        self.preset_color_10.setStyleSheet("background-color: rgb(255, 225, 25);\n"
"color: rgb(255, 225, 25);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_10.setObjectName("preset_color_10")
        self.gridLayout.addWidget(self.preset_color_10, 3, 4, 1, 1)
        self.preset_color_9 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_9.sizePolicy().hasHeightForWidth())
        self.preset_color_9.setSizePolicy(sizePolicy)
        self.preset_color_9.setStyleSheet("background-color: rgb(191, 239, 69);\n"
"color: rgb(191, 239, 69);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_9.setObjectName("preset_color_9")
        self.gridLayout.addWidget(self.preset_color_9, 3, 5, 1, 1)
        self.preset_color_12 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_12.sizePolicy().hasHeightForWidth())
        self.preset_color_12.setSizePolicy(sizePolicy)
        self.preset_color_12.setStyleSheet("background-color:rgb(35, 120, 82);\n"
"color: rgb(35, 120, 82);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_12.setObjectName("preset_color_12")
        self.gridLayout.addWidget(self.preset_color_12, 3, 9, 1, 1)
        self.preset_color_24 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_24.sizePolicy().hasHeightForWidth())
        self.preset_color_24.setSizePolicy(sizePolicy)
        self.preset_color_24.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_24.setObjectName("preset_color_24")
        self.gridLayout.addWidget(self.preset_color_24, 9, 9, 1, 1)
        self.preset_color_21 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_21.sizePolicy().hasHeightForWidth())
        self.preset_color_21.setSizePolicy(sizePolicy)
        self.preset_color_21.setStyleSheet("background-color: rgb(255, 250, 200);\n"
"color: rgb(255, 250, 200);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_21.setObjectName("preset_color_21")
        self.gridLayout.addWidget(self.preset_color_21, 9, 4, 1, 1)
        self.preset_color_22 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_22.sizePolicy().hasHeightForWidth())
        self.preset_color_22.setSizePolicy(sizePolicy)
        self.preset_color_22.setStyleSheet("background-color: rgb(170, 255, 195);\n"
"color: rgb(170, 255, 195);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_22.setObjectName("preset_color_22")
        self.gridLayout.addWidget(self.preset_color_22, 9, 5, 1, 1)
        self.preset_color_23 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_23.sizePolicy().hasHeightForWidth())
        self.preset_color_23.setSizePolicy(sizePolicy)
        self.preset_color_23.setStyleSheet("background-color: rgb(220, 190, 255);\n"
"color: rgb(220, 190, 255);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_23.setObjectName("preset_color_23")
        self.gridLayout.addWidget(self.preset_color_23, 9, 8, 1, 1)
        self.preset_color_13 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_13.sizePolicy().hasHeightForWidth())
        self.preset_color_13.setSizePolicy(sizePolicy)
        self.preset_color_13.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(0, 255, 255);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_13.setObjectName("preset_color_13")
        self.gridLayout.addWidget(self.preset_color_13, 4, 0, 1, 1)
        self.preset_color_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_3.sizePolicy().hasHeightForWidth())
        self.preset_color_3.setSizePolicy(sizePolicy)
        self.preset_color_3.setStyleSheet("background-color: rgb(128, 128, 0);\n"
"color: rgb(128, 128, 0);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_3.setObjectName("preset_color_3")
        self.gridLayout.addWidget(self.preset_color_3, 2, 4, 1, 1)
        self.preset_color_4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_4.sizePolicy().hasHeightForWidth())
        self.preset_color_4.setSizePolicy(sizePolicy)
        self.preset_color_4.setStyleSheet("background-color: rgb(70, 153, 144);\n"
"color: rgb(70, 153, 144);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_4.setObjectName("preset_color_4")
        self.gridLayout.addWidget(self.preset_color_4, 2, 5, 1, 1)
        self.preset_color_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_2.sizePolicy().hasHeightForWidth())
        self.preset_color_2.setSizePolicy(sizePolicy)
        self.preset_color_2.setStyleSheet("background-color: rgb(154, 99, 36);\n"
"color:rgb(154, 99, 36);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;\n"
"")
        self.preset_color_2.setObjectName("preset_color_2")
        self.gridLayout.addWidget(self.preset_color_2, 2, 2, 1, 1)
        self.preset_color_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_5.sizePolicy().hasHeightForWidth())
        self.preset_color_5.setSizePolicy(sizePolicy)
        self.preset_color_5.setStyleSheet("background-color: rgb(0, 0, 117);\n"
"color: rgb(0, 0, 117);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_5.setObjectName("preset_color_5")
        self.gridLayout.addWidget(self.preset_color_5, 2, 8, 1, 1)
        self.preset_color_1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_1.sizePolicy().hasHeightForWidth())
        self.preset_color_1.setSizePolicy(sizePolicy)
        self.preset_color_1.setStyleSheet("background-color: rgb(128, 0, 0);\n"
"color: rgb(128, 0, 0);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1;\n"
"border-radius:10px;")
        self.preset_color_1.setCheckable(False)
        self.preset_color_1.setObjectName("preset_color_1")
        self.gridLayout.addWidget(self.preset_color_1, 2, 0, 1, 1)
        self.preset_color_15 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_color_15.sizePolicy().hasHeightForWidth())
        self.preset_color_15.setSizePolicy(sizePolicy)
        self.preset_color_15.setStyleSheet("background-color: rgb(67, 99, 216);\n"
"color: rgb(67, 99, 216);\n"
"border-color: rgb(67, 67, 67);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;")
        self.preset_color_15.setObjectName("preset_color_15")
        self.gridLayout.addWidget(self.preset_color_15, 4, 4, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.hueLabel.setText(_translate("Form", "Hue"))
        self.satLabel.setText(_translate("Form", "Saturation"))
        self.valueValue.setText(_translate("Form", "Value"))
        self.nStepsLabel.setText(_translate("Form", "Steps"))
        self.preset_color_20.setToolTip(_translate("Form", "Apricot"))
        self.preset_color_20.setText(_translate("Form", "#ffd8b1"))
        self.preset_color_8.setToolTip(_translate("Form", "Red"))
        self.preset_color_8.setText(_translate("Form", "#e6194B"))
        self.preset_color_16.setToolTip(_translate("Form", "Purple"))
        self.preset_color_16.setText(_translate("Form", "#911eb4"))
        self.preset_color_7.setToolTip(_translate("Form", "Orange"))
        self.preset_color_7.setText(_translate("Form", "#f58231"))
        self.preset_color_17.setToolTip(_translate("Form", "Violet"))
        self.preset_color_17.setText(_translate("Form", "#c140f4"))
        self.preset_color_19.setToolTip(_translate("Form", "Pink"))
        self.preset_color_19.setText(_translate("Form", "#fabed4"))
        self.preset_color_6.setToolTip(_translate("Form", "Black"))
        self.preset_color_6.setText(_translate("Form", "#000000"))
        self.preset_color_18.setToolTip(_translate("Form", "Magenta"))
        self.preset_color_18.setText(_translate("Form", "#f032e6"))
        self.preset_color_14.setToolTip(_translate("Form", "Cerulean"))
        self.preset_color_14.setText(_translate("Form", "#42d4f4"))
        self.preset_color_11.setToolTip(_translate("Form", "Green"))
        self.preset_color_11.setText(_translate("Form", "#3cb44b"))
        self.preset_color_10.setToolTip(_translate("Form", "Yellow"))
        self.preset_color_10.setText(_translate("Form", "#ffe119"))
        self.preset_color_9.setToolTip(_translate("Form", "Lime"))
        self.preset_color_9.setText(_translate("Form", "#bfef45"))
        self.preset_color_12.setToolTip(_translate("Form", "Turtle Green"))
        self.preset_color_12.setText(_translate("Form", "#237852"))
        self.preset_color_24.setToolTip(_translate("Form", "White"))
        self.preset_color_24.setText(_translate("Form", "#ffffff"))
        self.preset_color_21.setToolTip(_translate("Form", "Beige"))
        self.preset_color_21.setText(_translate("Form", "#fffac8"))
        self.preset_color_22.setToolTip(_translate("Form", "Mint"))
        self.preset_color_22.setText(_translate("Form", "#aaffc3"))
        self.preset_color_23.setToolTip(_translate("Form", "Lavender"))
        self.preset_color_23.setText(_translate("Form", "#dcbeff"))
        self.preset_color_13.setToolTip(_translate("Form", "Cyan"))
        self.preset_color_13.setText(_translate("Form", "#00ffff"))
        self.preset_color_3.setToolTip(_translate("Form", "Olive"))
        self.preset_color_3.setText(_translate("Form", "#808000"))
        self.preset_color_4.setToolTip(_translate("Form", "Teal"))
        self.preset_color_4.setText(_translate("Form", "#469990"))
        self.preset_color_2.setToolTip(_translate("Form", "Brown"))
        self.preset_color_2.setText(_translate("Form", "#9A6324"))
        self.preset_color_5.setToolTip(_translate("Form", "Navy"))
        self.preset_color_5.setText(_translate("Form", "#000075"))
        self.preset_color_1.setToolTip(_translate("Form", "Maroon"))
        self.preset_color_1.setText(_translate("Form", "#800000"))
        self.preset_color_15.setToolTip(_translate("Form", "Blue"))
        self.preset_color_15.setText(_translate("Form", "#4363d8"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QWidget()
    window = Ui_Form()
    window.setupUi(main)
    main.show()
    from Ui_Functions import Ui_Functions
    functions = Ui_Functions(window)

    sys.exit(app.exec_())
else:
    print(__name__, "hh")