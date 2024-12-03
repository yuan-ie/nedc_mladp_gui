import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox, QStackedWidget, QScrollArea
from PyQt6.QtCore import Qt

import nedc_mladp_header_block as hd
from nedc_mladp_display_block import DisplayBlockManager
from nedc_mladp_stats_block import StatsBlockManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_idx = 0

        # Create manager objects
        self.display_block_manager = DisplayBlockManager()
        self.stats_block_manager = StatsBlockManager()

        # Set window properties
        self.setWindowTitle("Machine Learning Applications in Digital Pathology GUI")
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
        block_one = hd.title_block()
        content_layout.addWidget(block_one, 0)  # Stretch factor = 0, no extra space is given

        # block two -- menu bar
        block_two, about_button, data_button, types_button = hd.menu_block()
        content_layout.addLayout(block_two)


        # block three -- stacked widget
        self.stacked_widget = QStackedWidget()

        # Create widgets for each view
        self.about_widget = self.create_about_widget()
        self.data_widget = self.create_data_widget()
        self.types_widget = self.create_types_widget()
        self.more_widget = self.create_more_widget()
        self.more_widget.setWindowTitle("View More Slides")

        # Add widgets to the stacked widget
        self.stacked_widget.addWidget(self.about_widget)
        self.stacked_widget.addWidget(self.data_widget)
        self.stacked_widget.addWidget(self.types_widget)
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
        data_button.clicked.connect(self.show_data)   # Viewer button
        types_button.clicked.connect(self.show_types)   # Types button
        
    def create_about_widget(self):
        about_widget = QWidget()
        about_layout = QVBoxLayout()
        about_label = QLabel("""
    About the project:
    To minimize the time of cancer diagnosis, our team have created and used different Machine Learning models that
    could make predictions on breast tissue Biopsy slides.

    About this interface:
    This interface will allow users to select and view the original biopsy slides provided, as well as the annotations
    and predictions generated.
    In the All Data page:
        1. Select an image and click the "Select" button. This will display a JPEG image on the main window.
        2. Click the "More" button to view the annotations and predictions of different models in a separate window.
        3. Some important numbers are in the results window on the bottom of the main window.
                             """)
        about_layout.addWidget(about_label, 0)
        about_layout.addStretch(1)
        about_widget.setLayout(about_layout)

        return about_widget
    
    def create_data_widget(self):

        data_widget = QWidget()
        data_layout = QVBoxLayout()

        # Display the data
        display_block, self.button_select, self.button_more, self.button_save = self.display_block_manager.display_block()
        data_layout.addLayout(display_block)
        data_layout.addSpacing(20)

        stats_block = self.stats_block_manager.stats_block()
        data_layout.addLayout(stats_block)

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
    
    def create_types_widget(self):
        
        types_widget = QWidget()
        types_layout = QVBoxLayout()
        type_block = layouts.type_block()

        types_layout.addLayout(type_block, 0)
        types_layout.addStretch(1)
        types_widget.setLayout(types_layout)

        return types_widget
    
    def show_about(self):
        self.stacked_widget.setCurrentWidget(self.about_widget)

    def show_data(self):
        self.stacked_widget.setCurrentWidget(self.data_widget)

    def show_types(self):
        self.stacked_widget.setCurrentWidget(self.types_widget)

    def display_selected_item(self):
        self.more_widget.hide()
        self.display_block_manager.display_selected_item()
        original_file, cnn_file, rnf_file = self.display_block_manager.get_filenames()
        self.stats_block_manager.display_stats(original_file, cnn_file, rnf_file)

    def display_prev_item(self):
        self.image_idx = (self.image_idx-1) % 4
        self.display_block_manager.display_more_items(idx=self.image_idx)

    def display_next_item(self):
        self.image_idx = (self.image_idx+1) % 4
        self.display_block_manager.display_more_items(idx=self.image_idx)

    def toggle_more(self):
        if self.more_widget.isVisible():
            self.more_widget.hide()
        else:
            self.image_idx = 0
            self.more_widget.show()
            self.more_widget.setWindowTitle(self.display_block_manager.image_name)
            self.more_widget.update()