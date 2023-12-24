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


from interfaces.template.ui_janelaPrincipal import Ui_janelaPrincipal
from interfaces.template.ui_cadastro_funcionario import Ui_cadastro_funcionario

from interfaces.template.ui_cadastro_cliente import Ui_cadastro_cliente
from interfaces.template.ui_cadastro_fornecedor import Ui_cadastro_fornecedor
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
    
    def cadastro_cliente(self):
        subwindow = QMdiSubWindow()
        subwindow.setWindowTitle("Cadastro de Cliente")
        ui = Ui_cadastro_cliente()
        subwindow.setWidget(ui.setupUi(self))
        
        self.ui.mdiArea.addSubWindow(subwindow)
        subwindow.show()
        
    def cadastro_funcionario(self):
        
        subwindow = QMdiSubWindow()
        subwindow.setWindowTitle("Cadastro de Funcionario")
        cf = Ui_cadastro_funcionario()
        subwindow.setWidget(cf)
        
        self.ui.mdiArea.addSubWindow(subwindow)
        subwindow.show()
        
        
    def cadastro_fornecedor(self):
        
        subwindow = QMdiSubWindow()
        subwindow.setWindowTitle("Cadastro de Fornecedor")
        subwindow.setWidget(Ui_cadastro_fornecedor())
        
        self.ui.mdiArea.addSubWindow(subwindow)
        subwindow.show()
         
    def cadastro_transportador(self):
        
        subwindow = QMdiSubWindow()
        subwindow.setWindowTitle("Cadastro do Transportador")
        cf = Ui_cadastro_transportador()
        subwindow.setWidget(cf)
        
        self.ui.mdiArea.addSubWindow(subwindow)
        subwindow.show()
        
        

