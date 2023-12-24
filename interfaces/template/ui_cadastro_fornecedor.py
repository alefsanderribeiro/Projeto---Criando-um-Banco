# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_fornecedor.ui'
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

class Ui_cadastro_fornecedor(object):
    def setupUi(self, cadastro_fornecedor):
        if not cadastro_fornecedor.objectName():
            cadastro_fornecedor.setObjectName(u"cadastro_fornecedor")
        cadastro_fornecedor.resize(586, 500)
        cadastro_fornecedor.setMinimumSize(QSize(500, 500))
        self.label = QLabel(cadastro_fornecedor)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 60, 311, 221))

        self.retranslateUi(cadastro_fornecedor)

        QMetaObject.connectSlotsByName(cadastro_fornecedor)
    # setupUi

    def retranslateUi(self, cadastro_fornecedor):
        cadastro_fornecedor.setWindowTitle(QCoreApplication.translate("cadastro_fornecedor", u"Form", None))
        self.label.setText(QCoreApplication.translate("cadastro_fornecedor", u"<html><head/><body><p><span style=\" font-size:26pt;\">Fornecedor</span></p></body></html>", None))
    # retranslateUi

