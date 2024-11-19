from PyQt6.QtWidgets import QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class StatsBlockManager:
    def __init__(self):
        self.selected_itemm = None

    def stats_block(self):
        '''
        Method:
            Create the statistics block.
        '''

        stats = QVBoxLayout()

        self.image_window = QGroupBox("More")
        self.image_window.setStyleSheet("background-color: lightblue;")
        self.image_window.setFixedSize(600,500)
        self.image_window.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_window_layout =  QVBoxLayout()

        self.image_label = QLabel("No image.")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_window_layout.addWidget(self.image_label)
        self.image_window.setLayout(self.image_window_layout)



        stats.addWidget(self.image_window)

        return stats