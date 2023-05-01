import sys

from datetime import date as dt

from random import randint

import sqlite3

from PyQt6.QtSql import *
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem, QMessageBox
from PyQt6.QtWidgets import QMainWindow, QLabel, QFileDialog, QMessageBox
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor


class Ui_MainWindow(object):  # в Первых 3-х классах дизайн окон
    def setupUi(self, MainWindow):  # Дизайн главного окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 260, 101, 31))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 260, 101, 31))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 310, 101, 31))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 310, 101, 31))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 100, 251, 121))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 360, 279, 39))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 70, 151, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 120, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 150, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 200, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 400, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 420, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Что-то там) (проект)"))
        self.label.setText(_translate("MainWindow", "выберите файл!!!"))
        self.pushButton_5.setText(_translate("MainWindow", "Выбрать файл с вопросами"))
        self.label_2.setText(_translate("MainWindow", "Количество вопросов:"))
        self.pushButton_6.setText(_translate("MainWindow", "начать"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.lineEdit.setText(_translate("MainWindow", "5"))
        self.label_4.setText(_translate("MainWindow", "Место для \nвашей рекламы"))


class Desain_windiw_result(object):  # Дизайн окна сохранения результатов
    def setupUi(self, MyWidget):
        MyWidget.setObjectName("MyWidget")
        MyWidget.setEnabled(True)
        MyWidget.resize(773, 645)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        MyWidget.setFont(font)
        #        MyWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MyWidget.setMouseTracking(False)
        MyWidget.setAnimated(False)
        MyWidget.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MyWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 250, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 80, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 120, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 200, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        MyWidget.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyWidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName("menubar")
        MyWidget.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyWidget)
        self.statusbar.setObjectName("statusbar")
        MyWidget.setStatusBar(self.statusbar)

        self.retranslateUi(MyWidget)
        QtCore.QMetaObject.connectSlotsByName(MyWidget)

    def retranslateUi(self, MyWidget):
        _translate = QtCore.QCoreApplication.translate
        MyWidget.setWindowTitle(_translate("MyWidget", "Запись результата"))
        self.label.setText(_translate("MyWidget", "спасибо за игру"))
        self.pushButton.setText(_translate("MyWidget", "записать результат"))
        self.label_2.setText(_translate("MyWidget", "здесь место для \nдля вашей рекламы"))
        self.label_4.setText(_translate("MyWidget", "введите ваше имя:"))


class Reclama_desiner(object):  # Дизайн окна рекламы
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 40, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 40, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 190, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 180, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 310, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 290, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 310, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 460, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "РЕКЛАМА!!!"))
        self.label.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_2.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_3.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_4.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_5.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_6.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_7.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_8.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_9.setText(_translate("MainWindow", "РЕКЛАМА"))
        self.label_10.setText(_translate("MainWindow", "С любовью, саша =)"))


class MyWidget(QMainWindow, Ui_MainWindow):  # Главное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.vibor_otveta)
        self.pushButton_2.clicked.connect(self.vibor_otveta)
        self.pushButton_3.clicked.connect(self.vibor_otveta)
        self.pushButton_4.clicked.connect(self.vibor_otveta)
        self.pushButton_5.clicked.connect(self.vibor_fayla)
        self.pushButton_6.clicked.connect(self.start)
        self.fname = ''
        self.n = -1  # Количество выборов ответа
        self.nombers_voprosov = 0
        self.praveln_otvet = 0
        self.label_4.installEventFilter(self)  # Обрабатываем все Event связаные с label_4

    def eventFilter(self, obj, e):  # Обрабатываем все Event связаные с label_4
        if e.type() == 2:  # Спрашиваем была ли нажата кнопка на мыши
            btn = e.button()
            self.Reclama()
        return super(QMainWindow, self).eventFilter(obj, e)  # Отправляем сигнал дальше

    def vibor_fayla(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Бд с вопросами', '')[0]
        self.label.setText('')
        self.con = sqlite3.connect(self.fname)
        self.textEdit.setText('')
        self.label_3.setText('')
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_6.show()  # Показываем кнопку "старт"
        self.praveln_otvet = 0
        self.n = -1

    def vibor_otveta(self):
        if not self.fname:
            return
        try:
            self.nombers_voprosov = (int(self.lineEdit.text())) - 1  # Узнаем кол-во вопросов
            if self.nombers_voprosov <= -1:
                raise ValueError
            if self.nombers_voprosov + 1 > len(self.voprosy):
                raise Len_menhe_Error
            if self.sender().text() == self.voprosy[self.n][1]:  # сравниваем выбор и правельный ответ
                self.label.setText('Молодец правильно')
                self.praveln_otvet += 1
            else:
                self.label.setText('Молодец НЕ правильно')
            if self.n + 1 > self.nombers_voprosov:  # Если вопросы закончились
                self.label_3.setText('Вы ответили на все вопросы')
                self.textEdit.setText('')
                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.pushButton_4.setText("")
                self.fname = ''
                self.zapis_rezult(self.praveln_otvet)
                return
            self.n += 1
            self.pokaz_vopros()
        except ValueError:
            self.label.setText('Введите коректное кол-во вопросов')
            self.error_box = QMessageBox()
            self.error_box.setWindowTitle('Ошибка')
            self.error_box.setText('Введите коректное кол-во вопросов')
            self.error_box.show()
        except Len_menhe_Error:
            self.label.setText('Слишком много вопросов')
            self.error_box = QMessageBox()
            self.error_box.setWindowTitle('Ошибка')
            self.error_box.setText('Слишком много вопросов')
            self.error_box.show()

    def start(self):
        if not self.fname:
            return
        try:
            self.label.setText('')
            voprosy_list = self.con.cursor().execute('SELECT * FROM voprosy').fetchall()
            self.voprosy = []  # получаем список вопросов и ответов на них
            for i in voprosy_list:
                self.voprosy.append(list(i))
            self.nombers_voprosov = (int(self.lineEdit.text())) - 1
            if self.nombers_voprosov <= -1:
                raise ValueError
            if self.nombers_voprosov + 1 > len(self.voprosy):
                raise Len_menhe_Error
            self.n += 1
            self.pokaz_vopros()
            self.pushButton_6.hide()
        except ValueError:
            self.label.setText('Введите коректное кол-во вопросов')
            self.error_box = QMessageBox()
            self.error_box.setWindowTitle('Ошибка')
            self.error_box.setText('Введите коректное кол-во вопросов')
            self.error_box.show()
        except Len_menhe_Error:
            self.label.setText('Cлишком много вопросов')
            self.error_box = QMessageBox()
            self.error_box.setWindowTitle('Ошибка')
            self.error_box.setText('Cлишком много вопросов')
            self.error_box.show()

    def pokaz_vopros(self):
        a = set()
        a.add(self.voprosy[self.n][1])
        while len(a) < 4:
            a.add(self.generacya_otvet())
        a = list(a)  # случайно распределаем ответы и сгенерированные ответы по кнопкам
        self.pushButton.setText(a[0])
        self.pushButton_2.setText(a[1])
        self.pushButton_3.setText(a[2])
        self.pushButton_4.setText(a[3])
        self.textEdit.setText(str(self.voprosy[self.n][0]))

    def generacya_otvet(self):
        data = (self.voprosy[self.n][1]).split('.')
        got = str(data[0])  # Генерируем ответ
        if got[0] + got[1] == '20':  # и если дата близкая к севоднешней мы уменьшаем диапозон дат
            year = int(got) - randint(0, 10)
            generate_data = dt(year, randint(1, 12), randint(1, 28))
        else:
            year = int(got) - randint(0, 35)
            generate_data = dt(year, randint(1, 12), randint(1, 28))
        generate_data = '.'.join(str(generate_data).split('-'))
        return generate_data

    def zapis_rezult(self, bals):  # Открываем окно и записываем результат
        self.okno_result = Windiw_result(bals)
        self.okno_result.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.n == -1:
                self.start()

    def Reclama(self):
        self.reclama = Reclama_Window()
        self.reclama.show()


class Windiw_result(QMainWindow, Desain_windiw_result):  # Окно записи результата
    def __init__(self, bals):
        super().__init__()
        self.setupUi(self)
        self.bals = bals
        self.pushButton.clicked.connect(self.save_result)
        self.label_2.installEventFilter(self)  # Обрабатываем все Event связаные с label_2

    def eventFilter(self, obj, e):  # Обрабатываем все Event связаные с label_2
        if e.type() == 2:  # Спрашиваем была ли нажата кнопка на мыши
            btn = e.button()
            self.Reclama()
        return super(QMainWindow, self).eventFilter(obj, e)

    def save_result(self):
        con = sqlite3.connect('resultaty.sqlite3')  # Результат записывается в файл
        cur = con.cursor()
        name = self.lineEdit.text()
        cur.execute("INSERT INTO resyltaty(name,bals) VALUES('" + str(name) + "','" + str(self.bals) + "')")
        con.commit()
        con.close()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.save_result()

    def Reclama(self):
        self.reclama = Reclama_Window()
        self.reclama.show()


class Reclama_Window(QMainWindow, Reclama_desiner):  # Окно рекламы
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Len_menhe_Error(Exception):
    pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

# pyuic5 progect.ui -o ui_file.py
