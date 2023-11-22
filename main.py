import sys
import os.path
from Variables import var
from PyQt6.QtWidgets import QApplication
from Components.login import LoginPage
#from .Components.login import LoginPage


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #Save Root Directory (main.py) path to Variables
    var.root_dir_path=os.path.dirname(os.path.abspath(__file__))
    #app.setStyle("Fusion")
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec())