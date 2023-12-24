# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janelaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QSizePolicy, QWidget)

class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        if not janelaPrincipal.objectName():
            janelaPrincipal.setObjectName(u"janelaPrincipal")
        janelaPrincipal.resize(700, 500)
        janelaPrincipal.setMinimumSize(QSize(700, 500))
        janelaPrincipal.setLayoutDirection(Qt.LeftToRight)
        janelaPrincipal.setAnimated(True)
        self.actionCliente = QAction(janelaPrincipal)
        self.actionCliente.setObjectName(u"actionCliente")
        self.actionCliente.setShortcutContext(Qt.WindowShortcut)
        self.actionFuncionario = QAction(janelaPrincipal)
        self.actionFuncionario.setObjectName(u"actionFuncionario")
        self.actionFornecedor = QAction(janelaPrincipal)
        self.actionFornecedor.setObjectName(u"actionFornecedor")
        self.actionTransportador = QAction(janelaPrincipal)
        self.actionTransportador.setObjectName(u"actionTransportador")
        self.actionPais = QAction(janelaPrincipal)
        self.actionPais.setObjectName(u"actionPais")
        self.actionEstado = QAction(janelaPrincipal)
        self.actionEstado.setObjectName(u"actionEstado")
        self.actionCidade = QAction(janelaPrincipal)
        self.actionCidade.setObjectName(u"actionCidade")
        self.actionBairro = QAction(janelaPrincipal)
        self.actionBairro.setObjectName(u"actionBairro")
        self.actionLogradouro = QAction(janelaPrincipal)
        self.actionLogradouro.setObjectName(u"actionLogradouro")
        self.actionCEP = QAction(janelaPrincipal)
        self.actionCEP.setObjectName(u"actionCEP")
        self.actionContas = QAction(janelaPrincipal)
        self.actionContas.setObjectName(u"actionContas")
        self.actionAg_ncias = QAction(janelaPrincipal)
        self.actionAg_ncias.setObjectName(u"actionAg_ncias")
        self.actionTurnos = QAction(janelaPrincipal)
        self.actionTurnos.setObjectName(u"actionTurnos")
        self.centralwidget = QWidget(janelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.horizontalLayout.addWidget(self.mdiArea)

        janelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(janelaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 25))
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuPessoa = QMenu(self.menuCadastro)
        self.menuPessoa.setObjectName(u"menuPessoa")
        self.menuPessoa.setTabletTracking(False)
        self.menuEndere_o = QMenu(self.menuCadastro)
        self.menuEndere_o.setObjectName(u"menuEndere_o")
        self.menuFinanceiro = QMenu(self.menubar)
        self.menuFinanceiro.setObjectName(u"menuFinanceiro")
        self.menuCaixa = QMenu(self.menuFinanceiro)
        self.menuCaixa.setObjectName(u"menuCaixa")
        self.menuRelat_rios = QMenu(self.menubar)
        self.menuRelat_rios.setObjectName(u"menuRelat_rios")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        self.menuContabilidade = QMenu(self.menubar)
        self.menuContabilidade.setObjectName(u"menuContabilidade")
        self.menuOpera_es = QMenu(self.menubar)
        self.menuOpera_es.setObjectName(u"menuOpera_es")
        janelaPrincipal.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuOpera_es.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menubar.addAction(self.menuContabilidade.menuAction())
        self.menubar.addAction(self.menuRelat_rios.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menuCadastro.addAction(self.menuPessoa.menuAction())
        self.menuCadastro.addAction(self.menuEndere_o.menuAction())
        self.menuCadastro.addAction(self.actionAg_ncias)
        self.menuCadastro.addAction(self.actionContas)
        self.menuPessoa.addAction(self.actionCliente)
        self.menuPessoa.addAction(self.actionFuncionario)
        self.menuPessoa.addAction(self.actionFornecedor)
        self.menuPessoa.addAction(self.actionTransportador)
        self.menuEndere_o.addAction(self.actionPais)
        self.menuEndere_o.addAction(self.actionEstado)
        self.menuEndere_o.addAction(self.actionCidade)
        self.menuEndere_o.addAction(self.actionBairro)
        self.menuEndere_o.addAction(self.actionLogradouro)
        self.menuEndere_o.addAction(self.actionCEP)
        self.menuFinanceiro.addAction(self.menuCaixa.menuAction())
        self.menuCaixa.addAction(self.actionTurnos)

        self.retranslateUi(janelaPrincipal)

        QMetaObject.connectSlotsByName(janelaPrincipal)
    # setupUi

    def retranslateUi(self, janelaPrincipal):
        janelaPrincipal.setWindowTitle(QCoreApplication.translate("janelaPrincipal", u"\u00c1lefe - Banco Digital", None))
        self.actionCliente.setText(QCoreApplication.translate("janelaPrincipal", u"Cliente", None))
        self.actionFuncionario.setText(QCoreApplication.translate("janelaPrincipal", u"Funcion\u00e1rio", None))
        self.actionFornecedor.setText(QCoreApplication.translate("janelaPrincipal", u"Fornecedor", None))
        self.actionTransportador.setText(QCoreApplication.translate("janelaPrincipal", u"Transportador", None))
        self.actionPais.setText(QCoreApplication.translate("janelaPrincipal", u"Pa\u00eds", None))
        self.actionEstado.setText(QCoreApplication.translate("janelaPrincipal", u"Estado", None))
        self.actionCidade.setText(QCoreApplication.translate("janelaPrincipal", u"Cidade", None))
        self.actionBairro.setText(QCoreApplication.translate("janelaPrincipal", u"Bairro", None))
        self.actionLogradouro.setText(QCoreApplication.translate("janelaPrincipal", u"Logradouro", None))
        self.actionCEP.setText(QCoreApplication.translate("janelaPrincipal", u"CEP", None))
        self.actionContas.setText(QCoreApplication.translate("janelaPrincipal", u"Contas", None))
        self.actionAg_ncias.setText(QCoreApplication.translate("janelaPrincipal", u"Ag\u00eancias", None))
        self.actionTurnos.setText(QCoreApplication.translate("janelaPrincipal", u"Turnos", None))
        self.menuCadastro.setTitle(QCoreApplication.translate("janelaPrincipal", u"Cadastro", None))
        self.menuPessoa.setTitle(QCoreApplication.translate("janelaPrincipal", u"Pessoa", None))
        self.menuEndere_o.setTitle(QCoreApplication.translate("janelaPrincipal", u"Endere\u00e7o", None))
        self.menuFinanceiro.setTitle(QCoreApplication.translate("janelaPrincipal", u"Financeiro", None))
        self.menuCaixa.setTitle(QCoreApplication.translate("janelaPrincipal", u"Caixa", None))
        self.menuRelat_rios.setTitle(QCoreApplication.translate("janelaPrincipal", u"Relat\u00f3rios", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("janelaPrincipal", u"Ajuda", None))
        self.menuContabilidade.setTitle(QCoreApplication.translate("janelaPrincipal", u"Contabilidade", None))
        self.menuOpera_es.setTitle(QCoreApplication.translate("janelaPrincipal", u"Opera\u00e7\u00f5es", None))
    # retranslateUi

