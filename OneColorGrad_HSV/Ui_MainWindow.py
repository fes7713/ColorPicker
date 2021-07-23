# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.colorDisplay = QtWidgets.QWidget(self.centralwidget)
        self.colorDisplay.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorDisplay.sizePolicy().hasHeightForWidth())
        self.colorDisplay.setSizePolicy(sizePolicy)
        self.colorDisplay.setObjectName("colorDisplay")
        self.horizontalLayout_2.addWidget(self.colorDisplay)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hueLabel = QtWidgets.QLabel(self.centralwidget)
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
        self.hueSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hueSpinBox.sizePolicy().hasHeightForWidth())
        self.hueSpinBox.setSizePolicy(sizePolicy)
        self.hueSpinBox.setMaximum(360)
        self.hueSpinBox.setObjectName("hueSpinBox")
        self.horizontalLayout_3.addWidget(self.hueSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.hueSlider = QtWidgets.QSlider(self.centralwidget)
        self.hueSlider.setMaximum(360)
        self.hueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hueSlider.setObjectName("hueSlider")
        self.verticalLayout_2.addWidget(self.hueSlider)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.satLabel = QtWidgets.QLabel(self.centralwidget)
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
        self.satSpinBox = QtWidgets.QSpinBox(self.centralwidget)
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
        self.satSlider = QtWidgets.QSlider(self.centralwidget)
        self.satSlider.setMaximum(255)
        self.satSlider.setProperty("value", 255)
        self.satSlider.setOrientation(QtCore.Qt.Horizontal)
        self.satSlider.setObjectName("satSlider")
        self.verticalLayout_2.addWidget(self.satSlider)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.valueValue = QtWidgets.QLabel(self.centralwidget)
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
        self.valueSpinBox = QtWidgets.QSpinBox(self.centralwidget)
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
        self.valueSlider = QtWidgets.QSlider(self.centralwidget)
        self.valueSlider.setMaximum(255)
        self.valueSlider.setProperty("value", 255)
        self.valueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.valueSlider.setObjectName("valueSlider")
        self.verticalLayout_2.addWidget(self.valueSlider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nStepsLabel = QtWidgets.QLabel(self.centralwidget)
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
        self.stepSpinBox = QtWidgets.QSpinBox(self.centralwidget)
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
        self.nStepsSlider = QtWidgets.QSlider(self.centralwidget)
        self.nStepsSlider.setMinimum(1)
        self.nStepsSlider.setMaximum(200)
        self.nStepsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nStepsSlider.setObjectName("nStepsSlider")
        self.verticalLayout_2.addWidget(self.nStepsSlider)
        self.subColorDisplay = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subColorDisplay.sizePolicy().hasHeightForWidth())
        self.subColorDisplay.setSizePolicy(sizePolicy)
        self.subColorDisplay.setMinimumSize(QtCore.QSize(100, 100))
        self.subColorDisplay.setObjectName("subColorDisplay")
        self.verticalLayout_2.addWidget(self.subColorDisplay)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hueLabel.setText(_translate("MainWindow", "Hue"))
        self.satLabel.setText(_translate("MainWindow", "Saturation"))
        self.valueValue.setText(_translate("MainWindow", "Value"))
        self.nStepsLabel.setText(_translate("MainWindow", "Steps"))
