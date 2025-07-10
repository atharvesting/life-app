from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize QMainWindow
        self.setWindowTitle("Life App")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        test_button = QPushButton("Test Button")
        test_button2 = QPushButton("Test Mutton")
        
        self.stack = QStackedWidget()          # ✅ Create stack early
        page1 = QWidget()
        page2 = QWidget()
        self.stack.addWidget(page1)
        self.stack.addWidget(page2)

        layout.addWidget(test_button)          # ✅ Add nav button
        layout.addWidget(self.stack)           # ✅ Then add stack

        test_button.clicked.connect(lambda: self.stack.setCurrentIndex(1))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


