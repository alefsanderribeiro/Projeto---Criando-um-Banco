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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QGroupBox, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_cadastro_cliente(object):
    def setupUi(self, cadastro_cliente):
        if not cadastro_cliente.objectName():
            cadastro_cliente.setObjectName(u"cadastro_cliente")
        cadastro_cliente.resize(655, 500)
        cadastro_cliente.setMinimumSize(QSize(655, 500))
        cadastro_cliente.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(cadastro_cliente)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(cadastro_cliente)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(500, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_CPF_ou_CNPJ = QLineEdit(self.groupBox_2)
        self.lineEdit_CPF_ou_CNPJ.setObjectName(u"lineEdit_CPF_ou_CNPJ")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_CPF_ou_CNPJ.sizePolicy().hasHeightForWidth())
        self.lineEdit_CPF_ou_CNPJ.setSizePolicy(sizePolicy)
        self.lineEdit_CPF_ou_CNPJ.setMinimumSize(QSize(0, 20))
        self.lineEdit_CPF_ou_CNPJ.setMaxLength(32767)
        self.lineEdit_CPF_ou_CNPJ.setPlaceholderText(u"___.___.___-__")
        self.lineEdit_CPF_ou_CNPJ.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_4.addWidget(self.lineEdit_CPF_ou_CNPJ, 1, 6, 1, 3)

        self.dateEdit_cadastro = QDateEdit(self.groupBox_2)
        self.dateEdit_cadastro.setObjectName(u"dateEdit_cadastro")
        sizePolicy.setHeightForWidth(self.dateEdit_cadastro.sizePolicy().hasHeightForWidth())
        self.dateEdit_cadastro.setSizePolicy(sizePolicy)
        self.dateEdit_cadastro.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setPointSize(7)
        self.dateEdit_cadastro.setFont(font)
        self.dateEdit_cadastro.setWrapping(False)
        self.dateEdit_cadastro.setAlignment(Qt.AlignCenter)
        self.dateEdit_cadastro.setReadOnly(False)
        self.dateEdit_cadastro.setAccelerated(False)
        self.dateEdit_cadastro.setTime(QTime(0, 0, 0))
        self.dateEdit_cadastro.setCalendarPopup(True)
        self.dateEdit_cadastro.setDate(QDate(2000, 1, 1))

        self.gridLayout_4.addWidget(self.dateEdit_cadastro, 1, 9, 1, 4)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 2)

        self.lineEdit_Codigo = QLineEdit(self.groupBox_2)
        self.lineEdit_Codigo.setObjectName(u"lineEdit_Codigo")
        sizePolicy.setHeightForWidth(self.lineEdit_Codigo.sizePolicy().hasHeightForWidth())
        self.lineEdit_Codigo.setSizePolicy(sizePolicy)
        self.lineEdit_Codigo.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.lineEdit_Codigo, 1, 0, 1, 1)

        self.radioButton_Juridico = QRadioButton(self.groupBox_2)
        self.radioButton_Juridico.setObjectName(u"radioButton_Juridico")
        font1 = QFont()
        font1.setPointSize(8)
        self.radioButton_Juridico.setFont(font1)
        self.radioButton_Juridico.setIconSize(QSize(10, 10))
        self.radioButton_Juridico.setCheckable(True)
        self.radioButton_Juridico.setChecked(False)
        self.radioButton_Juridico.setAutoRepeat(False)
        self.radioButton_Juridico.setAutoExclusive(False)

        self.gridLayout_4.addWidget(self.radioButton_Juridico, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.radioButton_Fisica = QRadioButton(self.groupBox_2)
        self.radioButton_Fisica.setObjectName(u"radioButton_Fisica")
        self.radioButton_Fisica.setMinimumSize(QSize(0, 0))
        self.radioButton_Fisica.setFont(font1)
        self.radioButton_Fisica.setIconSize(QSize(10, 10))
        self.radioButton_Fisica.setCheckable(True)
        self.radioButton_Fisica.setChecked(False)

        self.gridLayout_4.addWidget(self.radioButton_Fisica, 1, 2, 1, 1)

        self.checkBox_ativo_ou_inativo = QCheckBox(self.groupBox_2)
        self.checkBox_ativo_ou_inativo.setObjectName(u"checkBox_ativo_ou_inativo")
        self.checkBox_ativo_ou_inativo.setMinimumSize(QSize(20, 20))
        self.checkBox_ativo_ou_inativo.setMaximumSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.checkBox_ativo_ou_inativo, 0, 12, 1, 1)

        self.label_CPF_CNPJ = QLabel(self.groupBox_2)
        self.label_CPF_CNPJ.setObjectName(u"label_CPF_CNPJ")
        self.label_CPF_CNPJ.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_CPF_CNPJ, 0, 6, 1, 3)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_12, 0, 11, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_11, 0, 9, 1, 2)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_Apelido = QLineEdit(self.groupBox_3)
        self.lineEdit_Apelido.setObjectName(u"lineEdit_Apelido")
        self.lineEdit_Apelido.setMinimumSize(QSize(0, 20))

        self.gridLayout_3.addWidget(self.lineEdit_Apelido, 1, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.lineEdit_Nome = QLineEdit(self.groupBox_3)
        self.lineEdit_Nome.setObjectName(u"lineEdit_Nome")
        self.lineEdit_Nome.setMinimumSize(QSize(0, 20))

        self.gridLayout_3.addWidget(self.lineEdit_Nome, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 2, 1)

        self.groupBox_21 = QGroupBox(cadastro_cliente)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMinimumSize(QSize(75, 478))
        self.groupBox_21.setMaximumSize(QSize(75, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox_21)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Button_Novo = QPushButton(self.groupBox_21)
        self.Button_Novo.setObjectName(u"Button_Novo")
        self.Button_Novo.setMinimumSize(QSize(70, 30))

        self.verticalLayout.addWidget(self.Button_Novo)

        self.Button_Salvar = QPushButton(self.groupBox_21)
        self.Button_Salvar.setObjectName(u"Button_Salvar")

        self.verticalLayout.addWidget(self.Button_Salvar)

        self.Button_Cancelar = QPushButton(self.groupBox_21)
        self.Button_Cancelar.setObjectName(u"Button_Cancelar")

        self.verticalLayout.addWidget(self.Button_Cancelar)

        self.verticalSpacer_2 = QSpacerItem(10, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.Button_Pesquisar = QPushButton(self.groupBox_21)
        self.Button_Pesquisar.setObjectName(u"Button_Pesquisar")

        self.verticalLayout.addWidget(self.Button_Pesquisar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Button_Fechar = QPushButton(self.groupBox_21)
        self.Button_Fechar.setObjectName(u"Button_Fechar")

        self.verticalLayout.addWidget(self.Button_Fechar)


        self.gridLayout.addWidget(self.groupBox_21, 0, 1, 4, 1)

        self.tabWidget = QTabWidget(cadastro_cliente)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QSize(500, 0))
        font2 = QFont()
        font2.setPointSize(6)
        self.tabWidget.setFont(font2)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.lgpd = QWidget()
        self.lgpd.setObjectName(u"lgpd")
        self.gridLayout_2 = QGridLayout(self.lgpd)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_13 = QLabel(self.lgpd)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.lgpd)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_15 = QLabel(self.lgpd)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 0, 2, 1, 2)

        self.label_16 = QLabel(self.lgpd)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_16, 0, 4, 1, 1)

        self.label_17 = QLabel(self.lgpd)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_17, 0, 5, 1, 1)

        self.dateEdit_cadastro_2 = QDateEdit(self.lgpd)
        self.dateEdit_cadastro_2.setObjectName(u"dateEdit_cadastro_2")
        sizePolicy.setHeightForWidth(self.dateEdit_cadastro_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_cadastro_2.setSizePolicy(sizePolicy)
        self.dateEdit_cadastro_2.setMinimumSize(QSize(0, 20))
        self.dateEdit_cadastro_2.setFont(font)
        self.dateEdit_cadastro_2.setWrapping(False)
        self.dateEdit_cadastro_2.setAlignment(Qt.AlignCenter)
        self.dateEdit_cadastro_2.setReadOnly(False)
        self.dateEdit_cadastro_2.setAccelerated(False)
        self.dateEdit_cadastro_2.setTime(QTime(0, 0, 0))
        self.dateEdit_cadastro_2.setCalendarPopup(True)
        self.dateEdit_cadastro_2.setDate(QDate(2000, 1, 1))

        self.gridLayout_2.addWidget(self.dateEdit_cadastro_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.lgpd)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 20))
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setMaxCount(3)

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.dateEdit_cadastro_4 = QDateEdit(self.lgpd)
        self.dateEdit_cadastro_4.setObjectName(u"dateEdit_cadastro_4")
        sizePolicy.setHeightForWidth(self.dateEdit_cadastro_4.sizePolicy().hasHeightForWidth())
        self.dateEdit_cadastro_4.setSizePolicy(sizePolicy)
        self.dateEdit_cadastro_4.setMinimumSize(QSize(0, 20))
        self.dateEdit_cadastro_4.setFont(font)
        self.dateEdit_cadastro_4.setWrapping(False)
        self.dateEdit_cadastro_4.setAlignment(Qt.AlignCenter)
        self.dateEdit_cadastro_4.setReadOnly(False)
        self.dateEdit_cadastro_4.setAccelerated(False)
        self.dateEdit_cadastro_4.setTime(QTime(0, 0, 0))
        self.dateEdit_cadastro_4.setCalendarPopup(True)
        self.dateEdit_cadastro_4.setDate(QDate(2000, 1, 1))

        self.gridLayout_2.addWidget(self.dateEdit_cadastro_4, 1, 2, 1, 2)

        self.lineEdit_Codigo_2 = QLineEdit(self.lgpd)
        self.lineEdit_Codigo_2.setObjectName(u"lineEdit_Codigo_2")
        sizePolicy.setHeightForWidth(self.lineEdit_Codigo_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_Codigo_2.setSizePolicy(sizePolicy)
        self.lineEdit_Codigo_2.setMinimumSize(QSize(0, 20))
        self.lineEdit_Codigo_2.setMaxLength(10)

        self.gridLayout_2.addWidget(self.lineEdit_Codigo_2, 1, 4, 1, 1)

        self.lineEdit_Codigo_3 = QLineEdit(self.lgpd)
        self.lineEdit_Codigo_3.setObjectName(u"lineEdit_Codigo_3")
        sizePolicy.setHeightForWidth(self.lineEdit_Codigo_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_Codigo_3.setSizePolicy(sizePolicy)
        self.lineEdit_Codigo_3.setMinimumSize(QSize(0, 20))
        self.lineEdit_Codigo_3.setMaxLength(10)

        self.gridLayout_2.addWidget(self.lineEdit_Codigo_3, 1, 5, 1, 1)

        self.label_23 = QLabel(self.lgpd)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_23, 2, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.lgpd)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 20))
        self.comboBox_3.setMaxVisibleItems(10)
        self.comboBox_3.setMaxCount(10)

        self.gridLayout_2.addWidget(self.comboBox_3, 3, 0, 1, 1)

        self.lineEdit_Codigo_6 = QLineEdit(self.lgpd)
        self.lineEdit_Codigo_6.setObjectName(u"lineEdit_Codigo_6")
        sizePolicy.setHeightForWidth(self.lineEdit_Codigo_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_Codigo_6.setSizePolicy(sizePolicy)
        self.lineEdit_Codigo_6.setMinimumSize(QSize(0, 20))
        self.lineEdit_Codigo_6.setMaxLength(10)

        self.gridLayout_2.addWidget(self.lineEdit_Codigo_6, 3, 1, 1, 3)

        self.lineEdit_Codigo_7 = QLineEdit(self.lgpd)
        self.lineEdit_Codigo_7.setObjectName(u"lineEdit_Codigo_7")
        sizePolicy.setHeightForWidth(self.lineEdit_Codigo_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_Codigo_7.setSizePolicy(sizePolicy)
        self.lineEdit_Codigo_7.setMinimumSize(QSize(0, 20))
        self.lineEdit_Codigo_7.setMaxLength(10)

        self.gridLayout_2.addWidget(self.lineEdit_Codigo_7, 3, 4, 1, 2)

        self.lineEdit_Codigo_8 = QLineEdit(self.lgpd)
        self.lineEdit_Codigo_8.setObjectName(u"lineEdit_Codigo_8")
        sizePolicy.setHeightForWidth(self.lineEdit_Codigo_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_Codigo_8.setSizePolicy(sizePolicy)
        self.lineEdit_Codigo_8.setMinimumSize(QSize(0, 20))
        self.lineEdit_Codigo_8.setMaxLength(10)

        self.gridLayout_2.addWidget(self.lineEdit_Codigo_8, 5, 0, 1, 3)

        self.lineEdit_Codigo_9 = QLineEdit(self.lgpd)
        self.lineEdit_Codigo_9.setObjectName(u"lineEdit_Codigo_9")
        sizePolicy.setHeightForWidth(self.lineEdit_Codigo_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_Codigo_9.setSizePolicy(sizePolicy)
        self.lineEdit_Codigo_9.setMinimumSize(QSize(0, 20))
        self.lineEdit_Codigo_9.setMaxLength(10)

        self.gridLayout_2.addWidget(self.lineEdit_Codigo_9, 5, 3, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(168, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 6, 0, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(168, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 6, 4, 1, 2)

        self.label_27 = QLabel(self.lgpd)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_27, 4, 3, 1, 3)

        self.label_26 = QLabel(self.lgpd)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_26, 4, 0, 1, 3)

        self.label_25 = QLabel(self.lgpd)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_25, 2, 4, 1, 2)

        self.label_24 = QLabel(self.lgpd)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_24, 2, 1, 1, 3)

        self.tabWidget.addTab(self.lgpd, "")
        self.principal = QWidget()
        self.principal.setObjectName(u"principal")
        self.tabWidget.addTab(self.principal, "")
        self.endereco = QWidget()
        self.endereco.setObjectName(u"endereco")
        self.tabWidget.addTab(self.endereco, "")
        self.contato = QWidget()
        self.contato.setObjectName(u"contato")
        self.tabWidget.addTab(self.contato, "")
        self.web = QWidget()
        self.web.setObjectName(u"web")
        self.tabWidget.addTab(self.web, "")
        self.trabalho = QWidget()
        self.trabalho.setObjectName(u"trabalho")
        self.tabWidget.addTab(self.trabalho, "")
        self.referencias = QWidget()
        self.referencias.setObjectName(u"referencias")
        self.tabWidget.addTab(self.referencias, "")
        self.financeiro = QWidget()
        self.financeiro.setObjectName(u"financeiro")
        self.tabWidget.addTab(self.financeiro, "")
        self.formas_pagto = QWidget()
        self.formas_pagto.setObjectName(u"formas_pagto")
        self.tabWidget.addTab(self.formas_pagto, "")
        self.spc = QWidget()
        self.spc.setObjectName(u"spc")
        self.tabWidget.addTab(self.spc, "")

        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 1)


        self.retranslateUi(cadastro_cliente)
        self.radioButton_Fisica.toggled.connect(self.radioButton_Juridico.setDisabled)
        self.radioButton_Juridico.toggled.connect(self.radioButton_Fisica.setDisabled)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(cadastro_cliente)
    # setupUi

    def retranslateUi(self, cadastro_cliente):
        cadastro_cliente.setWindowTitle(QCoreApplication.translate("cadastro_cliente", u"Form", None))
        self.groupBox.setTitle("")
        self.lineEdit_CPF_ou_CNPJ.setInputMask("")
        self.label_6.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:7pt;\">Tipo de Pessoa</span></p></body></html>", None))
        self.lineEdit_Codigo.setText("")
#if QT_CONFIG(tooltip)
        self.radioButton_Juridico.setToolTip(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:6pt;\">F\u00edsica</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_Juridico.setText(QCoreApplication.translate("cadastro_cliente", u"Jur\u00eddica", None))
        self.label_9.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p>C\u00f3digo</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.radioButton_Fisica.setToolTip(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p align=\"center\"><span style=\" font-size:6pt;\">F\u00edsica</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_Fisica.setText(QCoreApplication.translate("cadastro_cliente", u"F\u00edsica", None))
        self.checkBox_ativo_ou_inativo.setText("")
        self.label_CPF_CNPJ.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:7pt;\">CPF / CNPJ</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:7pt;\">Ativo</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:7pt;\">Data Cadastro</span></p></body></html>", None))
        self.lineEdit_Apelido.setText("")
        self.label_7.setText(QCoreApplication.translate("cadastro_cliente", u"Apelido / Nome Fantasia", None))
        self.label_8.setText(QCoreApplication.translate("cadastro_cliente", u"Nome / Raz\u00e3o Social", None))
        self.lineEdit_Nome.setText("")
        self.groupBox_21.setTitle("")
        self.Button_Novo.setText(QCoreApplication.translate("cadastro_cliente", u"Novo", None))
        self.Button_Salvar.setText(QCoreApplication.translate("cadastro_cliente", u"Salvar", None))
        self.Button_Cancelar.setText(QCoreApplication.translate("cadastro_cliente", u"Cancelar", None))
        self.Button_Pesquisar.setText(QCoreApplication.translate("cadastro_cliente", u"Pesquisar", None))
        self.Button_Fechar.setText(QCoreApplication.translate("cadastro_cliente", u"Fechar", None))
        self.label_13.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">Data de Nascimento</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">Sexo</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">Data Emiss\u00e3o RG</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">N\u00famero do RG</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">\u00d3rg\u00e3o Experidor RG</span></p></body></html>", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("cadastro_cliente", u"Masculino", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("cadastro_cliente", u"Feminino", None))

        self.lineEdit_Codigo_2.setText("")
        self.lineEdit_Codigo_3.setText("")
        self.label_23.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">Estado Civil</span></p></body></html>", None))
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.setItemText(1, QCoreApplication.translate("cadastro_cliente", u"Casado", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("cadastro_cliente", u"Vi\u00favo", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("cadastro_cliente", u"Solteiro", None))

        self.lineEdit_Codigo_6.setText("")
        self.lineEdit_Codigo_7.setText("")
        self.lineEdit_Codigo_8.setText("")
        self.lineEdit_Codigo_9.setText("")
        self.label_27.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">Nome da M\u00e3e</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">Nome do Pai</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">Naturalidade</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:8pt;\">Nacionalidade</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lgpd), QCoreApplication.translate("cadastro_cliente", u"LGPD", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.principal), QCoreApplication.translate("cadastro_cliente", u"Principal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.endereco), QCoreApplication.translate("cadastro_cliente", u"Endere\u00e7o Principal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contato), QCoreApplication.translate("cadastro_cliente", u"Fone / Contato", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.web), QCoreApplication.translate("cadastro_cliente", u"Web", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trabalho), QCoreApplication.translate("cadastro_cliente", u"Trabalho", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.referencias), QCoreApplication.translate("cadastro_cliente", u"Refer\u00eancias", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.financeiro), QCoreApplication.translate("cadastro_cliente", u"Vendas/Financeiro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.formas_pagto), QCoreApplication.translate("cadastro_cliente", u"Formas Pagto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spc), QCoreApplication.translate("cadastro_cliente", u"SPC/SERASA", None))
    # retranslateUi

