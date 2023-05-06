from PyQt5.QtWidgets import QApplication
from pyqt_shadow_frame_window_example import MainWindow, ShadowFrame

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = MainWindow()
    window = ShadowFrame(widget)
    window.show()
    app.exec()
