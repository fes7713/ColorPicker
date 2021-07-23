from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class _Bar(QtWidgets.QWidget):
    clickedValue = QtCore.pyqtSignal(QColor)

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
                for i in range(self.nSteps):
                    for j in range(self.nSteps):
                        color = QColor()
                        color.setHsv(self.colors[j][i][0], self.colors[j][i][1], self.colors[j][i][2])
                        brush.setColor(color)
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

        if 0 <= x_ind < self.nSteps and 0 <= y_ind < self.nSteps:
            color = self.colors[y_ind][x_ind]
            Color = QColor()
            Color.setHsv(int(color[0]), int(color[1]), int(color[2]))
            self.clickedValue.emit(Color)

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


        if 0 <= x_ind < self.nSteps and 0 <= y_ind < self.nSteps:
            color = self.colors[y_ind][x_ind]
            Color = QColor()
            Color.setHsv(int(color[0]), int(color[1]), int(color[2]))
            self.clickedValue.emit(Color)