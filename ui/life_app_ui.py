from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize QMainWindow
        self.setWindowTitle("Life App")
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        test_button = QPushButton("Test Button")
        test_button2 = QPushButton("Test Mutton")
        
        layout.addWidget(test_button)
        
        self.setCentralWidget(central_widget)
        
        stack_wig = QStackedWidget()
        layout2 = QVBoxLayout(stack_wig)
        
        layout.addChildLayout(layout2)
        layout2.addChildWidget(test_button2)
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


