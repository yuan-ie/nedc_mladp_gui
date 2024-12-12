import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox, QStackedWidget, QScrollArea
from PyQt6.QtCore import Qt

import nedc_mladp_header_block as hd
from nedc_mladp_display_block import DisplayBlockManager
from nedc_mladp_stats_block import StatsBlockManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initial slected image index.
        #
        self.image_idx = 0

        # Create manager objects
        #
        self.display_block_manager = DisplayBlockManager()
        self.stats_block_manager = StatsBlockManager()

        # Set window properties
        #
        self.setWindowTitle("Machine Learning Applications in Digital Pathology GUI")
        # self.setWindowTitle("Yuan Test GUI")
        self.setGeometry(0, 0, 1600, 900)
        self.setStyleSheet("background-color: #f0d1e1;")

        # Central widget. Holds ALL the page layouts.
        #
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Overall window is scrollable.
        #
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setContentsMargins(20, 20, 20, 20)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        
        # Main layout
        main_layout = QVBoxLayout()
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        

        # Main Window title block -- Displays title.
        #
        block_one = hd.title_block()
        content_layout.addWidget(block_one, 0)  # Stretch factor = 0, no extra space is given

        # Main window menu block -- Displays page buttons.
        #
        block_two, about_button, viewer_button, types_button = hd.menu_block()
        content_layout.addLayout(block_two)

        # Main window page block. -- Displays content based on the page picked in the menu block.
        #
        self.stacked_widget = QStackedWidget()

        self.about_widget = self.create_about_widget()
        self.viewer_widget = self.create_viewer_widget()
        self.types_widget = self.create_types_widget()
        self.more_widget = self.create_more_widget()

        self.stacked_widget.addWidget(self.about_widget)
        self.stacked_widget.addWidget(self.viewer_widget)
        self.stacked_widget.addWidget(self.types_widget)

        content_layout.addWidget(self.stacked_widget)
        content_layout.addStretch(1)

        # Set the central widget layout
        #
        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
        central_widget.setLayout(main_layout)

        # Connect buttons to corresponding pages.
        #
        about_button.clicked.connect(self.show_about)  # About Me button
        viewer_button.clicked.connect(self.show_viewer)   # Viewer button
        types_button.clicked.connect(self.show_types)   # Types button
        
    def create_about_widget(self):
        '''
        Method:
            Displays the content of the 'about' page.

        Returns:
            :about_widget: Widget-Type containing the 'about' content.
        '''

        about_widget = QWidget()
        about_layout = hd.about_block()
        about_widget.setLayout(about_layout)

        return about_widget
    
    def create_viewer_widget(self):
        '''
        Method:
            Displays the content of the 'viewer' page.

        Returns:
            :about_widget: Widget-Type containing the 'viewer' content.
        '''

        viewer_widget = QWidget()
        viewer_layout = QVBoxLayout()

        # Display the viewer
        display_block, self.button_select, self.button_more, self.button_save = self.display_block_manager.display_block()
        viewer_layout.addLayout(display_block)
        viewer_layout.addSpacing(20)

        stats_block = self.stats_block_manager.stats_block()
        viewer_layout.addLayout(stats_block)

        viewer_widget.setLayout(viewer_layout)

        self.button_select.clicked.connect(self.display_selected_item)
        
        return viewer_widget
    
    def create_more_widget(self):
    
        more_widget = QWidget()
        more_layout = QVBoxLayout()
    
        # Display more
        more_block, left_button, right_button = self.display_block_manager.more_block()
        more_layout.addWidget(more_block)
        more_widget.setLayout(more_layout)
        more_widget.hide()

        self.button_more.clicked.connect(self.toggle_more)
        left_button.clicked.connect(self.display_prev_item)
        right_button.clicked.connect(self.display_next_item)

        return more_widget
    
    def create_types_widget(self):
        '''
        Method:
            Displays the content of the 'data types'' page.

        Returns:
            :about_widget: Widget-Type containing the 'data types' content.
        '''
        
        types_widget = QWidget()
        types_layout = QVBoxLayout()
        type_block = hd.type_block()

        types_layout.addLayout(type_block, 0)
        types_layout.addStretch(1)
        types_widget.setLayout(types_layout)

        return types_widget
    
    def show_about(self):
        self.stacked_widget.setCurrentWidget(self.about_widget)

    def show_viewer(self):
        self.stacked_widget.setCurrentWidget(self.viewer_widget)

    def show_types(self):
        self.stacked_widget.setCurrentWidget(self.types_widget)

    def display_selected_item(self):
        self.more_widget.hide()
        self.display_block_manager.display_selected_item()
        if self.display_block_manager.selected_item is not None:
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