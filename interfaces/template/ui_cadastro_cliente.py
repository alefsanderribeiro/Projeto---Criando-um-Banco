# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_cliente.ui'
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

class Ui_cadastro_cliente(object):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, cadastro_cliente): 
        if not cadastro_cliente.objectName():
            cadastro_cliente.setObjectName(u"cadastro_cliente")
        cadastro_cliente.resize(557, 500)
        cadastro_cliente.setMinimumSize(QSize(500, 500))
        self.label = QLabel(cadastro_cliente)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 50, 181, 221))

        self.retranslateUi(cadastro_cliente)

        QMetaObject.connectSlotsByName(cadastro_cliente)
    # setupUi

    def retranslateUi(self, cadastro_cliente):
        cadastro_cliente.setWindowTitle(QCoreApplication.translate("cadastro_cliente", u"Form", None))
        self.label.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:26pt;\">Cliente</span></p></body></html>", None))
    # retranslateUi

