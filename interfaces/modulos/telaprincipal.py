import sys
from pathlib import Path
sys.path.append(str(Path().absolute()))

#from PySide6.QtWidgets import QApplication, QWidget, QPushButton

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget, QMessageBox, QMdiSubWindow)

from interfaces.modulos.cadastro_cliente import cadastro_cliente
from interfaces.modulos.cadastro_funcionario import cadastro_funcionario
from interfaces.modulos.cadastro_fornecedor import cadastro_fornecedor
from interfaces.modulos.cadastro_transportador import cadastro_transportador



from interfaces.template.ui_janelaPrincipal import Ui_janelaPrincipal
from interfaces.template.ui_cadastro_transportador import Ui_cadastro_transportador


class janelaPrincipal(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(janelaPrincipal, self).__init__(*args, **kwargs)
        self.ui = Ui_janelaPrincipal()
        self.ui.setupUi(self)

        
        self.ui.actionCliente.triggered.connect(self.cadastro_cliente)
        self.ui.actionFuncionario.triggered.connect(self.cadastro_funcionario)
        self.ui.actionFornecedor.triggered.connect(self.cadastro_fornecedor)
        self.ui.actionTransportador.triggered.connect(self.cadastro_transportador)
        
    
    def _criar_subwindow(self, título_subwindow:str, modulo):
        self.subwindow = QMdiSubWindow()
        self.subwindow.setWindowTitle(título_subwindow)
        self.subwindow.setWidget(modulo)
        
        self.ui.mdiArea.addSubWindow(self.subwindow)
        self.subwindow.show()
        
    def cadastro_cliente(self):
        self._criar_subwindow("Cadastro do Cliente", cadastro_cliente())

    def cadastro_funcionario(self):
        self._criar_subwindow("Cadastro de Funcionario", cadastro_funcionario())

    def cadastro_fornecedor(self):
        self._criar_subwindow("Cadastro de Fornecedor", cadastro_fornecedor())

    def cadastro_transportador(self):
        self._criar_subwindow("Cadastro do Transportador", cadastro_transportador())

        

