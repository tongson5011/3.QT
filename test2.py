# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'replaceJPMOyz.ui'
##
# Created by: Qt User Interface Compiler version 6.4.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_Replace(object):
    def setupUi(self, Replace):
        if not Replace.objectName():
            Replace.setObjectName(u"Replace")
        Replace.resize(355, 68)
        Replace.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Replace)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Replace)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.replace_input = QLineEdit(self.frame)
        self.replace_input.setObjectName(u"replace_input")

        self.verticalLayout.addWidget(self.replace_input)

        self.replace_output = QLineEdit(self.frame)
        self.replace_output.setObjectName(u"replace_output")

        self.verticalLayout.addWidget(self.replace_output)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Replace)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Replace)

        QMetaObject.connectSlotsByName(Replace)
    # setupUi

    def retranslateUi(self, Replace):
        Replace.setWindowTitle(
            QCoreApplication.translate("Replace", u"Form", None))
        self.pushButton.setText(
            QCoreApplication.translate("Replace", u"Replace", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "Replace", u"Replace All", None))
    # retranslateUi
