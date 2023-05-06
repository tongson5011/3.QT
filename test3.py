from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget, QMenu, QSizeGrip,
                               QSpacerItem, QSizePolicy, QDockWidget, QTextEdit, QFileDialog,
                               QToolBar, QVBoxLayout, QGraphicsDropShadowEffect)
from PySide6.QtCore import (Qt, QPropertyAnimation, QRect, QEasingCurve, QPoint,
                            QSize, QObject, Signal, QRunnable, Slot, QThreadPool, QPointF, QEvent)
from PySide6.QtGui import (QIcon, QAction, QResizeEvent, QCursor, QMouseEvent, QPixmap, QKeyEvent,
                           QClipboard, QColor, QTextFormat, QTextCharFormat, QTextCursor, QBrush, QTextBlockFormat)

from pyqt_frameless_window import framelessWindow
# import local file
from ui.main_app_ui import Ui_MainWindow
from ui.menu_ui import Menu_ui
from ui.Edit_ui import Edit_UI
import sys
import os
PATH = os.path.dirname(os.path.abspath(__file__))
maximize_app = os.path.join(PATH, 'maximize_app.css')
normalize_app = os.path.join(PATH, 'normalize_app.css')
app_logo = os.path.join(PATH, 'assects\icon\logo.png')

with open(normalize_app, 'r') as f:
    app_normal_style = f.read()
with open(maximize_app, 'r') as f:
    app_max_style = f.read()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # app config
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() |
                            Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # config global veriable
        self.app_resize = True
        self.app_width = self.geometry().width()
        self.app_height = self.geometry().height()
        self.app_margin = 4
        self.app_crusor_shape = None

        # handle resize, move app
        self.setMouseTracking(True)
        self.installEventFilter(self)
        self.main_app.enterEvent = self.handleEnterEvent
        self.main_app.leaveEvent = self.handleLeaveEvent

        # set style
        self.setStyleSheet(app_normal_style)
        # handle minimize, maximize, close app
        self.app_close.clicked.connect(lambda: self.close())

    def handleEnterEvent(self, e):
        self.app_resize = False
        self.setCursor(Qt.ArrowCursor)

    def handleLeaveEvent(self, e):
        self.app_resize = True

    # handle evenr filter
    def eventFilter(self, obj, event):
        if event.type() == 129 and not self.isMaximized() and self.app_resize:
            local_width = int(event.position().x())
            local_height = int(event.position().y())
            min_width = self.app_width - local_width
            min_height = self.app_height - local_height

            # print('position', event.position())
            # print('globalPosition', event.globalPosition())
            self.handleSetCursor(local_width, local_height,
                                 min_width, min_height)
        return super().eventFilter(obj, event)

    # set app resize cursor
    def handleSetCursor(self, local_width, local_height, min_width, min_height):
        # top - left
        if (local_width < self.app_margin + 4 and local_height < self.app_margin + 4):
            self.setCursor(Qt.SizeFDiagCursor)
            self.app_crusor_shape = 'top_left'

        # top - right
        elif (min_width < self.app_margin + 4 and local_height < self.app_margin + 4):
            self.setCursor(Qt.SizeBDiagCursor)
            self.app_crusor_shape = 'top_right'

        # bottom - left
        elif (local_width < self.app_margin + 4 and min_height < self.app_margin + 4):
            self.setCursor(Qt.SizeBDiagCursor)
            self.app_crusor_shape = 'bottom_left'

        # bottom - right
        elif (min_width < self.app_margin + 4 and min_height < self.app_margin + 4):
            self.setCursor(Qt.SizeFDiagCursor)
            self.app_crusor_shape = 'bottom_right'

        # left
        elif local_width < self.app_margin:
            self.setCursor(Qt.SizeHorCursor)
            self.app_crusor_shape = 'left'

        # right
        elif (min_width < self.app_margin):
            self.setCursor(Qt.SizeHorCursor)
            self.app_crusor_shape = 'right'

        # top
        elif (local_height < self.app_margin):
            self.setCursor(Qt.SizeVerCursor)
            self.app_crusor_shape = 'top'

        # bottom
        elif (min_height < self.app_margin):
            self.setCursor(Qt.SizeVerCursor)
            self.app_crusor_shape = 'bottom'

        else:
            self.setCursor(Qt.ArrowCursor)
            self.app_crusor_shape = None

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if not self.isMaximized() and self.app_resize:
            self.handleResizeApp()
        return super().mousePressEvent(event)
    # set resize app

    def handleResizeApp(self):
        window = self.window().windowHandle()
        # resize top - left
        if self.app_crusor_shape == 'top_left':
            window.startSystemResize(Qt.TopEdge | Qt.LeftEdge)

        # resize top - right
        elif self.app_crusor_shape == 'top_right':
            window.startSystemResize(Qt.TopEdge | Qt.RightEdge)

        # resize bottom - left
        elif self.app_crusor_shape == 'bottom_left':
            window.startSystemResize(Qt.BottomEdge | Qt.LeftEdge)

        # resize bottom - right
        elif self.app_crusor_shape == 'bottom_right':
            window.startSystemResize(Qt.BottomEdge | Qt.RightEdge)

        # resize left
        elif self.app_crusor_shape == 'left':
            window.startSystemResize(Qt.LeftEdge)

        # resize right
        elif self.app_crusor_shape == 'right':
            window.startSystemResize(Qt.RightEdge)

        # resize top
        elif self.app_crusor_shape == 'top':
            window.startSystemResize(Qt.TopEdge)

        # resize bottom
        elif self.app_crusor_shape == 'bottom':
            window.startSystemResize(Qt.BottomEdge)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
