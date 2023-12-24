# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_transportador.ui'
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

class Ui_cadastro_transportador(object):
    def setupUi(self, cadastro_transportador):
        if not cadastro_transportador.objectName():
            cadastro_transportador.setObjectName(u"cadastro_transportador")
        cadastro_transportador.resize(594, 500)
        cadastro_transportador.setMinimumSize(QSize(500, 500))
        self.label = QLabel(cadastro_transportador)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 30, 311, 221))

        self.retranslateUi(cadastro_transportador)

        QMetaObject.connectSlotsByName(cadastro_transportador)
    # setupUi

    def retranslateUi(self, cadastro_transportador):
        cadastro_transportador.setWindowTitle(QCoreApplication.translate("cadastro_transportador", u"Form", None))
        self.label.setText(QCoreApplication.translate("cadastro_transportador", u"<html><head/><body><p><span style=\" font-size:26pt;\">Transportador</span></p></body></html>", None))
    # retranslateUi

