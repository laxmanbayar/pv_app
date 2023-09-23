import sys
from PyQt6.QtWidgets import QApplication
from Components.login import LoginPage


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("Fusion")
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec())