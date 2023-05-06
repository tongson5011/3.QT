from PySide6.QtWidgets import QMainWindow, QWidget, QDockWidget, QApplication, QTextEdit, QScrollBar
from PySide6.QtCore import Qt


class CustomScrollBar(QScrollBar):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
                    QScrollBar:vertical {
                        border: 0px solid #999999;
                        background: #efefef;
                        width: 8px;
                        margin: 5px 0px 5px 0px;
                      }
                    QScrollBar::handle:vertical {
                        min-height: 30px;
                        border: 0px solid red;
                        border-radius: 2px;
                        background-color: #838383;
                    }
                    QScrollBar::add-line:vertical {
                        height: 0px;
                        subcontrol-position: bottom;
                        subcontrol-origin: margin;
                    }
                    QScrollBar::sub-line:vertical {
                        height: 0px;
                        subcontrol-position: top;
                        subcontrol-origin: margin;
                    }

                    """)
        # Add custom styling here


class Edit_UI(QMainWindow):
    def __init__(self):
        super(Edit_UI, self).__init__()
        # create dock widget
        self.dock_cn = QDockWidget("CN", self)
        self.dock_vi = QDockWidget("VI", self)
        self.dock_en = QDockWidget("EN", self)
        self.dock_en_vi = QDockWidget("EN_VI", self)
        self.dock_vietPhrase = QDockWidget("VietPhrase", self)
        self.dock_HanViet = QDockWidget("Han Viet", self)
        self.dock_Properties = QDockWidget("Properties", self)

        # set line center
        self.edit_line = QWidget()
        self.edit_line.setObjectName('edit_line')
        self.edit_line.setFixedWidth(1)
        # self.edit_line.setStyleSheet('background-color: #000;')
        self.setCentralWidget(self.edit_line)
        # add dock widget
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_cn)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_en)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_vi)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_en_vi)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_vietPhrase)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_HanViet)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_Properties)
        self.tabifyDockWidget(self.dock_cn, self.dock_HanViet)
        self.tabifyDockWidget(self.dock_cn, self.dock_Properties)
        self.tabifyDockWidget(self.dock_en, self.dock_vietPhrase)

        # create edit
        self.edit_cn = QTextEdit()
        self.edit_vi = QTextEdit()
        self.edit_en = QTextEdit()
        self.edit_en_vi = QTextEdit()
        self.edit_vietPhrase = QTextEdit()
        self.edit_HanViet = QTextEdit()
        self.edit_Properties = QTextEdit()

        # add text edit to dock widget
        self.dock_cn.setWidget(self.edit_cn)
        self.dock_en.setWidget(self.edit_en)
        self.dock_en_vi.setWidget(self.edit_en_vi)
        self.dock_HanViet.setWidget(self.edit_HanViet)
        self.dock_vi.setWidget(self.edit_vi)
        self.dock_vietPhrase.setWidget(self.edit_vietPhrase)
        self.dock_Properties.setWidget(self.edit_Properties)

        self.dock_cn.raise_()

        # add custom scroll
        # scroll_bar = QScrollBar(Qt.Vertical)
        # =============================================
        # add Edit CN scroll
        self.edit_cn.setVerticalScrollBar(CustomScrollBar())
        # self.edit_cn.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # add Edit Han Viet scroll
        self.edit_HanViet.setVerticalScrollBar(CustomScrollBar())
        # self.edit_HanViet.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # add Edit VI scroll
        self.edit_vi.setVerticalScrollBar(CustomScrollBar())
        # self.edit_vi.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # add Edit EN scroll
        self.edit_en.setVerticalScrollBar(CustomScrollBar())
        # self.edit_en.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # add Edit VietPhrase scroll
        self.edit_vietPhrase.setVerticalScrollBar(CustomScrollBar())
        # self.edit_vietPhrase.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # add Edit EN_VI scroll
        self.edit_en_vi.setVerticalScrollBar(CustomScrollBar())
        # self.edit_en_vi.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # add Edit Properties scroll
        self.edit_Properties.setVerticalScrollBar(CustomScrollBar())
        # self.edit_en_vi.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # =============================================

        # set style
        # scroll_bar.setStyleSheet("background-color: #f0f0f0;")
        self.setStyleSheet(
            '''
            * {
                background-color: #e8e8e8;
            }
            #edit_line {
                background-color: #000;
                } 
            QTextEdit{
                    border-radius: 8px; 
                    background-color: #fff;
                    font-size: 14pt;
                    font-family: 'Segoe UI'
                } 
            QDockWidget{
                    border-radius: 8px; 
                    background-color: #e8e8e8;
                }
                ''')


if __name__ == '__main__':
    app = QApplication([])
    window = Edit_UI()
    window.show()
    app.exec()
