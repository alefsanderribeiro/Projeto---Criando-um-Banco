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


from interfaces.template.ui_cadastro_funcionario import Ui_cadastro_funcionario



class cadastro_funcionario(QWidget):
    def __init__(self, *args, **kwargs):
        super(cadastro_funcionario, self).__init__(*args, **kwargs)
        self.ui = Ui_cadastro_funcionario()
        self.ui.setupUi(self)
        