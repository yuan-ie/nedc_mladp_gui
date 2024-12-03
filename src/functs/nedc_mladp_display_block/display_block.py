from PyQt6.QtWidgets import QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os
imagepath = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/original_files/"
imagepath_OG = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/original_ann_files/"
imagepath_CNN = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/cnn_files/"
imagepath_RNF = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/rnf_files/"

cnn_list_file = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/all_files/cnn_files.list"
rnf_list_file = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/all_files/rnf_files.list"
xml_list_file = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/all_files/xml_files.list"

class DisplayBlockManager:
    def __init__(self):
        '''
        Constructor:
            Default to no image selected.
        '''
        self.selected_item = None
        self.pixmap = None
        self.image_title = "No image."
        self.image_name = None

        with open(cnn_list_file, "r") as cnn_files:
            self.cnn_list = [file.strip() for file in cnn_files]

        with open(rnf_list_file, "r") as rnf_files:
            self.rnf_list = [file.strip() for file in rnf_files]

        with open(xml_list_file, "r") as xml_files:
            self.xml_list = [file.strip() for file in xml_files]

    def display_block(self):
        '''
        Method:
            Create the display block.

        Returns:
            :display: display block layout.
        '''

        # Initializa the layout.
        display = QVBoxLayout()
        window_layout = QHBoxLayout()
        window_layout.setSpacing(30)  # Space between buttons

        # Split this block in two layouts.
        window_layout = self.image_block(window_layout)
        window_layout, button_select, button_more, button_save = self.list_block(window_layout)
        display.addLayout(window_layout)

        return display, button_select, button_more, button_save

    def image_block(self, display_window):
        '''
        Method:
            Create the image block -- the left side of display block.

        Args:
            :display_window: display block layout.

        Returns:
            :display_window: display block layout with image block added.
        '''

        # Initialize the image block layout.
        self.image_window = QGroupBox("Image Window")
        self.image_window.setStyleSheet("background-color: lightblue;")
        self.image_window.setFixedSize(400, 300)
        self.image_window_layout = QVBoxLayout()

        # Default text for no image.
        self.image_label = QLabel("No Image Selected.")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("font-size: 16px; font-style: italic;")

        # Add the elements to the display window layout.
        self.image_window_layout.addWidget(self.image_label)
        self.image_window.setLayout(self.image_window_layout)
        display_window.addWidget(self.image_window)

        return display_window

    def list_block(self, display_window):
        '''
        Method:
            Create the list block -- the left side of display block.
            List of images to choose from.
            Buttons to select image, display more information, and save image.

        Args:
            :display_window: display block layout.

        Returns:
            :display_window: display block layout with list block and buttons added.
        '''

        # Initialize the list block layout.
        self.list_layout = QVBoxLayout()

        list_widget = self.dummy_list()

        # Add the buttons.
        buttons = QHBoxLayout()
        button_select = QPushButton("Select")
        button_more = QPushButton("More")
        button_save = QPushButton("Save")
        button_select.clicked.connect(self.display_selected_item)
        buttons.addWidget(button_select)
        buttons.addWidget(button_more)
        buttons.addWidget(button_save)

        self.list_layout.addWidget(list_widget)
        self.list_layout.addLayout(buttons)

        display_window.addLayout(self.list_layout)

        return display_window, button_select, button_more, button_save
    
    def track_selection(self, item):
        self.selected_item = item

    def display_selected_item(self):
        if self.selected_item:
            self.image_name = self.selected_item.text()
            self.image_window.setTitle(self.image_name)
            self.pixmap = QPixmap(imagepath+self.image_name)
            print("directory: ", imagepath)
            print("filename: ", self.image_name)
            if not self.pixmap.isNull():
                self.image_label.setPixmap(self.pixmap.scaled(
                    self.image_label.width(),
                    self.image_label.height(),
                    Qt.AspectRatioMode.KeepAspectRatio
                ))
                more_image_name = self.more_dummy_list(0)
                self.more_title.setText(self.image_title)
                self.pixmap = QPixmap(more_image_name)
                self.more_label.setPixmap(self.pixmap.scaled(
                    self.more_label.width(),
                    self.more_label.height(),
                    Qt.AspectRatioMode.KeepAspectRatio
                ))
            else:
                self.image_label.setText("Image not found.")
        else:
            self.image_label.setText("No item selected. Please select an item first.")

    def display_more(self):
        more_layout = QVBoxLayout()
        more_window_layout =  QVBoxLayout()
        

        self.more_window = QGroupBox()
        self.more_window.setStyleSheet("background-color: lightblue;")
        self.more_window.setFixedSize(600,500)
        self.more_window.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.more_title = QLabel()
        self.more_title.setText("Original Biopsy Slide")
        self.more_title.setFixedHeight(20)
        self.more_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.more_title.setStyleSheet("font-size: 16px;") # font-weight: bold;

        # Display image
        self.more_label = QLabel()
        self.more_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add the previous and next buttons
        more_buttons = QHBoxLayout()
        left_button = QPushButton("Previous")
        left_button.setFixedWidth(100)
        right_button = QPushButton("Next")
        right_button.setFixedWidth(100)
        more_buttons.addWidget(left_button)
        more_buttons.addWidget(right_button)

        more_window_layout.addWidget(self.more_title,0)
        more_window_layout.addWidget(self.more_label)
        more_window_layout.addLayout(more_buttons)
        # more_window_layout.addStretch(1)
        self.more_window.setLayout(more_window_layout)

        more_layout.addWidget(self.more_window)

        return more_layout, left_button, right_button
    
    def display_more_items(self, idx):
        if self.selected_item:
            # self.image_name = self.selected_item.text()

            more_image_name = self.more_dummy_list(idx)
            self.pixmap = QPixmap(more_image_name)
            print(self.pixmap.isNull())
            if not self.pixmap.isNull():
                self.more_title.setText(self.image_title)
                self.more_label.setPixmap(self.pixmap.scaled(
                    self.more_label.width(),
                    self.more_label.height(),
                    Qt.AspectRatioMode.KeepAspectRatio
                ))
            else:
                self.more_title.setText("No Image")
                self.more_label.setText("Image not found.")
        else:
            self.more_label.setText("No item selected. Please select an item first.")

    def dummy_list(self):

        # List widget for the scrollable list.
        list_widget = QListWidget()

        list_widget.itemClicked.connect(self.track_selection)
        for image in os.listdir(imagepath):
            list_widget.addItem(image)

        # Add fixed number of items
        for i in range(20):  # Adjust the number as needed
            list_widget.addItem(f"Image {i + 1}")

        return list_widget
    
    def more_dummy_list(self, idx):
        image = imagepath + self.image_name
        image_OG = imagepath_OG + self.image_name
        image_RNF = imagepath_RNF + self.image_name
        image_CNN = imagepath_CNN + self.image_name
        more_image_list = [image, image_OG, image_RNF, image_CNN]
        more_image_title = ["Original Biopsy Slide", "Original Annotations", "RNF Predictions", "CNN Predictions"]
        self.image_title = more_image_title[idx]
        print(idx, ": ", more_image_list[idx], "| original image: ", self.image_name)

        return more_image_list[idx]
    
    def get_filenames(self):
        file, extension = os.path.splitext(self.image_name)

        for line in self.xml_list:
            if file in line:
                self.original_xml_file = line
    
        for line in self.cnn_list:
            if file in line:
                self.cnn_pred_file = line

        for line in self.rnf_list:
            if file in line:
                self.rnf_pred_file = line

        print("files: ")
        print("  > ", self.original_xml_file)
        print("  > ", self.cnn_pred_file)
        print("  > ", self.rnf_pred_file)

        return self.original_xml_file, self.cnn_pred_file, self.rnf_pred_file