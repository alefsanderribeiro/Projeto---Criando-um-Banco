# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_funcionario.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_cadastro_funcionario(object):
    def setupUi(self, cadastro_funcionario):
        if not cadastro_funcionario.objectName():
            cadastro_funcionario.setObjectName(u"cadastro_funcionario")
        cadastro_funcionario.resize(534, 500)
        cadastro_funcionario.setMinimumSize(QSize(500, 500))
        cadastro_funcionario.setWindowTitle(u"cadastro_funcionario")
        self.label = QLabel(cadastro_funcionario)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 50, 311, 221))

        self.retranslateUi(cadastro_funcionario)

        QMetaObject.connectSlotsByName(cadastro_funcionario)
    # setupUi

    def retranslateUi(self, cadastro_funcionario):
        self.label.setText(QCoreApplication.translate("cadastro_funcionario", u"<html><head/><body><p><span style=\" font-size:26pt;\">Funcion\u00e1rio</span></p></body></html>", None))
        pass
    # retranslateUi

