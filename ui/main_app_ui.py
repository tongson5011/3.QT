# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_app.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"/*\n"
"QFrame {\n"
"border: 1px solid #ccc;\n"
"}*/\n"
"/* global */\n"
"/*\n"
"#centralwidget {\n"
"	\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 10px;\n"
"	\n"
"}\n"
"*/\n"
"/* main*/\n"
"#main_app {\n"
"	background-color: rgb(239, 239, 239);\n"
"	border: 1px solid #ccc ;\n"
"	border-radius: 10px;\n"
"}\n"
"/* header btn */\n"
"#main_app #app_close {\n"
"	background-color: rgb(234, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"#main_app #app_maximize {\n"
"	background-color: rgb(200, 200, 16);\n"
"	border-radius: 9px;\n"
"}\n"
"#main_app #app_minimize {\n"
"	background-color: rgb(85, 255, 127);\n"
"	border-radius: 9px;\n"
"}\n"
"/* hover close, maximize, minimize*/\n"
"#main_app #app_close:hover {\n"
"	background-color: rgba(234, 0, 0,128);\n"
"	border-radius: 10px;\n"
"}\n"
"#main_app #app_maximize:hover {\n"
"	background-color: rgba(200, 200, 16,128);\n"
"	border-radius: 9px;\n"
"}\n"
"#main_app #app_minimize:hover {\n"
"	background-color: rgba(85, 255, 127,128);\n"
"	border-radius: 9px;\n"
"}\n"
"\n"
"/"
                        "*footer */\n"
"#app_message {\n"
"	background-color: rgb(40, 40, 40);\n"
"    color: #74cf62;\n"
"    font-size: 10pt;\n"
"	border: 0px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.main_app = QWidget(self.centralwidget)
        self.main_app.setObjectName(u"main_app")
        self.verticalLayout_2 = QVBoxLayout(self.main_app)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_app)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 40))
        self.header_frame.setMaximumSize(QSize(16777215, 40))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.header_layouts = QHBoxLayout(self.header_frame)
        self.header_layouts.setSpacing(6)
        self.header_layouts.setObjectName(u"header_layouts")
        self.header_layouts.setContentsMargins(6, 0, 6, 0)
        self.app_icon = QLabel(self.header_frame)
        self.app_icon.setObjectName(u"app_icon")
        self.app_icon.setMinimumSize(QSize(25, 25))
        self.app_icon.setMaximumSize(QSize(25, 25))
        self.app_icon.setPixmap(QPixmap(u"assects/icon/logo.png"))
        self.app_icon.setScaledContents(True)

        self.header_layouts.addWidget(self.app_icon, 0, Qt.AlignVCenter)

        self.app_menu = QHBoxLayout()
        self.app_menu.setObjectName(u"app_menu")

        self.header_layouts.addLayout(self.app_menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.header_layouts.addItem(self.horizontalSpacer)

        self.app_minimize = QPushButton(self.header_frame)
        self.app_minimize.setObjectName(u"app_minimize")
        self.app_minimize.setMinimumSize(QSize(0, 18))
        self.app_minimize.setMaximumSize(QSize(18, 18))

        self.header_layouts.addWidget(self.app_minimize, 0, Qt.AlignVCenter)

        self.app_maximize = QPushButton(self.header_frame)
        self.app_maximize.setObjectName(u"app_maximize")
        self.app_maximize.setMinimumSize(QSize(0, 18))
        self.app_maximize.setMaximumSize(QSize(18, 18))

        self.header_layouts.addWidget(self.app_maximize, 0, Qt.AlignVCenter)

        self.app_close = QPushButton(self.header_frame)
        self.app_close.setObjectName(u"app_close")
        self.app_close.setMinimumSize(QSize(0, 20))
        self.app_close.setMaximumSize(QSize(20, 20))

        self.header_layouts.addWidget(self.app_close, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.header_frame)

        self.content_frame = QFrame(self.main_app)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.content_layouts = QVBoxLayout(self.content_frame)
        self.content_layouts.setSpacing(0)
        self.content_layouts.setObjectName(u"content_layouts")
        self.content_layouts.setContentsMargins(0, 0, 0, 0)
        self.content_title_frame = QFrame(self.content_frame)
        self.content_title_frame.setObjectName(u"content_title_frame")
        self.content_title_frame.setMaximumSize(QSize(16777215, 60))
        self.content_title_frame.setFrameShape(QFrame.StyledPanel)
        self.content_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content_title_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.content_title_left = QFrame(self.content_title_frame)
        self.content_title_left.setObjectName(u"content_title_left")
        self.content_title_left.setFrameShape(QFrame.StyledPanel)
        self.content_title_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_title_left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_search_bottom = QHBoxLayout()
        self.content_search_bottom.setSpacing(8)
        self.content_search_bottom.setObjectName(u"content_search_bottom")
        self.content_search_bottom.setContentsMargins(6, -1, 6, -1)
        self.search_label = QLabel(self.content_title_left)
        self.search_label.setObjectName(u"search_label")

        self.content_search_bottom.addWidget(self.search_label)

        self.search_input = QLineEdit(self.content_title_left)
        self.search_input.setObjectName(u"search_input")

        self.content_search_bottom.addWidget(self.search_input)

        self.search_push = QPushButton(self.content_title_left)
        self.search_push.setObjectName(u"search_push")

        self.content_search_bottom.addWidget(self.search_push)


        self.verticalLayout_3.addLayout(self.content_search_bottom)

        self.content_search_top = QHBoxLayout()
        self.content_search_top.setSpacing(10)
        self.content_search_top.setObjectName(u"content_search_top")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.content_search_top.addItem(self.horizontalSpacer_4)

        self.app_prev = QPushButton(self.content_title_left)
        self.app_prev.setObjectName(u"app_prev")

        self.content_search_top.addWidget(self.app_prev, 0, Qt.AlignVCenter)

        self.app_next = QPushButton(self.content_title_left)
        self.app_next.setObjectName(u"app_next")

        self.content_search_top.addWidget(self.app_next, 0, Qt.AlignVCenter)

        self.app_paste = QPushButton(self.content_title_left)
        self.app_paste.setObjectName(u"app_paste")

        self.content_search_top.addWidget(self.app_paste, 0, Qt.AlignVCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.content_search_top.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.content_search_top)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.content_title_left)

        self.content_title_right = QFrame(self.content_title_frame)
        self.content_title_right.setObjectName(u"content_title_right")
        self.content_title_right.setFrameShape(QFrame.StyledPanel)
        self.content_title_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_title_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.content_options_top = QHBoxLayout()
        self.content_options_top.setSpacing(0)
        self.content_options_top.setObjectName(u"content_options_top")
        self.content_options_top.setContentsMargins(6, -1, 6, -1)
        self.translate_options = QComboBox(self.content_title_right)
        self.translate_options.addItem("")
        self.translate_options.addItem("")
        self.translate_options.addItem("")
        self.translate_options.addItem("")
        self.translate_options.addItem("")
        self.translate_options.addItem("")
        self.translate_options.addItem("")
        self.translate_options.setObjectName(u"translate_options")
        self.translate_options.setMaximumSize(QSize(115, 16777215))

        self.content_options_top.addWidget(self.translate_options, 0, Qt.AlignLeft)

        self.translate_push = QPushButton(self.content_title_right)
        self.translate_push.setObjectName(u"translate_push")

        self.content_options_top.addWidget(self.translate_push, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.content_options_top.addItem(self.horizontalSpacer_3)

        self.checkBox = QCheckBox(self.content_title_right)
        self.checkBox.setObjectName(u"checkBox")

        self.content_options_top.addWidget(self.checkBox, 0, Qt.AlignRight)

        self.app_scroll = QCheckBox(self.content_title_right)
        self.app_scroll.setObjectName(u"app_scroll")
        self.app_scroll.setMinimumSize(QSize(64, 0))

        self.content_options_top.addWidget(self.app_scroll, 0, Qt.AlignRight)


        self.verticalLayout_4.addLayout(self.content_options_top)

        self.content_options_bottom = QHBoxLayout()
        self.content_options_bottom.setObjectName(u"content_options_bottom")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.content_options_bottom.addItem(self.horizontalSpacer_2)

        self.app_state_message = QCheckBox(self.content_title_right)
        self.app_state_message.setObjectName(u"app_state_message")
        self.app_state_message.setChecked(True)

        self.content_options_bottom.addWidget(self.app_state_message, 0, Qt.AlignTop)


        self.verticalLayout_4.addLayout(self.content_options_bottom)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.content_title_right)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.content_layouts.addWidget(self.content_title_frame)

        self.content_main_frame = QFrame(self.content_frame)
        self.content_main_frame.setObjectName(u"content_main_frame")
        self.content_main_frame.setFrameShape(QFrame.StyledPanel)
        self.content_main_frame.setFrameShadow(QFrame.Raised)
        self.content_main_layouts = QVBoxLayout(self.content_main_frame)
        self.content_main_layouts.setSpacing(0)
        self.content_main_layouts.setObjectName(u"content_main_layouts")
        self.content_main_layouts.setContentsMargins(0, 0, 0, 0)

        self.content_layouts.addWidget(self.content_main_frame)


        self.verticalLayout_2.addWidget(self.content_frame)

        self.footer_frame = QFrame(self.main_app)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMinimumSize(QSize(0, 80))
        self.footer_frame.setMaximumSize(QSize(16777215, 80))
        self.footer_layouts = QHBoxLayout(self.footer_frame)
        self.footer_layouts.setSpacing(0)
        self.footer_layouts.setObjectName(u"footer_layouts")
        self.footer_layouts.setContentsMargins(0, 0, 0, 0)
        self.app_message = QPlainTextEdit(self.footer_frame)
        self.app_message.setObjectName(u"app_message")
        self.app_message.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.app_message.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.app_message.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.app_message.setReadOnly(True)

        self.footer_layouts.addWidget(self.app_message)


        self.verticalLayout_2.addWidget(self.footer_frame)


        self.verticalLayout.addWidget(self.main_app)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_icon.setText("")
        self.app_minimize.setText("")
        self.app_maximize.setText("")
        self.app_close.setText("")
        self.search_label.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.search_push.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.app_prev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.app_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.app_paste.setText(QCoreApplication.translate("MainWindow", u"Paste from Clipboard", None))
        self.translate_options.setItemText(0, QCoreApplication.translate("MainWindow", u"Translate All", None))
        self.translate_options.setItemText(1, QCoreApplication.translate("MainWindow", u"Translate CN", None))
        self.translate_options.setItemText(2, QCoreApplication.translate("MainWindow", u"Translate VI", None))
        self.translate_options.setItemText(3, QCoreApplication.translate("MainWindow", u"Translate EN", None))
        self.translate_options.setItemText(4, QCoreApplication.translate("MainWindow", u"Translate VietPhrase", None))
        self.translate_options.setItemText(5, QCoreApplication.translate("MainWindow", u"Translate Han Viet", None))
        self.translate_options.setItemText(6, "")

        self.translate_push.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"HightLight", None))
        self.app_scroll.setText(QCoreApplication.translate("MainWindow", u"Scorll", None))
        self.app_state_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
    # retranslateUi

