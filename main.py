# import PySide6
from qframelesswindow import FramelessMainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextEdit
from PySide6.QtCore import Qt, QThreadPool
from PySide6.QtGui import QFont, QTextCharFormat, QTextCursor, QColor, QCursor
from load_config import Worker
# import ui module
from ui.menu_ui import Menu_ui
from ui.Edit_ui import Edit_UI
from ui.main_app_ui import Ui_MainWindow
# import extenal module
import json
import os
import sys
import time
# import internal module
from crawl_story import Story, validateURL
from Translater import Translate
from charaters import charaters_name
from splitChinaText import find_dict
from datetime import datetime

# config os path
PATH = os.path.dirname(os.path.abspath(__file__))
userData = os.path.join(PATH, 'userData')
userData_temp = os.path.join(userData, 'temp')
maximize_app = os.path.join(PATH, 'maximize_app.css')
normalize_app = os.path.join(PATH, 'normalize_app.css')
app_logo = os.path.join(PATH, 'assects\icon\logo.png')

with open(normalize_app, 'r') as f:
    app_style = f.read()


class MainWindow(FramelessMainWindow, Ui_MainWindow):
    app_windows = []

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.main_app.raise_()
        # config global app
        MainWindow.app_windows.append(self)
        self.header_frame.mousePressEvent = self.handleMoveApp
        # add CSS
        self.setStyleSheet(app_style)
        # config widget
        self.menu_ui = Menu_ui()
        self.edit_ui = Edit_UI()
        self.m_story = Story()
        self.trans = Translate(charaters=charaters_name)
        self.theadpool = QThreadPool()
        # ======================================
        # ==========config variable=============
        # ======================================
        self.app_path_file = None
        self.app_config = None
        self.isTranslateAll = False
        self.story_input = None
        #
        self.maxScroll_VI = 0
        # ======================================
        # ======================================
        # ======================================
        # add widget
        self.app_menu_layouts.addWidget(self.menu_ui)
        self.content_main_layouts.addWidget(self.edit_ui)
        # ==================================================================
        # ==================================================================
        # hidden app message
        self.app_state_message.stateChanged.connect(self.handleHidenMessage)
        # multi scroll
        self.edit_ui.edit_vi.verticalScrollBar().valueChanged.connect(self.handleScroll)
        # change cursor position
        self.edit_ui.edit_vi.cursorPositionChanged.connect(
            self.handleHightLightText)
        # ===================================================================
        # ===================================================================
        # close, maximize, minimize app
        self.app_close.clicked.connect(lambda: self.close())
        self.app_minimize.clicked.connect(lambda: self.showMinimized())
        self.app_maximize.clicked.connect(self.handleMaximize)
        # ==============================================
        # ==========handle menu bar actions=============
        # ==============================================
        # menu new
        self.menu_ui.new_action.triggered.connect(self.handleNewApp)
        # menu open
        self.menu_ui.open_action.triggered.connect(self.handleOpenApp)
        # menu save
        self.menu_ui.save_action.triggered.connect(self.handleSaveApp)
        # menu save as
        self.menu_ui.save_as_action.triggered.connect(self.handleSaveAsApp)
        # menu export
        self.menu_ui.export_All.triggered.connect(self.handleExportAll)
        self.menu_ui.export_VI.triggered.connect(self.handleExportVI)

        # ==============================================
        # ==============================================
        # ==============================================
        # search story
        self.search_story_push.clicked.connect(self.handleScrawlStory)
        # next story
        self.search_next_chapter.clicked.connect(
            lambda: self.handleNextPrevChapter(chapter_data='next_chapter'))
        self.search_prev_chapter.clicked.connect(
            lambda: self.handleNextPrevChapter(chapter_data='prev_chapter'))
        # translate story
        self.translate_push.clicked.connect(self.handleTranslation)

    # ==============================================
    # ===========Translate sections====================
    # ==============================================
    # Translate all
    def handleTranslation(self):
        translate_input = self.translate_options.currentText()
        translate_options = ['Translate All', 'Translate Han Viet',
                             'Translate VI', 'Translate EN', 'Translate VietPhrase', 'Translate EN-VI']
        trans_data = self.edit_ui.edit_cn.toPlainText()
        trans_en_data = self.edit_ui.edit_en.toPlainText()
        index_option = translate_options.index(translate_input)
        # EN-VI
        if index_option == 5:
            if not trans_en_data:
                self.app_message.appendPlainText(
                    'EN data is emtry. Please insert EN data')
            else:
                self.app_message.appendPlainText('Starting translation....')
                trans_en_vi_worker = Worker(
                    lambda data=trans_en_data: self.trans.translateENtoVI(data))
                trans_en_vi_worker.signals.result.connect(
                    self.handleLoadStoryData)
                self.theadpool.start(trans_en_vi_worker)
        else:
            if not trans_data:
                self.app_message.appendPlainText(
                    'CN data is emtry. Please insert cn data')
            else:
                self.app_message.appendPlainText('Starting translation....')
                # all
                if index_option == 0:
                    # check translate all
                    self.isTranslateAll = True
                    # add worker
                    trans_hv_worker = Worker(
                        lambda hv_data=trans_data: self.trans.translateHanViet(text=hv_data))
                    trans_vi_worker = Worker(
                        lambda vi_data=trans_data: self.trans.translateCNtoVI(cn_vi_text=vi_data))
                    trans_en_worker = Worker(
                        lambda en_data=trans_data: self.trans.translateCNtoEN(cn_en_text=en_data))
                    trans_vf_worker = Worker(
                        lambda vf_data=trans_data: self.trans.translateVietPhrase(text=vf_data))
                    # load result to ui
                    trans_hv_worker.signals.result.connect(
                        self.handleLoadStoryData)
                    trans_vf_worker.signals.result.connect(
                        self.handleLoadStoryData)
                    trans_vi_worker.signals.result.connect(
                        self.handleLoadStoryData)
                    trans_en_worker.signals.result.connect(
                        self.handleLoadStoryData)

                    # run worker
                    self.theadpool.start(trans_hv_worker)
                    self.theadpool.start(trans_vf_worker)
                    self.theadpool.start(trans_vi_worker)
                    self.theadpool.start(trans_en_worker)

                # han viet
                elif index_option == 1:
                    trans_hv_worker = Worker(
                        lambda data=trans_data: self.trans.translateHanViet(data))
                    trans_hv_worker.signals.result.connect(
                        self.handleLoadStoryData)
                    self.theadpool.start(trans_hv_worker)
                # VI
                elif index_option == 2:
                    trans_vi_worker = Worker(
                        lambda data=trans_data: self.trans.translateCNtoVI(data))
                    trans_vi_worker.signals.result.connect(
                        self.handleLoadStoryData)
                    self.theadpool.start(trans_vi_worker)
                # EN
                elif index_option == 3:
                    trans_en_worker = Worker(
                        lambda data=trans_data: self.trans.translateCNtoEN(data))
                    trans_en_worker.signals.result.connect(
                        self.handleLoadStoryData)
                    self.theadpool.start(trans_en_worker)
                # VietPhrase
                elif index_option == 4:
                    trans_vf_worker = Worker(
                        lambda data=trans_data: self.trans.translateVietPhrase(data))
                    trans_vf_worker.signals.result.connect(
                        self.handleLoadStoryData)
                    self.theadpool.start(trans_vf_worker)
                # EN-VI

    # ==============================================
    # ==============================================
    # ==============================================

    # ==============================================
    # ===========Search sections====================
    # ==============================================
    # check input
    def handleCheckStoryInput(self, story_url=''):
        if not story_url:
            story_url = self.search_story_input.text()
        if not story_url:
            self.app_message.appendPlainText('Url is emtry')
            return False
        elif not validateURL(story_url):
            self.app_message.appendPlainText('Url is not validate')
            return False
        else:
            return story_url

    # load data to Edit UI
    def handleLoadStoryData(self, story_data):

        if story_data['status'] == 'Faild':
            self.app_message.appendPlainText(story_data['message'])
        else:
            self.app_message.appendPlainText('Start load data to UI')
            if story_data['data'] == 'CN':
                self.edit_ui.edit_cn.setPlainText(story_data['result'])
            elif story_data['data'] == 'hanViet':
                self.edit_ui.edit_HanViet.setPlainText(story_data['result'])
            elif story_data['data'] == 'VI':
                self.edit_ui.edit_vi.setPlainText(story_data['result'])
            elif story_data['data'] == 'EN':
                self.edit_ui.edit_en.setPlainText(story_data['result'])
                if self.isTranslateAll == True:
                    trans_en_vi_worker = Worker(
                        lambda data=story_data['result']: self.trans.translateENtoVI(data))
                    trans_en_vi_worker.signals.result.connect(
                        self.handleLoadStoryData)
                    self.theadpool.start(trans_en_vi_worker)
                    self.isTranslateAll = False
            elif story_data['data'] == 'vietPhrase':
                self.edit_ui.edit_vietPhrase.setPlainText(story_data['result'])
            elif story_data['data'] == 'EN-VI':
                self.edit_ui.edit_en_vi.setPlainText(story_data['result'])
            self.app_message.appendPlainText('Load done...')
        self.search_story_push.setDisabled(False)

    # run crawl sotry
    def handleScrawlStory(self, chapter_url=''):
        # save current data
        self.handleSaveTempFile()
        #
        self.search_story_push.setDisabled(True)
        if chapter_url:
            self.story_input = self.handleCheckStoryInput(
                story_url=chapter_url)
        else:
            self.story_input = self.handleCheckStoryInput()
        if self.story_input:
            self.search_story_input.setText(self.story_input)
            self.app_message.appendPlainText(
                'Stating crawl story data. please Wait a few minute')
            self.m_story = Story(url=self.story_input)
            story_worker = Worker(self.m_story.scrawlChapterDATA)
            story_worker.signals.result.connect(self.handleLoadStoryData)
            self.theadpool.start(story_worker)
        else:
            self.search_story_push.setDisabled(False)

    # handle next, prev chapter
    def handleNextPrevChapter(self, chapter_data):
        self.handleSaveTempFile()
        self.story_input = self.search_story_input.text()
        if not self.story_input:
            self.app_message.appendPlainText(
                'URL is emtry, please insert chapter url first')
        else:
            self.m_story = Story(url=self.story_input)
            if chapter_data == 'prev_chapter':
                prev_story_worker = Worker(self.m_story.prevChapter)
                prev_story_worker.signals.result.connect(
                    lambda data: self.handleScrawlStory(chapter_url=data['chapter_url']) if data['status'] == 'Success' else self.app_message.appendPlainText(data['message']))
                self.theadpool.start(prev_story_worker)
            elif chapter_data == 'next_chapter':
                next_story_worker = Worker(self.m_story.nextChapter)
                next_story_worker.signals.result.connect(
                    lambda data: self.handleScrawlStory(chapter_url=data['chapter_url']) if data['status'] == 'Success' else self.app_message.appendPlainText(data['message']))
                self.theadpool.start(next_story_worker)

    # ==============================================
    # ==============================================
    # ==============================================

    # ==============================================
    # ===========File actions=======================
    # ==============================================

    # handle save app
    def handleSaveApp(self):
        if not self.app_path_file:
            self.handleSaveAsApp()
        else:
            self.saveAppConfig()
            with open(self.app_path_file, 'w', encoding='utf-8') as f:
                json.dump(self.app_config, f)
            self.app_message.appendPlainText('App was save data')

    # handle save as app
    def handleSaveAsApp(self):
        self.saveAppConfig()
        fileName, _ = QFileDialog.getSaveFileName(
            self, 'Save File', '', 'QT Translate (*.st)')
        print(fileName)
        if fileName:
            self.app_path_file = fileName
            with open(fileName, 'w', encoding='utf-8') as f:
                json.dump(self.app_config, f)
            self.app_message.appendPlainText('App was save data')

    # handle open app
    def handleOpenApp(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, 'Open File', '', 'Text File (*.st)')
        if fileName:
            self.app_path_file = fileName
            with open(fileName, 'r', encoding='utf-8') as f:
                self.app_data = json.load(f)
            self.loadAppConfig()
            self.app_message.appendPlainText('App was load data')

    # save config
    def saveAppConfig(self):
        # app config
        is_message = self.app_state_message.isChecked()
        chapter_url = self.search_story_input.text()
        is_HightLight = self.app_hightLight.isChecked()
        # ==========================
        # cn data
        cn_data = self.edit_ui.edit_cn.toPlainText()
        cn_fontSize = self.edit_ui.edit_cn.font().pointSize()
        cn_fontFamily = self.edit_ui.edit_cn.font().family()

        # Han Viet data
        hanViet_data = self.edit_ui.edit_HanViet.toPlainText()
        hanViet_fontSize = self.edit_ui.edit_HanViet.font().pointSize()
        hanViet_fontFamily = self.edit_ui.edit_HanViet.font().family()

        # vi data
        vi_data = self.edit_ui.edit_vi.toPlainText()
        vi_fontSize = self.edit_ui.edit_vi.font().pointSize()
        vi_fontFamily = self.edit_ui.edit_vi.font().family()

        # en data
        en_data = self.edit_ui.edit_en.toPlainText()
        en_fontSize = self.edit_ui.edit_en.font().pointSize()
        en_fontFamily = self.edit_ui.edit_en.font().family()

        # vietPhrase data
        vietPhrase_data = self.edit_ui.edit_vietPhrase.toPlainText()
        vietPhrase_fontSize = self.edit_ui.edit_vietPhrase.font().pointSize()
        vietPhrase_fontFamily = self.edit_ui.edit_vietPhrase.font().family()

        # vietPhrase data
        en_vi_data = self.edit_ui.edit_en_vi.toPlainText()
        en_vi_fontSize = self.edit_ui.edit_en_vi.font().pointSize()
        en_vi_fontFamily = self.edit_ui.edit_en_vi.font().family()

        self.app_config = {
            'app_cls': {'is_message': is_message, 'is_HightLight': is_HightLight, 'chapter_url': chapter_url},
            'app_data':
                [
                    {
                        'id': 1,
                        'name': 'CN',
                        'data': cn_data,
                        'font_size': cn_fontSize,
                        'font_family': cn_fontFamily
                    },
                    {
                        'id': 2,
                        'name': 'HanViet',
                        'data': hanViet_data,
                        'font_size': hanViet_fontSize,
                        'font_family': hanViet_fontFamily
                    },
                    {
                        'id': 3,
                        'name': 'VI',
                        'data': vi_data,
                        'font_size': vi_fontSize,
                        'font_family': vi_fontFamily
                    },
                    {
                        'id': 4,
                        'name': 'EN',
                        'data': en_data,
                        'font_size': en_fontSize,
                        'font_family': en_fontFamily
                    },
                    {
                        'id': 5,
                        'name': 'VietPhrase',
                        'data': vietPhrase_data,
                        'font_size': vietPhrase_fontSize,
                        'font_family': vietPhrase_fontFamily
                    },
                    {
                        'id': 6,
                        'name': 'EN_VI',
                        'data': en_vi_data,
                        'font_size': en_vi_fontSize,
                        'font_family': en_vi_fontFamily
                    }
            ]
        }

    # load config
    def loadAppConfig(self):
        is_message = self.app_data['app_cls']['is_message']
        is_HightLight = self.app_data['app_cls']['is_HightLight'] if 'is_HightLight' in self.app_data['app_cls'] else False
        chapter_url = self.app_data['app_cls']['chapter_url'] if 'chapter_url' in self.app_data['app_cls'] else ''
        # ==========================
        current_data = self.app_data['app_data']
        # cn data
        cn_data = current_data[0]['data']
        cn_fontSize = current_data[0]['font_size']
        cn_fontFamily = current_data[0]['font_family']

        # Han Viet data
        hanViet_data = current_data[1]['data']
        hanViet_fontSize = current_data[1]['font_size']
        hanViet_fontFamily = current_data[1]['font_family']

        # vi data
        vi_data = current_data[2]['data']
        vi_fontSize = current_data[2]['font_size']
        vi_fontFamily = current_data[2]['font_family']

        # en data
        en_data = current_data[3]['data']
        en_fontSize = current_data[3]['font_size']
        en_fontFamily = current_data[3]['font_family']

        # vietPhrase data
        vietPhrase_data = current_data[4]['data']
        vietPhrase_fontSize = current_data[4]['font_size']
        vietPhrase_fontFamily = current_data[4]['font_family']

        # vietPhrase data
        en_vi_data = current_data[5]['data']
        en_vi_fontSize = current_data[5]['font_size']
        en_vi_fontFamily = current_data[5]['font_family']

        # load data to app

        cn_font = QFont(cn_fontFamily, cn_fontSize)
        hanViet_font = QFont(hanViet_fontFamily, hanViet_fontSize)
        vietPhrase_font = QFont(vietPhrase_fontFamily, vietPhrase_fontSize)
        vi_font = QFont(vi_fontFamily, vi_fontSize)
        en_font = QFont(en_fontFamily, en_fontSize)
        en_vi_font = QFont(en_vi_fontFamily, en_vi_fontSize)
        # ============================================================
        # load app config
        self.app_state_message.setChecked(is_message)
        self.app_hightLight.setChecked(is_HightLight)
        self.search_story_input.setText(chapter_url)
        # ====================================
        # load cn data
        self.edit_ui.edit_cn.setPlainText(cn_data)
        self.edit_ui.edit_cn.setCurrentFont(cn_font)
        # load han viet data
        self.edit_ui.edit_HanViet.setPlainText(hanViet_data)
        self.edit_ui.edit_cn.setCurrentFont(hanViet_font)
        # load vi data
        self.edit_ui.edit_vi.setPlainText(vi_data)
        self.edit_ui.edit_vi.setCurrentFont(vi_font)
        # load en data
        self.edit_ui.edit_en.setPlainText(en_data)
        self.edit_ui.edit_en.setCurrentFont(en_font)
        # load viet Phrase data
        self.edit_ui.edit_vietPhrase.setPlainText(vietPhrase_data)
        self.edit_ui.edit_vietPhrase.setCurrentFont(vietPhrase_font)
        # load en_vi data
        self.edit_ui.edit_en_vi.setPlainText(en_vi_data)
        self.edit_ui.edit_en_vi.setCurrentFont(en_vi_font)
        # ===========================================
        # ==============================================
        # =============================================
        # ==================================================

    def handleExportAll(self):
        pass

    def handleExportVI(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, 'export File', '', 'Vi Text (*.txt)')
        vi_data = self.edit_ui.edit_vi.toPlainText()
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(vi_data)

    def handleSaveTempFile(self):
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S-%f")
        file_temp = os.path.join(userData_temp, f'{dt_string}.st')
        print(file_temp)
        with open(file_temp, 'w', encoding='utf-8') as f:
            json.dump(self.app_config, f)

    # ==================================================
    # =============== handle app config ================
    # ==================================================
    # hidden message

    def handleHidenMessage(self):
        if not self.app_state_message.isChecked():
            self.app_message.hide()
            self.footer_frame.setMinimumHeight(4)
            self.footer_frame.setMaximumHeight(4)

        else:
            self.footer_frame.setMinimumHeight(80)
            self.footer_frame.setMaximumHeight(80)
            self.app_message.show()

    # multi scroll
    def handleScroll(self, event):
        # scroll is checked
        if self.app_scroll.isChecked():
            self.maxScroll_VI = self.edit_ui.edit_vi.verticalScrollBar().maximum()
            perScroll = event / self.maxScroll_VI
            # set variable
            verticalScroll_CN = self.edit_ui.edit_cn.verticalScrollBar()
            verticalScroll_EN = self.edit_ui.edit_en.verticalScrollBar()
            verticalScroll_EN_VI = self.edit_ui.edit_en_vi.verticalScrollBar()
            verticalScroll_vietPhrase = self.edit_ui.edit_vietPhrase.verticalScrollBar()
            verticalScroll_hanViet = self.edit_ui.edit_HanViet.verticalScrollBar()
            # set value
            verticalScroll_CN.setValue(perScroll * verticalScroll_CN.maximum())
            verticalScroll_EN.setValue(perScroll * verticalScroll_EN.maximum())
            verticalScroll_EN_VI.setValue(
                perScroll * verticalScroll_EN_VI.maximum())
            verticalScroll_vietPhrase.setValue(
                perScroll * verticalScroll_vietPhrase.maximum())
            verticalScroll_hanViet.setValue(
                perScroll * verticalScroll_hanViet.maximum())

    # handle hightlight another text
    def handleHightLightCurrentText(self, target, line_number, isScroll=True):
        document = target.document()
        block = document.findBlockByLineNumber(line_number)
        start_position = block.position()
        end_position = start_position + block.length() - 1
        highlight_format = QTextCharFormat()
        highlight_format.setBackground(QColor(255, 255, 0))
        extra_selection = QTextEdit.ExtraSelection()
        extra_selection.format = highlight_format
        extra_selection.cursor = QTextCursor(document)
        extra_selection.cursor.setPosition(start_position)
        extra_selection.cursor.setPosition(
            end_position, QTextCursor.KeepAnchor)
        target.setExtraSelections([extra_selection])
        if isScroll:
            scroll_bar = target.verticalScrollBar()
            cursor_rect = target.cursorRect(extra_selection.cursor)
            viewport_height = target.viewport().height()
            # print(target)
            scroll_bar.setValue(scroll_bar.value() +
                                cursor_rect.top() - viewport_height / 2)

    # hightlight text
    def handleHightLightText(self):
        if self.app_hightLight.isChecked():
            cursor = self.edit_ui.edit_vi.textCursor()
            line_number = cursor.blockNumber() or 0
            current_block = self.edit_ui.edit_cn.document().findBlockByLineNumber(line_number)
            china_text = current_block.text()

            # self.edit_ui.edit_Properties.clear()
            find_dict_worker = Worker(
                lambda: find_dict(default_text=china_text))
            # find_dict_worker.signals.result.connect(
            #     lambda result_data: self.edit_ui.edit_Properties.append(' '.join(result_data)))
            find_dict_worker.signals.result.connect(
                lambda result: self.handleAddChinaDict(china_text, result))
            self.theadpool.start(find_dict_worker)
            # print(result)
            # self.edit_ui.edit_Properties.append()
            # hightlight VI
            self.handleHightLightCurrentText(
                target=self.edit_ui.edit_vi, line_number=line_number, isScroll=False)
            # hightlight CN
            self.handleHightLightCurrentText(
                target=self.edit_ui.edit_cn, line_number=line_number, isScroll=True)
            # hightlight Han Viet
            self.handleHightLightCurrentText(
                target=self.edit_ui.edit_HanViet, line_number=line_number, isScroll=True)
            # hightlight EN
            self.handleHightLightCurrentText(
                target=self.edit_ui.edit_en, line_number=line_number, isScroll=True)
            # hightlight VietPhrase
            self.handleHightLightCurrentText(
                target=self.edit_ui.edit_vietPhrase, line_number=line_number, isScroll=True)
            # hightlight EN-VI
            self.handleHightLightCurrentText(
                target=self.edit_ui.edit_en_vi, line_number=line_number, isScroll=True)

        # highlight_format = QTextCharFormat()
        # highlight_format.setBackground(QColor(255, 255, 0))
        # extra_selection = QTextEdit.ExtraSelection()
        # extra_selection.format = highlight_format
        # extra_selection.cursor = QTextCursor(self.edit_ui.edit_vi.document())
        # extra_selection.cursor.setPosition(start_l)
        # extra_selection.cursor.setPosition(
        #     end_l, QTextCursor.KeepAnchor)
        # self.edit_ui.edit_vi.setExtraSelections([extra_selection])
    # add china dictionary
    def handleAddChinaDict(self, china_text, list_datas):
        result = ''''''
        print(list_datas)
        for data in list_datas:
            if not result:
                result = result + f'''{china_text} \n'''
            key = data[0]
            value = data[1]
            result = result + f'''-{key}: {value} \n'''
        self.edit_ui.edit_Properties.clear()
        self.edit_ui.edit_Properties.append(result)
    # =============================================
    # =============================================

    # handle resize event

    def resizeEvent(self, event):
        # print(self.maximumSize())
        if event.size().width() >= 1550:
            self.main_app.setContentsMargins(0, 0, 14, 14)
        else:
            self.main_app.setContentsMargins(0, 0, 0, 0)
        # print(self.is)
        return QMainWindow.resizeEvent(self, event)
    # handle Maximize app

    def handleMaximize(self):
        if not self.isMaximized():
            self.showMaximized()
        else:
            self.showNormal()

    # move app in window
    def handleMoveApp(self, event):
        if not self.isMaximized() and event.button() == Qt.MouseButton.LeftButton:
            window = self.window().windowHandle()
            window.startSystemMove()

        elif event.type() == 4:
            self.showNormal()
        return super().mousePressEvent(event)

    # ==================================================
    # ==========Handle create new app =================+
    # ==================================================
    # open app in a new window

    def handleNewApp(self):
        new_app = QApplication.instance()

        if new_app is None:
            new_app = QApplication(sys.argv)
        new_window = MainWindow()
        old_window = self.geometry()
        if old_window.y() - 10 > 50:
            new_y = old_window.y() - 50
        else:
            new_y = old_window.y() + 10
        if old_window.x() + 100 < 700:
            mew_x = old_window.x() + 100
        else:
            mew_x = old_window.x() + 100
        new_window.setGeometry(
            mew_x, new_y, old_window.width(), old_window.height())
        # new_window.move(self.geometry().bottomLeft() +
        #                 new_window.rect().bottomLeft())
        new_window.show()
        # new_app.exec()

    # close event
    def closeEvent(self, event):
        # Remove this window from the list of windows
        MainWindow.app_windows.remove(self)
        event.accept()
    # ==================================================
    # ==================================================
    # ==================================================


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
