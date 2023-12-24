import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import PyQt5.QtCore as QtCore

class CadastroUsuario(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Banco Digital 'Alefe'")
        self.setWindowState(QtCore.Qt.WindowMaximized)

        # Criando os widgets
        self.lbl_nome = QLabel("Nome:")
        self.lbl_email = QLabel("E-mail:")
        self.lbl_senha = QLabel("Senha:")

        self.txt_nome = QLineEdit()
        self.txt_email = QLineEdit()
        self.txt_senha = QLineEdit()

        self.btn_cadastrar = QPushButton("Cadastrar")

        # Posicionando os widgets
        self.lbl_nome.move(20, 20)
        self.txt_nome.move(80, 20)

        self.lbl_email.move(20, 60)
        self.txt_email.move(80, 60)

        self.lbl_senha.move(20, 100)
        self.txt_senha.move(80, 100)

        self.btn_cadastrar.move(150, 150)

        # Conectando os eventos
        self.btn_cadastrar.clicked.connect(self.cadastrar)

    def cadastrar(self):
        # Pegando os dados do formulário
        nome = self.txt_nome.text()
        email = self.txt_email.text()
        senha = self.txt_senha.text()

        # Validando os dados
        if nome == "" or email == "" or senha == "":
            print("Preencha todos os campos!")
            return

        # Cadastrando o usuário no banco de dados
        # (código simulado)
        print("Cadastrando usuário...")

        # Fechando a janela
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cadastro = CadastroUsuario()
    cadastro.show()
    sys.exit(app.exec_())

