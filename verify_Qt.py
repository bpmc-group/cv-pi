import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello, Qt is now available\n\n How 'bout 'dem apples?")
label.show()
app.exec()