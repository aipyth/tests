import random, pdb
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QPushButton, QLabel, QProgressBar, QLayout,\
QHBoxLayout, QVBoxLayout, QSizePolicy, QGroupBox
from core import *

class Window(QtWidgets.QWidget):
    def __init__(self, test, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.test = test
        self.counter = 0

        desktop = QtWidgets.QApplication.desktop()
        size_of_window = QtCore.QSize(desktop.width() - (desktop.width()*0.15625),
                                    desktop.height() - (desktop.height()*0.27778))
        start_point = QtCore.QPoint((desktop.width() - size_of_window.width()) // 2 ,
                                    (desktop.height() - size_of_window.height()) // 2)
        self.resize(size_of_window)
        self.move(start_point)
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                            QtGui.QColor('#dad8d7'))
        pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
                            QtGui.QColor('#dad8d7'))
        self.setPalette(pal)

        self.TestNameLabel = QLabel(self.test.get_name())
        self.TestNameLabel.setWordWrap(True)
        TestNameLabelPolicy = QSizePolicy(QSizePolicy.MinimumExpanding,
                                        QSizePolicy.MinimumExpanding)
        self.TestNameLabel.setSizePolicy(TestNameLabelPolicy)
        self.TestNameLabel.setStyleSheet(""" QLabel {
        border: 4px solid #1e3b63;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        font-family: Impact;
        font-size: 28px;
        }""")
        self.QuestionLabel = QLabel(self.test.get_question())
        self.QuestionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.QuestionLabel.setWordWrap(True)
        self.QuestionLabel.setMinimumWidth(500)
        QuestionLabelPolicy = QSizePolicy(QSizePolicy.Expanding,
                                        QSizePolicy.Expanding)
        self.QuestionLabel.setSizePolicy(TestNameLabelPolicy)
        self.QuestionLabel.setStyleSheet(""" QLabel {
        font-family: Arial;
        font-size: 25px;
        }""")

        self.answers = self.test.get_answers()
        self.FirstAnswerButton = QPushButton(self.answers[0])
        self.FirstAnswerButton.clicked.connect(self.f_handler_push_button)
        self.SecondAnswerButton = QPushButton(self.answers[1])
        self.SecondAnswerButton.clicked.connect(self.handler_push_button)
        self.ThirdAnswerButton = QPushButton(self.answers[2])
        self.ThirdAnswerButton.clicked.connect(self.handler_push_button)
        self.FourthAnswerButton = QPushButton(self.answers[3])
        self.FourthAnswerButton.clicked.connect(self.handler_push_button)
        # self.FirstAnswerButton = QPushButton(self.answers[0])
        # self.FirstAnswerButton.clicked.connect(self.f_simple_handler)
        # self.SecondAnswerButton = QPushButton(self.answers[1])
        # self.SecondAnswerButton.clicked.connect(self.simple_handler_sec)
        # self.ThirdAnswerButton = QPushButton(self.answers[2])
        # self.ThirdAnswerButton.clicked.connect(self.simple_handler_thi)
        # self.FourthAnswerButton = QPushButton(self.answers[3])
        # self.FourthAnswerButton.clicked.connect(self.simple_handler_fou)
        ButtonSizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.ButtonsList = [self.FirstAnswerButton, self.SecondAnswerButton,
        self.ThirdAnswerButton, self.FourthAnswerButton]
        for item in self.ButtonsList:
            item.setSizePolicy(ButtonSizePolicy)
            item.setFlat(True)
            item.setStyleSheet(""" QPushButton {
            color: #363636;
            font-size: 18px;
            font-family: Arial, Verdana, monospace;
            border: 7px solid #1e3b63;
            border-top-width: 0px;
            border-left-width: 0px;
            border-right-width: 0px;
            background: #c8c8c8;
            }""")


        random.shuffle(self.ButtonsList)
        self.AnswerGridLayout = QtWidgets.QGridLayout()
        for i, item in enumerate(self.ButtonsList):
            if i == 0:
                self.AnswerGridLayout.addWidget(item, 0, 0)
            if i == 1:
                self.AnswerGridLayout.addWidget(item, 0, 2)
            if i == 2:
                self.AnswerGridLayout.addWidget(item, 2, 0)
            if i == 3:
                self.AnswerGridLayout.addWidget(item, 2, 2)

        self.AnswGroupBox = QGroupBox('Choose one variant')
        self.AnswGroupBox.setLayout(self.AnswerGridLayout)
        self.AnswGroupBox.setFlat(True)
        self.AnswGroupBox.setStyleSheet(""" QGroupBox {
        font-size: 18px;
        }""")

        self.MainLayout = QVBoxLayout()
        self.MainLayout.addWidget(self.TestNameLabel, alignment=QtCore.Qt.AlignTop|QtCore.Qt.AlignCenter)
        self.MainLayout.addWidget(self.QuestionLabel, alignment=QtCore.Qt.AlignHCenter)
        self.MainLayout.addWidget(self.AnswGroupBox)
        self.setLayout(self.MainLayout)

    def f_simple_handler(self):
        self.FirstAnswerButton.setStyleSheet(""" QPushButton {
        color: #363636;
        font-size: 18px;
        font-family: Arial, Verdana, monospace;
        border: 7px solid #1e3b63;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        background: #00cf08;
        }""")

    def simple_handler_sec(self):
        self.FirstAnswerButton.setStyleSheet(""" QPushButton {
        color: #363636;
        font-size: 18px;
        font-family: Arial, Verdana, monospace;
        border: 7px solid #1e3b63;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        background: #00cf08;
        }""")
        self.SecondAnswerButton.setStyleSheet(""" QPushButton {
        color: #e2e2e2;
        font-size: 18px;
        font-family: Arial, Verdana, monospace;
        border: 7px solid #1e3b63;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        background: #ad2828;
        }""")

    def simple_handler_thi(self):
        self.FirstAnswerButton.setStyleSheet(""" QPushButton {
        color: #363636;
        font-size: 18px;
        font-family: Arial, Verdana, monospace;
        border: 7px solid #1e3b63;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        background: #00cf08;
        }""")
        self.ThirdAnswerButton.setStyleSheet(""" QPushButton {
        color: #e2e2e2;
        font-size: 18px;
        font-family: Arial, Verdana, monospace;
        border: 7px solid #1e3b63;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        background: #ad2828;
        }""")

    def simple_handler_fou(self):
        self.FirstAnswerButton.setStyleSheet(""" QPushButton {
        color: #363636;
        font-size: 18px;
        font-family: Arial, Verdana, monospace;
        border: 7px solid #1e3b63;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        background: #00cf08;
        }""")
        self.FourthAnswerButton.setStyleSheet(""" QPushButton {
        color: #e2e2e2;
        font-size: 18px;
        font-family: Arial, Verdana, monospace;
        border: 7px solid #1e3b63;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        background: #ad2828;
        }""")

    def f_handler_push_button(self):
        self.counter += 1
        self.update_info()

    def handler_push_button(self):
        self.update_info()

    def update_info(self):
        self.question = self.test.get_question()
        if self.question == '<Questions ended>':
            self.show_results()
            return
        self.answers = self.test.get_answers()
        self.ButtonsList = [self.FirstAnswerButton, self.SecondAnswerButton,
        self.ThirdAnswerButton, self.FourthAnswerButton]
        self.QuestionLabel.setText(self.question)
        for i, item in enumerate(self.ButtonsList):
            item.setText(self.answers[i])
        random.shuffle(self.ButtonsList)
        for i, item in enumerate(self.ButtonsList):
            if i == 0:
                self.AnswerGridLayout.addWidget(item, 0, 0)
            if i == 1:
                self.AnswerGridLayout.addWidget(item, 0, 2)
            if i == 2:
                self.AnswerGridLayout.addWidget(item, 2, 0)
            if i == 3:
                self.AnswerGridLayout.addWidget(item, 2, 2)
        self.MainLayout.update()

    def show_results(self):
        counter = self.counter
        num_of_questions = TestObj().count_questions()
        result = counter * 12 / num_of_questions
        finalWindow.TAnswersFieldLabel.setText(str(counter))
        finalWindow.MarkLabel.setText(str(result))
        finalWindow.Progress.setValue(result)
        finalWindow.show()


class FinalWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setWindowFlags(QtCore.Qt.ToolTip)
        self.setWindowModality(2)

        desktop = QtWidgets.QApplication.desktop()

        pal = self.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                            QtGui.QColor('#aaa9a9'))
        pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
                            QtGui.QColor('#aaa9a9'))
        self.setPalette(pal)

        self.TestLabel = QLabel('Test name: ')
        self.TestLabel.setStyleSheet("""QLabel {
        font-size: 20px;
        font-family: Arial;
        }""")
        self.TestFieldLabel = QLabel(str(TestObj().get_name()))
        self.TestFieldLabel.setStyleSheet("""QLabel {
        font-size: 24px;
        font-family: Arial;
        font-weight: bold;
        border: 3px solid rgb(27, 3, 106);
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        }""")
        self.QuestionLabel = QLabel('Questions: ')
        self.QuestionLabel.setStyleSheet("""QLabel {
        font-size: 20px;
        font-family: Arial;
        }""")
        self.QuestionFieldLabel = QLabel(str(TestObj().count_questions()))
        self.QuestionFieldLabel.setStyleSheet("""QLabel {
        font-size: 24px;
        font-family: Arial;
        font-weight: bold;
        border: 3px solid rgb(27, 3, 106);
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        }""")
        self.TAnswersLabel = QLabel('True answers: ')
        self.TAnswersLabel.setStyleSheet("""QLabel {
        font-size: 20px;
        font-family: Arial;
        }""")
        self.TAnswersFieldLabel = QLabel()
        self.TAnswersFieldLabel.setStyleSheet("""QLabel {
        font-size: 24px;
        font-family: Arial;
        border: 3px solid rgb(27, 3, 106);
        font-weight: bold;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        }""")

        self.Progress = QProgressBar()
        self.Progress.setRange(0, 12)
        self.Progress.setFormat('%p% done')
        self.Progress.setStyleSheet(""" QProgressBar {
        border: 3px solid rgb(27, 3, 106);
        border-radius: 4px;
        text-align: center;
        color: #012342;
        font-weight: bold;
        }
        QProgressBar::chunk {background-color: #0ca5de}""")

        self.MarkLabel = QLabel()
        self.MarkLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.MarkLabel.setStyleSheet(""" QLabel {
        text-align: middle;
        font-size: 80px;
        color: #af0000;
        font-weight: bold;
        }""")

        self.exitButton = QPushButton('Exit')
        self.exitButton.clicked.connect(sys.exit)
        self.exitButton.setStyleSheet("""QPushButton {
        font-family: "Trebuchet MS", "Lucida Console", monospace;
        font-size: 20px;
        font-weight: bold;
        color: #f4f6f5;
        background-color: #02325f;
        }""")

        sizePolicy = QSizePolicy(QSizePolicy.Maximum,
                                QSizePolicy.Maximum)

        self.MainLayout = QtWidgets.QGridLayout()
        self.MainLayout.setSpacing(10)
        self.MainLayout.addWidget(self.TestLabel, 0, 0)
        self.MainLayout.addWidget(self.TestFieldLabel, 0, 1)
        self.MainLayout.addWidget(self.QuestionLabel, 1, 0)
        self.MainLayout.addWidget(self.QuestionFieldLabel, 1, 1)
        self.MainLayout.addWidget(self.TAnswersLabel, 2, 0)
        self.MainLayout.addWidget(self.TAnswersFieldLabel, 2, 1)
        self.MainLayout.addWidget(self.Progress, 3, 0, 3, 2)
        self.MainLayout.addWidget(self.MarkLabel, 6, 0, 6, 2)

        self.MainLayoutEnd = QVBoxLayout()
        self.MainLayoutEnd.addLayout(self.MainLayout)
        self.MainLayoutEnd.addWidget(self.exitButton, alignment=QtCore.Qt.AlignHCenter)

        self.TestLabel.setSizePolicy(sizePolicy)
        self.TestFieldLabel.setSizePolicy(sizePolicy)
        self.QuestionLabel.setSizePolicy(sizePolicy)
        self.QuestionFieldLabel.setSizePolicy(sizePolicy)
        self.TAnswersLabel.setSizePolicy(sizePolicy)
        self.TAnswersFieldLabel.setSizePolicy(sizePolicy)

        self.setLayout(self.MainLayoutEnd)

        self.adjustSize()
        start_point = QtCore.QPoint((desktop.width() - self.width()) // 2 ,
                            (desktop.height() - self.height()) // 2)
        self.move(start_point)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test = TestObj()
    window = Window(test)
    finalWindow = FinalWindow()
    window.setWindowTitle(test.get_name())
    window.show()
    sys.exit(app.exec_())
