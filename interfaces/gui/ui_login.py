# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import rc_imagens

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.setWindowModality(Qt.ApplicationModal)
        login.resize(500, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QSize(500, 500))
        login.setMaximumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u":/imagens/imagens/Logo - Icon - Alefe - Digital Bank.png", QSize(), QIcon.Active, QIcon.On)
        login.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(login)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/imagens/imagens/Logo - Alefe - Digital Bank.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.botaoEsqueceuSuaSenha = QPushButton(self.frame)
        self.botaoEsqueceuSuaSenha.setObjectName(u"botaoEsqueceuSuaSenha")

        self.gridLayout.addWidget(self.botaoEsqueceuSuaSenha, 4, 0, 1, 1)

        self.botaoEntrar = QPushButton(self.frame)
        self.botaoEntrar.setObjectName(u"botaoEntrar")

        self.gridLayout.addWidget(self.botaoEntrar, 3, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_login = QLabel(self.frame)
        self.label_login.setObjectName(u"label_login")

        self.horizontalLayout.addWidget(self.label_login)

        self.horizontalSpacer = QSpacerItem(5, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.LineEditLogin = QLineEdit(self.frame)
        self.LineEditLogin.setObjectName(u"LineEditLogin")
        self.LineEditLogin.setMinimumSize(QSize(380, 0))
        self.LineEditLogin.setMaxLength(10)

        self.horizontalLayout.addWidget(self.LineEditLogin)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_senha = QLabel(self.frame)
        self.label_senha.setObjectName(u"label_senha")

        self.horizontalLayout_2.addWidget(self.label_senha)

        self.horizontalSpacer_2 = QSpacerItem(5, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.LineEditSenha = QLineEdit(self.frame)
        self.LineEditSenha.setObjectName(u"LineEditSenha")
        self.LineEditSenha.setMinimumSize(QSize(380, 0))
        self.LineEditSenha.setMaxLength(255)
        self.LineEditSenha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.LineEditSenha)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 2, 1)


        self.verticalLayout_2.addWidget(self.frame)

        QWidget.setTabOrder(self.LineEditLogin, self.LineEditSenha)
        QWidget.setTabOrder(self.LineEditSenha, self.botaoEntrar)
        QWidget.setTabOrder(self.botaoEntrar, self.botaoEsqueceuSuaSenha)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Banco Digital 'Alefe'", None))
        login.setWindowFilePath(QCoreApplication.translate("login", u"C:\\Users\\Alefs\\Documentos\\Mega\\Documentos\\Drive\\Projetos\\Projeto---Criando-um-Banco\\main.py", None))
        self.label.setText("")
        self.botaoEsqueceuSuaSenha.setText(QCoreApplication.translate("login", u"Esqueceu sua senha?", None))
        self.botaoEntrar.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.label_login.setText(QCoreApplication.translate("login", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Login</span></p></body></html>", None))
        self.LineEditLogin.setPlaceholderText(QCoreApplication.translate("login", u"Digita seu Login", None))
        self.label_senha.setText(QCoreApplication.translate("login", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Senha</span></p></body></html>", None))
        self.LineEditSenha.setText("")
        self.LineEditSenha.setPlaceholderText(QCoreApplication.translate("login", u"Digita sua Senha", None))
    # retranslateUi

