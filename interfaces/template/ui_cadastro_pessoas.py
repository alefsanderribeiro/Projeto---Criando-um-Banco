# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_pessoas.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)

class Ui_cadastro_funcionario(QWidget):
    def setupUi(self, cadastro_funcionario):
        if not cadastro_funcionario.objectName():
            cadastro_funcionario.setObjectName(u"cadastro_funcionario")
        cadastro_funcionario.resize(800, 600)
        self.centralwidget = QWidget(cadastro_funcionario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 240, 431, 20))
        cadastro_funcionario.setCentralWidget(self.centralwidget)

        self.retranslateUi(cadastro_funcionario)

        QMetaObject.connectSlotsByName(cadastro_funcionario)
    # setupUi

    def retranslateUi(self, cadastro_funcionario):
        cadastro_funcionario.setWindowTitle(QCoreApplication.translate("cadastro_funcionario", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("cadastro_funcionario", u"Cadastro_Funcionario", None))
    # retranslateUi

