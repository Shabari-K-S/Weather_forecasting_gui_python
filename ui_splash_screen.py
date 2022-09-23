# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenKvfsWI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_splachscreen(object):
    def setupUi(self, splachscreen):
        if not splachscreen.objectName():
            splachscreen.setObjectName(u"splachscreen")
        splachscreen.resize(680, 400)
        self.centralwidget = QWidget(splachscreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius : 20px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 50, 661, 141))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"QLabel{\n"
"	color: rgb(87, 173, 255);\n"
"}")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.frame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(10, 140, 641, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(37, 290, 581, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.progressBar.setFont(font2)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style : none;\n"
"	border-radius: 10px;\n"
"	text-align : centre;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius : 10px;\n"
"	background-color:qlineargradient(spread:pad, x1:0.00568182, y1:0.523, x2:1, y2:0.477, stop:0 rgba(87, 173, 255, 255), stop:1 rgba(39, 79, 116, 255))}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 170, 641, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_loading = QLabel(self.frame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 661, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.label_loading.setFont(font3)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.frame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(30, 350, 621, 21))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        self.label_credits.setFont(font4)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_loading.raise_()
        self.label_title.raise_()
        self.label_description.raise_()
        self.progressBar.raise_()
        self.label_3.raise_()
        self.label_credits.raise_()

        self.verticalLayout.addWidget(self.frame)

        splachscreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splachscreen)

        QMetaObject.connectSlotsByName(splachscreen)
    # setupUi

    def retranslateUi(self, splachscreen):
        splachscreen.setWindowTitle(QCoreApplication.translate("splachscreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("splachscreen", u"<strong> WEATHER</strong> FORECASTING", None))
        self.label_description.setText(QCoreApplication.translate("splachscreen", u"<strong>MINI PROJECT<strong>", None))
        self.label_3.setText(QCoreApplication.translate("splachscreen", u"<strong>MINI<strong> Project", None))
        self.label_loading.setText(QCoreApplication.translate("splachscreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("splachscreen", u"<strong>Created :</strong> Shabari, <strong>Unnamed", None))
    # retranslateUi

