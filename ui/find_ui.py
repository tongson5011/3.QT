# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Find(object):
    def setupUi(self, Find):
        if not Find.objectName():
            Find.setObjectName(u"Find")
        Find.resize(400, 46)
        self.verticalLayout = QVBoxLayout(Find)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Find)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.find_input = QLineEdit(self.frame)
        self.find_input.setObjectName(u"find_input")

        self.horizontalLayout.addWidget(self.find_input)

        self.find_up = QPushButton(self.frame)
        self.find_up.setObjectName(u"find_up")
        self.find_up.setMinimumSize(QSize(40, 0))
        self.find_up.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.find_up)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 0))
        self.pushButton_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Find)

        QMetaObject.connectSlotsByName(Find)
    # setupUi

    def retranslateUi(self, Find):
        Find.setWindowTitle(QCoreApplication.translate("Find", u"Form", None))
        self.find_up.setText(QCoreApplication.translate("Find", u"U", None))
        self.pushButton_2.setText(QCoreApplication.translate("Find", u"D", None))
    # retranslateUi

