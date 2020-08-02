#! /usr/bin/env python
# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from pdfcopyUI import Ui_Form
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import pyperclip as pyperclip
import os

class pdfcopyInterface(QWidget,Ui_Form):
    def __init__(self):
        super(pdfcopyInterface, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.deleteEnter.clicked.connect(self.deleteEnterAction)
        self.toSentence.clicked.connect(self.toSentenceAction)
        self.copy.clicked.connect(self.copyAction)

    def deleteEnterAction(self):
        self.label.setText("尚未复制")
        # print("deleteEnterTest")
        text = self.input.toPlainText()
        # print("获得text为：\n" + text)
        deleteEnterText = text.replace('\n',' ')
        # print("删除回车后的text为：\n" + deleteEnterText)
        self.input.setPlainText(deleteEnterText)

    def toSentenceAction(self):
        self.label.setText("尚未复制")
        # print("toSentenceAction")
        text = self.input.toPlainText()
        deleteEnterText = text.replace('\n', ' ')
        # print("deleteEnterText运行成功")

        punkt_param = PunktParameters()
        # 为避免句子在‘i.e.’后面被切分，使用nltk.tokenize.punkt并且自定义缩写词表。
        # 可以添加多个缩写词，注意添加的缩写词应该没有最后的“.”，比如i.e.写成i.e，比如al.写成al
        abbreviation = ['i.e', 'al']
        punkt_param.abbrev_types = set(abbreviation)
        tokenizer = PunktSentenceTokenizer(punkt_param)
        toSentenceText = tokenizer.tokenize(deleteEnterText)
        # for temp in toSentenceText:
        #     print(temp)
        self.input.setPlainText('\n'.join(toSentenceText))

    def copyAction(self):
        # print("copyAction")
        text = self.input.toPlainText()
        pyperclip.copy(text)
        self.label.setText("复制成功！")


if __name__ == '__main__':
    # current_directory = os.path.dirname(os.path.abspath(__file__))
    project_path = 'C:/Me/PyCharm-workspace/PDFCopy'
    os.chdir(project_path)
    sys.path.append(project_path)
    myapp = QApplication(sys.argv)
    pdfcopy = pdfcopyInterface()
    pdfcopy.show()
    sys.exit(myapp.exec_())