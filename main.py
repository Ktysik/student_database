import sys
from PyQt5.QtWidgets import QApplication
from ui import StudentApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentApp()
    window.show()
    sys.exit(app.exec_())
