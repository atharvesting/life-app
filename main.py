import sys
from PySide6.QtWidgets import QApplication
from ui.life_app_ui import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()