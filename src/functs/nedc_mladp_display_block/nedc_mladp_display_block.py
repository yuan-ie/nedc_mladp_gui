from PyQt6.QtWidgets import QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QGridLayout
from PyQt6.QtGui import QPixmap, QColor, QPalette
from PyQt6.QtCore import Qt
import os

from nedc_mladp_zoom_funct import ImageZoomManager

imagepath = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/original_files/"
imagepath_ANN = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/original_ann_files/"
imagepath_CNN = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/cnn_files/"
imagepath_RNF = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/rnf_files/"

cnn_list_file = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/all_files/cnn_files.list"
rnf_list_file = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/all_files/rnf_files.list"
xml_list_file = "/data/isip/exp/tuh_dpath/exp_0289/Machine-Learning-Applications-In-Digital-Pathology/nedc_mladp/data/yuan_test/all_files/xml_files.list"

class DisplayBlockManager:

    '''
    Class: This controls the graphic display and buttons in the 'Viewer' page.

    Main blocks in the DisplayBlockManager:
        display_block:
            - image_block: displays the selected image from the list.
            - list_block: list of breast tissue images as JPEG.
            - more_block: separate window that displays more graphics of selected image.
            
    '''
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
            Create the display block, which contains the image block and list block.

        Returns:
            :display: Layout-type.
        '''

        # Initializa the layout.
        display = QVBoxLayout()
        self.display_layout = QHBoxLayout()
        self.display_layout.setSpacing(30)  # Space between buttons

        # Split this block in two layouts.
        image_block = self.image_block()
        list_block, button_select, button_more, button_save = self.list_block()

        self.display_layout.addWidget(image_block)
        self.display_layout.addLayout(list_block)
        display.addLayout(self.display_layout)

        return display, button_select, button_more, button_save

    def image_block(self):
        '''
        Method:
            Create the image block -- the left side of display block.

        Returns:
            :image_window: Layout-type.
        '''

        # Initialize the image window within the 'Viewer' page.
        #
        self.image_window = QGroupBox("Image Window")
        self.image_window.setStyleSheet("background-color: lightblue;")
        self.image_window.setFixedSize(900, 430)

        # Default text for no image.
        #
        self.image_label = QLabel("No Image Selected.")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("font-size: 16px; font-style: italic;")

        # Add the elements to the image layout.
        #
        self.image_layout = QVBoxLayout()
        self.image_layout.addWidget(self.image_label)
        self.image_window.setLayout(self.image_layout)

        return self.image_window

    def list_block(self):
        '''
        Method:
            Create the list block -- the left side of display block.
            List of images to choose from.
            Buttons to select image, display more information, and save image.

        Returns:
            :list_layout: Layout-type. Contains both scrollable list and buttons.
            :button_select: ButtonWidget-Type.
            :button_more: ButtonWidget-Type.
            :button_save: ButtonWidget-Type.
        '''

        # List block layout.
        #
        self.list_layout = QVBoxLayout()
        list_widget = self.image_list()

        # Button layout.
        #
        buttons = QHBoxLayout()
        button_select = QPushButton("Select")
        button_more = QPushButton("More")
        button_save = QPushButton("Save")
        buttons.addWidget(button_select)
        buttons.addWidget(button_more)
        buttons.addWidget(button_save)

        # Add the elements to the list block layout.
        #
        self.list_layout.addWidget(list_widget)
        self.list_layout.addLayout(buttons)

        return self.list_layout, button_select, button_more, button_save
    
    def track_selection(self, item):
        '''
        Method:
            Track the selection of the item in the scrollable list.
        '''

        self.selected_item = item

    def display_selected_item(self):
        '''
        Method:
            Display the selected item from the list (when the 'select' button is clicked).
            Display the original image (no annotations).
        '''

        # If an image was selected:
        #
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
                image_path = self.selected_image_list(0)
                self.more_title.setText(self.image_title)
                self.image_zoom_manager.update_image(image_path)

            else:
                pass

        elif self.selected_item is None:
            self.image_label.setText("No item selected. Please select an item first.")

    def more_block(self):
        '''
        Method:
            This method activates for each 'more' button click.
            Creates a new window with the layout of title, image, buttons, and legend.
            Starts off with the original image that is selected.

        Returns:
            :more_block: Widget-Type that contains the whole 'more' window layout.
            :left_button: ButtonWidget-Type.
            :right_button: ButtonWidget-Type.
        '''

        # Overall 'more' window containing the overall layout.
        #
        more_window = QGroupBox()
        more_window.setStyleSheet("background-color: lightblue;")
        more_window.setGeometry(20, 20, 900, 800)
        more_window.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Overall layout containing the 'more' functions.
        #
        more_layout =  QVBoxLayout()

        # Title of the toggled image in the 'more' window'.
        #
        self.more_title = QLabel()
        self.more_title.setText("Original Biopsy Slide")
        self.more_title.setFixedHeight(20)
        self.more_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.more_title.setStyleSheet("font-size: 16px;") # font-weight: bold;

        # Legend of the 'more' window.
        #
        self.more_legend = self.legend_chart()
        self.more_legend.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Toggled image of the 'more' window'. Has the zoom and drag functionality.
        #
        self.more_image = QVBoxLayout()
        self.more_image.addWidget(self.image_zoom_manager)
        self.more_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Previous and Next buttons for the 'more' window.
        #
        more_buttons = QHBoxLayout()
        left_button = QPushButton("Previous")
        left_button.setFixedSize(100,100)
        right_button = QPushButton("Next")
        right_button.setFixedSize(100,100)
        more_buttons.addWidget(left_button)
        more_buttons.addWidget(right_button)
        more_buttons.addWidget(self.more_legend)

        # Add all components to the layout and add layout to the 'more' block.
        #
        more_layout.addWidget(self.more_title,0)
        more_layout.setSpacing(10)
        more_layout.addLayout(self.more_image)
        more_layout.setSpacing(30)
        more_layout.addLayout(more_buttons)
        more_layout.addStretch(1)
        more_window.setLayout(more_layout)

        return more_window, left_button, right_button
    
    def display_more_items(self, idx):
        '''
        Method:
            Activates when 'prev' or 'next' button is clicked.
            Displays the new image within the 'more' window.

        Arguments:
            :idx: Index of the graphic for each image.
                (0) Original Image
                (1) Original Image w/ Annotations
                (2) RNF Predictions
                (3) CNN Predictions
        '''

        # Display image if available.
        #
        if self.selected_item:

            image_path = self.selected_image_list(idx)
            self.pixmap = QPixmap(image_path)
            if not self.pixmap.isNull():

                # Displays the toggled image on the 'more' window.
                #
                self.more_title.setText(self.image_title)
                self.image_zoom_manager.update_image(image_path)
            else:
                pass
        else:
            pass

    def image_list(self):
        '''
        Method:
            Create list of all the image names in the directory (without the whole path).
        
        Returns:
            :list_widget: Scrollable list Widget-Type.
        '''

        # List widget for the scrollable list.
        #
        list_widget = QListWidget()

        # Track the selection when an item is clicked.
        #
        list_widget.itemClicked.connect(self.track_selection)

        # Add all images to list.
        #
        for image in os.listdir(imagepath):
            list_widget.addItem(image)

        return list_widget
    
    def selected_image_list(self, idx):
        '''
        Method:
            Get the next or previous graphic of the selected image.

        Arguments:
            :idx: Index of the graphic for each image.
                (0) Original Image
                (1) Original Image w/ Annotations
                (2) RNF Predictions
                (3) CNN Predictions

        Returns:
            :selected_image[idx]: Indexed image.
        '''

        # Concatanate the file path to the file name.
        #
        image = imagepath + self.image_name
        image_ANN = imagepath_ANN + self.image_name
        image_RNF = imagepath_RNF + self.image_name
        image_CNN = imagepath_CNN + self.image_name

        # Select through the correct file to display.
        #
        selected_image = [image, image_ANN, image_RNF, image_CNN]
        more_image_title = ["Biopsy Slide", "Pathologist Annotations", "RNF Predictions", "CNN Predictions"]
        self.image_title = more_image_title[idx]

        return selected_image[idx]
    
    def get_filenames(self):
        '''
        Method:
            Get the whole XML, CSV (CNN), and CSV (RNF) filepaths of the selected image.
            These paths are to be used by the stats block to display accuracies.

        Returns:
            :original_xml_file: XML file.
            :cnn_pred_file: CSV file.
            :rnf_pred_file: CSV file.
        '''
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