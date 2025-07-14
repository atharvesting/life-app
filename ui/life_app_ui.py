from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QStackedWidget
)
import sys
from pages.life_grid_page import LifeGridPage
from logic.logic import date_logic

# The MainWindow class defines the structure and logic of the app's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize the base QMainWindow class
        self.setWindowTitle("Life App")  # Set window title

        # Create the central widget that acts as the "canvas" for the app's layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)  # Set central_widget as the window's main content area

        # Create a vertical layout to stack widgets top-to-bottom inside the central widget
        layout = QVBoxLayout(central_widget)

        # Create the navigation button that will switch to Page 2 when clicked
        test_button = QPushButton("Test Button")

        # Create the stacked widget to manage multiple "pages"
        self.stack = QStackedWidget()

        # Create two placeholder pages as empty QWidgets
        page1 = QWidget()  # Page index 0
        page2 = LifeGridPage()  # Page index 1

        # Add the pages to the stack in the order you want them indexed
        self.stack.addWidget(page1)  # Adds page1 at index 0
        self.stack.addWidget(page2)  # Adds page2 at index 1

        # Add widgets to the main layout:
        # 1. Button at the top
        # 2. Page stack below the button
        layout.addWidget(test_button)
        layout.addWidget(self.stack)

        # Connect the button to change the visible page to index 1 (page2)
        test_button.clicked.connect(lambda: self.stack.setCurrentIndex(1))


# Main block that starts the Qt application loop
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Initialize the app engine
    window = MainWindow()         # Create the main window
    window.show()                 # Display the main window
    app.exec()                    # Run the app loop (blocking call until window is closed)

