# import headers
from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget, QMenu, QSizeGrip,
                               QSpacerItem, QSizePolicy, QDockWidget, QTextEdit, QFileDialog,
                               QToolBar, QVBoxLayout, QGraphicsDropShadowEffect)
from PySide6.QtCore import (Qt, QPropertyAnimation, QRect, QEasingCurve, QPoint,
                            QSize, QObject, Signal, QRunnable, Slot, QThreadPool, QPointF)
from PySide6.QtGui import (QIcon, QAction, QResizeEvent, QCursor, QMouseEvent, QPixmap, QKeyEvent,
                           QClipboard, QColor, QTextFormat, QTextCharFormat, QTextCursor, QBrush, QTextBlockFormat)
# import local file
from ui.main_app_ui import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() |
                            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
