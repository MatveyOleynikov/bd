# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 727)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.shop = QtWidgets.QWidget()
        self.shop.setObjectName("shop")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.shop)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.shop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.findEdit = QtWidgets.QLineEdit(self.shop)
        self.findEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.findEdit.setMaximumSize(QtCore.QSize(450, 16777215))
        self.findEdit.setObjectName("findEdit")
        self.horizontalLayout.addWidget(self.findEdit)
        self.findButton = QtWidgets.QPushButton(self.shop)
        self.findButton.setObjectName("findButton")
        self.horizontalLayout.addWidget(self.findButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.shop)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.shopTable = QtWidgets.QTableWidget(self.shop)
        self.shopTable.setMinimumSize(QtCore.QSize(0, 0))
        self.shopTable.setObjectName("shopTable")
        self.shopTable.setColumnCount(6)
        self.shopTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.shopTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.shopTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.shopTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.shopTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.shopTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.shopTable.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.shopTable)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.shop)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.nameEdit = QtWidgets.QLineEdit(self.widget)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_3.addWidget(self.nameEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.release_dateEdit = QtWidgets.QDateEdit(self.widget)
        self.release_dateEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.release_dateEdit.setObjectName("release_dateEdit")
        self.verticalLayout_6.addWidget(self.release_dateEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 2, 2, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.descriptionEdit = QtWidgets.QTextEdit(self.widget)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.verticalLayout_4.addWidget(self.descriptionEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 3, 2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBox.setMaximum(5000)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_5.addWidget(self.spinBox)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 228, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 2, 1, 1)
        self.scoreLabel = QtWidgets.QLabel(self.widget)
        self.scoreLabel.setObjectName("scoreLabel")
        self.gridLayout_2.addWidget(self.scoreLabel, 4, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 227, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 3, 2, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_9.addWidget(self.pushButton_3)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.developerBox = QtWidgets.QComboBox(self.widget)
        self.developerBox.setObjectName("developerBox")
        self.developerBox.addItem("")
        self.horizontalLayout_4.addWidget(self.developerBox)
        self.publisherBox = QtWidgets.QComboBox(self.widget)
        self.publisherBox.setObjectName("publisherBox")
        self.publisherBox.addItem("")
        self.horizontalLayout_4.addWidget(self.publisherBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_10, 5, 0, 2, 1)
        spacerItem4 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 6, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.editButton = QtWidgets.QPushButton(self.widget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_5.addWidget(self.editButton)
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_5.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_5.addWidget(self.deleteButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 6, 2, 1, 2)
        self.gridLayout_3.addWidget(self.widget, 0, 1, 1, 1)
        self.tabWidget.addTab(self.shop, "")
        self.library = QtWidgets.QWidget()
        self.library.setObjectName("library")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.library)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.label_8 = QtWidgets.QLabel(self.library)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.libraryTable = QtWidgets.QTableWidget(self.library)
        self.libraryTable.setMinimumSize(QtCore.QSize(0, 0))
        self.libraryTable.setObjectName("libraryTable")
        self.libraryTable.setColumnCount(6)
        self.libraryTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.libraryTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.libraryTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.libraryTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.libraryTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.libraryTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.libraryTable.setHorizontalHeaderItem(5, item)
        self.verticalLayout_8.addWidget(self.libraryTable)
        self.gridLayout_5.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.library)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_2)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(5)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_8.addWidget(self.spinBox_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_7.addWidget(self.textEdit)
        self.gridLayout_4.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.library, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.regiseterAction = QtWidgets.QAction(MainWindow)
        self.regiseterAction.setObjectName("regiseterAction")
        self.enterAction = QtWidgets.QAction(MainWindow)
        self.enterAction.setObjectName("enterAction")
        self.deleteAction = QtWidgets.QAction(MainWindow)
        self.deleteAction.setObjectName("deleteAction")
        self.turnOffAction = QtWidgets.QAction(MainWindow)
        self.turnOffAction.setObjectName("turnOffAction")
        self.turnOnAction = QtWidgets.QAction(MainWindow)
        self.turnOnAction.setObjectName("turnOnAction")
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.menu.addAction(self.regiseterAction)
        self.menu.addAction(self.enterAction)
        self.menu.addAction(self.exitAction)
        self.menu.addAction(self.deleteAction)
        self.menu_2.addAction(self.turnOffAction)
        self.menu_2.addAction(self.turnOnAction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Поиск игр"))
        self.findButton.setText(_translate("MainWindow", "Найти"))
        self.label.setText(_translate("MainWindow", "Список игр"))
        item = self.shopTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.shopTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата выхода"))
        item = self.shopTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.shopTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Разработчик"))
        item = self.shopTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Издатель"))
        item = self.shopTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Теги"))
        self.label_3.setText(_translate("MainWindow", "Название"))
        self.label_5.setText(_translate("MainWindow", "Дата релиза"))
        self.label_4.setText(_translate("MainWindow", "Описание"))
        self.label_6.setText(_translate("MainWindow", "Цена"))
        self.scoreLabel.setText(_translate("MainWindow", "Средняя оценка: "))
        self.pushButton.setText(_translate("MainWindow", "Найти по разработчик"))
        self.pushButton_3.setText(_translate("MainWindow", "Найти по издателю"))
        self.developerBox.setItemText(0, _translate("MainWindow", "Разработчик"))
        self.publisherBox.setItemText(0, _translate("MainWindow", "Издатель"))
        self.editButton.setText(_translate("MainWindow", "Редактировать"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shop), _translate("MainWindow", "Магазин"))
        self.label_8.setText(_translate("MainWindow", "Библиотека"))
        item = self.libraryTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.libraryTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата выхода"))
        item = self.libraryTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.libraryTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Разработчик"))
        item = self.libraryTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Издатель"))
        item = self.libraryTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Теги"))
        self.label_7.setText(_translate("MainWindow", "Название игры:"))
        self.label_9.setText(_translate("MainWindow", "Оценка:"))
        self.label_10.setText(_translate("MainWindow", "Комментарий:"))
        self.pushButton_2.setText(_translate("MainWindow", "Оставить отзыв"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.library), _translate("MainWindow", "Библиотека"))
        self.menu.setTitle(_translate("MainWindow", "Пользователь"))
        self.menu_2.setTitle(_translate("MainWindow", "Режим администратора"))
        self.regiseterAction.setText(_translate("MainWindow", "Зарегистироваться"))
        self.enterAction.setText(_translate("MainWindow", "Войти"))
        self.deleteAction.setText(_translate("MainWindow", "Удалить пользователя"))
        self.turnOffAction.setText(_translate("MainWindow", "Выключено"))
        self.turnOnAction.setText(_translate("MainWindow", "Включено"))
        self.exitAction.setText(_translate("MainWindow", "Выйти"))