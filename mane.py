import sys

from PyQt5.QtWidgets import *
from  PyQt5 .QtGui import *

class BSWorld(QMainWindow):
    def __init__(self):
        super(BSWorld, self).__init__()
        self.editor = QTextEdit()
        self.editor.setFontPointSize(20)
        self.setCentralWidget(self.editor)
        self.font_size_box = QSpinBox
        self.showMaximized()
        self.setWindowTitle(" my shomriddho's world")
        self.create_tool_bar()


    def create_tool_bar(self) :
        tool_bar = QToolBar()

        undo_action = QAction(QIcon('undo-5.png'),'undo', self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        redo_action = QAction(QIcon('redo-5.png'),'redo', self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)



        self.addToolBar(tool_bar)







app = QApplication(sys.argv)
window = BSWorld()
window.show()
sys.exit(app.exec_())