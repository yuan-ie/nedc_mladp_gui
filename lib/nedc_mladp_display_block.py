from PyQt6.QtWidgets import QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QGridLayout
from PyQt6.QtGui import QPixmap, QColor, QPalette
from PyQt6.QtCore import Qt
import os

from nedc_mladp_zoom_funct import ImageZoomManager

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

        # Create the scene
        self.image_zoom_manager = ImageZoomManager()
        self.image_zoom_manager.setFixedSize(800, 550)

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
        self.image_window.setFixedSize(900, 430)
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

            # If the image exists:
            #
            if not self.pixmap.isNull():

                # Displays selected image on the 'Viewer' page of the main window.
                #
                self.image_label.setPixmap(self.pixmap.scaled(
                    self.image_label.width(),
                    self.image_label.height(),
                    Qt.AspectRatioMode.KeepAspectRatio
                ))

                # Displays selected image by default on 'more' window popup.
                #
                image_path = self.more_dummy_list(0)
                self.more_title.setText(self.image_title)
                self.image_zoom_manager.update_image(image_path)

            else:
                # self.image_label.setText("Image not found.")
                # self.more_label.setText("Image not found.")
                # self.image_label.setText("New.")
                # self.more_label.setText("New.")
                pass
        elif self.selected_item is None:
            self.image_label.setText("No item selected. Please select an item first.")

    def display_more(self):
        '''
        Method:
            This method activates for each 'more' button click.
            Creates a new window with the layout of title, image, and buttons.
            Starts off with the original image that is selected.
        '''

        more_layout = QVBoxLayout()
        
        more_window_layout =  QVBoxLayout()

        self.more_window = QGroupBox()
        self.more_window.setStyleSheet("background-color: lightblue;")
        # self.more_window.setFixedSize(900,800)
        self.more_window.setGeometry(20, 20, 900, 800)
        self.more_window.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.more_title = QLabel()
        self.more_title.setText("Original Biopsy Slide")
        self.more_title.setFixedHeight(20)
        self.more_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.more_title.setStyleSheet("font-size: 16px;") # font-weight: bold;

        # Display image
        # self.more_label = QLabel()
        # self.more_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.legend = self.legend_chart()
        self.legend.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.focus_graphic = QVBoxLayout()
        self.focus_graphic.addWidget(self.image_zoom_manager)
        self.focus_graphic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add the previous and next buttons
        more_buttons = QHBoxLayout()
        left_button = QPushButton("Previous")
        left_button.setFixedSize(100,100)
        # left_button.setFixedWidth(100)
        right_button = QPushButton("Next")
        right_button.setFixedSize(100,100)
        # right_button.setFixedWidth(100)
        more_buttons.addWidget(left_button)
        more_buttons.addWidget(right_button)
        more_buttons.addWidget(self.legend)

        more_window_layout.addWidget(self.more_title,0)
        more_window_layout.setSpacing(10)
        more_window_layout.addLayout(self.focus_graphic)
        more_window_layout.setSpacing(30)
        # more_window_layout.addWidget(self.legend, alignment=Qt.AlignmentFlag.AlignCenter)
        more_window_layout.addLayout(more_buttons)

        more_window_layout.addStretch(1)
        self.more_window.setLayout(more_window_layout)

        more_layout.addWidget(self.more_window)

        return more_layout, left_button, right_button
    
    def display_more_items(self, idx):
        '''
        Method:
            Activates when 'prev' or 'next' is clicked.
        '''

        if self.selected_item:

            image_path = self.more_dummy_list(idx)
            self.pixmap = QPixmap(image_path)
            if not self.pixmap.isNull():

                # Displays the toggled image on the 'more' window.
                #
                self.more_title.setText(self.image_title)
                self.image_zoom_manager.update_image(image_path)

            else:
                pass
                # self.more_title.setText("No Image")
                # self.more_label.setText("Image not found.")
        else:
            pass
            # self.more_label.setText("No item selected. Please select an item first.")

    def dummy_list(self):

        # List widget for the scrollable list.
        list_widget = QListWidget()

        list_widget.itemClicked.connect(self.track_selection)
        for image in os.listdir(imagepath):
            list_widget.addItem(image)

        # Add fixed number of items
        # for i in range(20):  # Adjust the number as needed
        #     list_widget.addItem(f"Image {i + 1}")

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
    
    def legend_chart(self):
        grid_box = QGroupBox()
        grid_box.setStyleSheet("background-color: white;")
        grid_box.setFixedWidth(400)
        # grid_box.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bckg_ref, bckg_hyp = "#ff9603", "#ffcb82"
        norm_ref, norm_hyp = "#ffdd00", "#f7eb9e"
        nneo_ref, nneo_hyp = "#ff003c", "#ffa6bb"
        indc_ref, indc_hyp = "#47ff3d", "#b2f2ae"
        dcis_ref, dcis_hyp = "#0877ff", "#a8cfff"
        artf_ref, artf_hyp = "#ff0ff3", "#ffa1fa"
        null_ref, null_hyp = "#9d14ff", "#d294ff"
        infl_ref, infl_hyp = "#17f3ff", "#c4fcff"
        susp_ref, susp_hyp = "#b8ff1f", "#e1faac"

        colors = [
            [bckg_ref, norm_ref, artf_ref, null_ref, susp_ref, infl_ref, nneo_ref, indc_ref, dcis_ref],
            [bckg_hyp, norm_hyp, artf_hyp, null_hyp, susp_hyp, infl_hyp, nneo_hyp, indc_hyp, dcis_hyp]
        ]

        labels = ["bckg", "norm", "artf", "null", "susp", "infl", "nneo", "indc", "dcis"]
        types = ["hyp", "ref"]
        rows, cols = 3, 10

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # grid.setSpacing(1)

        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    if c != 0:
                        box = QLabel()
                        box.setFixedSize(30,20)
                        box.setText(labels[c-1])
                        grid.addWidget(box, r, c)
                else:
                    if c == 0:
                        box = QLabel()
                        box.setFixedSize(30,20)
                        box.setText(types[r-1])
                        grid.addWidget(box, r, c)
                    else:
                        box = QLabel()
                        box.setFixedSize(30,20)
                        pixmap = QPixmap(30,20)
                        pixmap.fill(QColor(colors[r-1][c-1]))
                        box.setPixmap(pixmap)
                        grid.addWidget(box, r, c)
        
        grid_box.setLayout(grid)

        return grid_box