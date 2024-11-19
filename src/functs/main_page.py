import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox, QStackedWidget, QScrollArea
from PyQt6.QtCore import Qt

import layouts
from display_block import DisplayBlockManager
from stats_block import StatsBlockManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_idx = 0

        # Create manager objects
        self.display_block_manager = DisplayBlockManager()

        # Set window properties
        self.setWindowTitle("PyQt6 GUI with Styling")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0d1e1;")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setContentsMargins(20, 20, 20, 20)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout()
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        

        # block one -- title block
        block_one = layouts.title_block()
        content_layout.addWidget(block_one, 0)  # Stretch factor = 0, no extra space is given

        # block two -- menu bar
        block_two, about_button, data_button = layouts.menu_block()
        content_layout.addLayout(block_two)


        # block three -- stacked widget
        self.stacked_widget = QStackedWidget()

        # Create widgets for each view
        self.about_widget = self.create_about_widget()
        self.data_widget = self.create_data_widget()
        self.more_widget = self.create_more_widget()

        # Add widgets to the stacked widget
        self.stacked_widget.addWidget(self.about_widget)
        self.stacked_widget.addWidget(self.data_widget)
        # self.stacked_widget.addWidget(self.more_widget)
        content_layout.addWidget(self.stacked_widget)

        content_layout.addStretch(1)

        # Set the central widget layout
        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
        central_widget.setLayout(main_layout)

        # Connect buttons to corresponding slots
        about_button.clicked.connect(self.show_about)  # About Me button
        data_button.clicked.connect(self.show_data)   # All Data button
        
    def create_about_widget(self):
        about_widget = QWidget()
        about_layout = QVBoxLayout()
        about_label = QLabel("This will be about me...")
        about_layout.addWidget(about_label)
        about_widget.setLayout(about_layout)

        return about_widget
    
    def create_data_widget(self):

        data_widget = QWidget()
        data_layout = QVBoxLayout()

        # Display the data
        display_block, self.button_select, self.button_more, self.button_save = self.display_block_manager.display_block()
        data_layout.addLayout(display_block)
        data_layout.addSpacing(15)
        data_widget.setLayout(data_layout)

        self.button_select.clicked.connect(self.display_selected_item)
        
        return data_widget
    
    def create_more_widget(self):
    
        more_widget = QWidget()
        more_layout = QVBoxLayout()
    
        # Display more
        more_block, left_button, right_button = self.display_block_manager.display_more()
        more_layout.addLayout(more_block)
        more_widget.setLayout(more_layout)
        more_widget.hide()

        self.button_more.clicked.connect(self.toggle_more)
        left_button.clicked.connect(self.display_prev_item)
        right_button.clicked.connect(self.display_next_item)

        return more_widget
    
    def show_about(self):
        self.stacked_widget.setCurrentWidget(self.about_widget)

    def show_data(self):
        self.stacked_widget.setCurrentWidget(self.data_widget)

    def display_selected_item(self):
        self.more_widget.hide()
        self.display_block_manager.display_selected_item()

    def display_prev_item(self):
        self.image_idx = (self.image_idx+1) % 3
        self.display_block_manager.display_more_items(idx=self.image_idx)

    def display_next_item(self):
        self.image_idx = (self.image_idx+1) % 3
        self.display_block_manager.display_more_items(idx=self.image_idx)

    def toggle_more(self):
        if self.more_widget.isVisible():
            self.more_widget.hide()
        else:
            self.image_idx = 0
            self.more_widget.show()
            self.more_widget.update()