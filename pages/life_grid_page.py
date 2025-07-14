from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout
from PySide6.QtCore import QSize

class LifeGridPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        grid_layout = QGridLayout()

        total_weeks = 90 * 52  # adjust as needed
        cols = 52
        self.buttons = []
        
        for i in range(total_weeks):
            row = i // cols
            col = i % cols

            button = QPushButton("")  # keep text blank for now
            button.setFixedSize(QSize(15, 15))  # square size
            grid_layout.addWidget(button, row, col)
            self.buttons.append(button)
            
            grid_layout.setContentsMargins(10, 10, 10, 10)
            grid_layout.setSpacing(2)  # or 1 for denser grid


        self.setLayout(grid_layout)