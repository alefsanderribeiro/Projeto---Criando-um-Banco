import sys
from pathlib import Path
sys.path.append(str(Path().absolute()))


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget, QMessageBox)



from interfaces.template.ui_login import Ui_login
from interfaces.modulos.telaprincipal import janelaPrincipal
from banco_de_dados import banco_dados as bd



class login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        
        self.ui.botaoEntrar.clicked.connect(self.entrar)
        self.ui.botaoEsqueceuSuaSenha.clicked.connect(self.esqueceu_senha)
        
        
    def entrar(self):

        user_botao = self.ui.LineEditLogin.text()
        pass_botao = self.ui.LineEditSenha.text()
        
        if bd.Procurar.senha_do_funcionario(user_botao, pass_botao):
            
            QMessageBox.information(QMessageBox(), "Login Realizado!", "Seja Bem vindo!")
            
            self.tela = janelaPrincipal()
            self.tela.show()
            login.hide(self)
        else:
            QMessageBox.warning(QMessageBox(), "Login Error!", "Verifique seus dados!")
    
    def esqueceu_senha(self):
        
        # Depois irei criar umas opções para recuperação de senha por meio do email e Celular. Estudar futuramente isso.
        # Ou então, irei soliciar para entrar em contato com o Administrador para a recuperação da senha.
        print("Esqueceu sua Senha")
        

