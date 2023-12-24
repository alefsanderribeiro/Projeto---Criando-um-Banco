# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
sys.path.append(str(Path().absolute()))


from PySide6.QtWidgets import QApplication

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from .modulos.login import login


def interface():

    app = QApplication(sys.argv)
    widget = login()
    widget.show()
    sys.exit(app.exec())


interface()
