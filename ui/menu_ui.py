# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'menu.ui'
##
# Created by: Qt User Interface Compiler version 6.4.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QMainWindow, QMenu)


class Menu_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()
        # create menu
        file_menu = QMenu("File", self)
        export_menu = QMenu("Export File", self)
        edit_menu = QMenu("Edit", self)
        window_menu = QMenu("Window", self)
        view_menu = QMenu("View", self)
        help_menu = QMenu("Help", self)
        # add menu
        menubar.addMenu(file_menu)
        menubar.addMenu(edit_menu)
        menubar.addMenu(window_menu)
        menubar.addMenu(view_menu)
        menubar.addMenu(help_menu)
        # create action
        # =======================
        self.new_action = QAction("New", self)
        self.open_action = QAction("Open", self)
        self.save_action = QAction("Save", self)
        self.save_as_action = QAction("Save As", self)
        #
        self.export_All = QAction("Export All", self)
        self.export_VI = QAction("Export VI", self)
        self.export_CN = QAction("Export CN", self)
        self.export_EN = QAction("Export EN", self)
        self.export_VietPhrase = QAction("Export VietPhrase", self)
        self.export_Han_Viet = QAction("Export Han Viet", self)

        self.export_EN_VI = QAction("Export EN-VI", self)
        #
        self.exit_action = QAction("Exit", self)
        # ===============================================
        self.edit_action = QAction("Edit", self)
        # ======================================
        self.layout_action = QAction('Layout', self)
        # add toolbar action
        self.paste_action = QAction('Paste', self)
        # create shortcut
        self.new_action.setShortcut('Ctrl+N')
        self.open_action.setShortcut('Ctrl+O')

        self.save_action.setShortcut('Ctrl+S')
        self.save_as_action.setShortcut('Ctrl+Shift+S')
        self.export_All.setShortcut('Ctrl+Shift+A')
        self.export_VI.setShortcut('Ctrl+E')
        self.export_EN_VI.setShortcut('Ctrl+W')

        # ===================================
        self.message_action = QAction('Message', self)
        self.message_action.setCheckable(True)
        self.message_action.setChecked(True)
        # ==========================================
        self.about_action = QAction("About", self)
        # add actions
        file_menu.addActions(
            [self.new_action, self.open_action, file_menu.addSeparator(), self.save_action, self.save_as_action, file_menu.addSeparator(), file_menu.addMenu(export_menu), self.exit_action])
        export_menu.addActions(
            [self.export_All, self.export_VI, self.export_CN, self.export_EN, self.export_EN_VI, self.export_VietPhrase, self.export_Han_Viet])
        edit_menu.addActions([self.edit_action])
        view_menu.addActions([self.message_action])
        window_menu.addActions([self.layout_action])
        help_menu.addActions([self.about_action])

        # css
        self.setStyleSheet('''
        QMenuBar {
            background-color: #73c264;
            color: #000;
            border: none;
            font-size: 10pt;
            }
        QMenuBar::item::selected {
            background-color: #e8e8e8;
            border-radius: 6px;
        }''')
