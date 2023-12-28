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


from interfaces.template.ui_cadastro_cliente import Ui_cadastro_cliente



class cadastro_cliente(QWidget):
    def __init__(self, *args, **kwargs):
        super(cadastro_cliente, self).__init__(*args, **kwargs)
        self.ui = Ui_cadastro_cliente()
        self.ui.setupUi(self)
        self.ui.radioButton_Fisica.toggled.connect(self.check_CPF)
        self.ui.radioButton_Juridico.toggled.connect(self.check_CNPJ)
    
        self.ui.Button_Novo.clicked.connect(self.limpar_dados)
        self.ui.Button_Cancelar.clicked.connect(self.cancelar)
        self.ui.Button_Salvar.clicked.connect(self.salvar)
        self.ui.Button_Pesquisar.clicked.connect(self.pesquisar)

    def __nome_normal(self):
        
        self.ui.label_CPF_CNPJ.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:7pt;\">CPF_ou_CNPJ</span></p></body></html>", None))
        self.ui.lineEdit_CPF_ou_CNPJ.setText("")
        self.ui.lineEdit_CPF_ou_CNPJ.setDisabled(True)
        
    def check_CPF(self, checked):
        if checked:
            self.ui.lineEdit_CPF_ou_CNPJ.setDisabled(False)
            self.ui.lineEdit_CPF_ou_CNPJ.setPlaceholderText(u"___.___.___-__")
            self.ui.label_CPF_CNPJ.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:7pt;\">CPF</span></p></body></html>", None))
            self.ui.lineEdit_CPF_ou_CNPJ.setMaxLength(14)
            self.ui.lineEdit_CPF_ou_CNPJ.setInputMask(u"000.000.000-00")
        else:
            self.__nome_normal()
        

    def check_CNPJ(self, checked):
        if checked:
            self.ui.lineEdit_CPF_ou_CNPJ.setDisabled(False)
            self.ui.lineEdit_CPF_ou_CNPJ.setPlaceholderText(u"__.___.___/____-__")
            self.ui.label_CPF_CNPJ.setText(QCoreApplication.translate("cadastro_cliente", u"<html><head/><body><p><span style=\" font-size:7pt;\">CNPJ</span></p></body></html>", None))
            self.ui.lineEdit_CPF_ou_CNPJ.setMaxLength(16)
            self.ui.lineEdit_CPF_ou_CNPJ.setInputMask("00.000.000/0000-00")
        else:
            self.__nome_normal()
        
    def limpar_dados(self):
        # Antes de limpar os dados, precisa ser verificado se algum dado foi alterado.
        # Após, pergunta-se se vai querer descartar as novas informações.
        
        self.ui.lineEdit_Codigo.clear()
        
    
    def cancelar(self):
        # Cancelar a inserção de dados
        pass
    
    def pesquisar(self):
        # Fazer uma janela de pesquisa de cadastros de clientes.
        # Dentro dessa nova janela, precisa acompanhar várias formas de pesquisar esses dados.
        # Após pesquisar e selecionar o "cliente", retornar todos os dados para a tela de cadastro de usuário.
        pass
