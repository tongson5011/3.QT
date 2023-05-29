import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title.
        self.setWindowTitle("My Notepad")

        # Create a text editor widget.
        self.text_editor = QPlainTextEdit()

        # Create a status bar.
        self.status_bar = QStatusBar()

        # Set the central widget of the window to the text editor widget.
        self.setCentralWidget(self.text_editor)

        # Add the status bar to the window.
        self.setStatusBar(self.status_bar)

        ############################################
        # Create a new action to open a file.
        self.open_file_action = QAction("Open File", self)
        self.open_file_action.triggered.connect(self.open_file)

        # Create a new action to create a new file.
        self.new_file_action = QAction("New File", self)
        self.new_file_action.triggered.connect(self.new_file)

        self.find_action = QAction("Find", self)
        self.find_action.triggered.connect(self.handleFindRequest)

        # # Create a new action to open a file in an external app.
        # self.open_file_in_app_action = QAction("Open File in App", self)
        # self.open_file_in_app_action.triggered.connect(self.open_file_in_app)

        # Add the actions to the menu bar.
        self.menu_bar = QMenuBar(self)
        self.menu_bar.addAction(self.open_file_action)
        self.menu_bar.addAction(self.new_file_action)
        self.menu_bar.addAction(self.find_action)

        # self.menu_bar.addAction(self.open_file_in_app_action)

    def new_file(self):
        # Clear the text editor widget.
        self.text_editor.clear()

    def save_file(self):
        # Get the current text from the text editor widget.
        text = self.text_editor.toPlainText()

        # Prompt the user for a file name.
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt)")

        # If the user cancels, do nothing.
        if not file_name:
            return

        # Write the text to the file.
        with open(file_name, "w") as f:
            f.write(text)

    def close_file(self):
        # Get the current text from the text editor widget.
        text = self.text_editor.toPlainText()

        # Prompt the user if they want to save the file.
        if not QMessageBox.question(self, "Save File", "Do you want to save the file?", QMessageBox.Save | QMessageBox.Discard):
            return

        # If the user wants to save the file, call the save_file() method.
        if QMessageBox.Save == QMessageBox.clickedButton(self):
            self.save_file()

        # Close the window.
        self.close()

    def open_file(self):
        # Prompt the user for a file name.
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt)")

        # If the user cancels, do nothing.
        if not file_name:
            return

        # Read the text from the file.
        with open(file_name, "r") as f:
            text = f.read()

        # Set the text in the text editor widget.
        self.text_editor.setPlainText(text)

    def about(self):
        QMessageBox.about(self, "About My Notepad",
                          "My Notepad is a simple text editor written in Python using PyQt.")

    def handleFindRequest(self):
        # Get the text that the user wants to find
        findText = QInputDialog.getText(self, "Find", "Find what?")

        # If the user entered a text, then search for it in the document
        if findText:
            self.text_editor.document().find(findText)


def main():
    app = QApplication([])
    # Create the main window object.
    main_window = MainWindow()

    # Show the main window.
    main_window.show()

    # Start the event loop.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
