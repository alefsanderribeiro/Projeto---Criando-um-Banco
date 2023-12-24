# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_pessoas.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget, QVBoxLayout, QLineEdit, QPushButton)

class Ui_cadastro_funcionario(QWidget):
    def __init__(self):
        super().__init__()

        # Define as propriedades da janela
        self.setGeometry(0, 0, 400, 300)
        self.setWindowTitle("Cadastro de Funcionário")

        # Cria o layout vertical
        verticalLayout = QVBoxLayout(self)

        # Adiciona o rótulo "Nome" ao layout
        label = QLabel("Nome:")
        verticalLayout.addWidget(label)

        # Adiciona a caixa de edição de texto "lineEditNome" ao layout
        lineEditNome = QLineEdit()
        verticalLayout.addWidget(lineEditNome)

        # Adiciona o rótulo "CPF" ao layout
        label_2 = QLabel("CPF:")
        verticalLayout.addWidget(label_2)

        # Adiciona a caixa de edição de texto "lineEditCpf" ao layout
        lineEditCpf = QLineEdit()
        verticalLayout.addWidget(lineEditCpf)

        # Adiciona o botão "pushButtonSalvar" ao layout
        pushButtonSalvar = QPushButton("Salvar")
        verticalLayout.addWidget(pushButtonSalvar)

        # Conecta o sinal de clique do botão "pushButtonSalvar" ao método "salvar"
        #pushButtonSalvar.clicked.connect(self.salvar)
    # setupUi

    def retranslateUi(self, cadastro_funcionario):
        cadastro_funcionario.setWindowTitle(QCoreApplication.translate("cadastro_funcionario", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("cadastro_funcionario", u"Cadastro_Funcionario", None))
    # retranslateUi

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    widget = Ui_cadastro_funcionario()
    widget.show()
    sys.exit(app.exec())