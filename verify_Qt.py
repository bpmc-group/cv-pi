import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello, Qt")
label.show()
app.exec()