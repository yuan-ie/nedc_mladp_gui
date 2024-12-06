from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox, QListWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


def menu_block():
    '''
    Block two:
        contains buttons and search: About, All Data, and Search
    '''
    
    # Create the second block
    block_two = QVBoxLayout()

    # Horizontal Layout for buttons
    button_layout = QHBoxLayout()
    button_layout.setContentsMargins(40, 10, 40, 10)
    button_layout.setSpacing(50)  # Space between buttons
    
    # Create buttons with rounded corners
    button1 = QPushButton("About")
    button2 = QPushButton("Viewer")
    button3 = QPushButton("Data Types")
    
    # Add buttons to the layout
    button_layout.addWidget(button1)
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)

    # Add to layout
    block_two.addLayout(button_layout)

    return block_two, button1, button2, button3

def title_block():
    '''
    Block one:
        displays only the title of the window -- center-aligned.
    '''
    title_label = QLabel("Biopsy Slide Viewer")
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_label.setStyleSheet("font-size: 24px;") # font-weight: bold;
    return title_label

def type_block():

    bckg_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/bckg.png")
    norm_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/norm.png")
    artf_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/artf.png")
    null_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/null.png")
    nneo_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/nneo.png")
    susp_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/susp.png")
    infl_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/infl.png")
    dcis_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/dcis.png")
    indc_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/indc.png")

    type_layout = QVBoxLayout()
    type_layout.setContentsMargins(40, 0, 40, 0) 

    non_cancerous_layout = QVBoxLayout()
    non_cancerous_label = QLabel("Non-cancerous Types")
    non_cancerous_label.setStyleSheet("font-size: 14px; font-weight: bold;")
    non_cancerous_types = QLabel("bckg: Background\nnorm: Normal\nartf: Artificial\nnull: Null\n")
    non_cancerous_types.setStyleSheet("font-size: 14px;")

    non_cancerous_picture_group = QHBoxLayout()

    non_cancerous_bckg_group = QVBoxLayout()
    bckg_text = QLabel('bckg')
    bckg_image = QLabel()
    bckg_image.setFixedSize(100,100)
    bckg_image.setPixmap(bckg_pixmap)
    non_cancerous_bckg_group.addWidget(bckg_text)
    non_cancerous_bckg_group.addWidget(bckg_image)
    non_cancerous_picture_group.addLayout(non_cancerous_bckg_group)

    non_cancerous_norm_group = QVBoxLayout()
    norm_text = QLabel('norm')
    norm_image = QLabel()
    norm_image.setFixedSize(100,100)
    norm_image.setPixmap(norm_pixmap)
    non_cancerous_norm_group.addWidget(norm_text)
    non_cancerous_norm_group.addWidget(norm_image)
    non_cancerous_picture_group.addLayout(non_cancerous_norm_group)

    non_cancerous_artf_group = QVBoxLayout()
    artf_text = QLabel('artf')
    artf_image = QLabel()
    artf_image.setFixedSize(100,100)
    artf_image.setPixmap(artf_pixmap)
    non_cancerous_artf_group.addWidget(artf_text)
    non_cancerous_artf_group.addWidget(artf_image)
    non_cancerous_picture_group.addLayout(non_cancerous_artf_group)

    non_cancerous_null_group = QVBoxLayout()
    null_text = QLabel('null')
    null_image = QLabel()
    null_image.setFixedSize(100,100)
    null_image.setPixmap(null_pixmap)
    non_cancerous_null_group.addWidget(null_text)
    non_cancerous_null_group.addWidget(null_image)
    non_cancerous_picture_group.addLayout(non_cancerous_null_group)
    non_cancerous_picture_group.addStretch(1)

    non_cancerous_layout.addWidget(non_cancerous_label)
    non_cancerous_layout.addWidget(non_cancerous_types)
    non_cancerous_layout.addLayout(non_cancerous_picture_group)


    #-------------------------------------------------------------

    prob_cancerous_picture_group = QHBoxLayout()

    prob_cancerous_layout = QVBoxLayout()
    prob_cancerous_label = QLabel("Potentially-cancerous Types")
    prob_cancerous_label.setStyleSheet("font-size: 14px; font-weight: bold;")
    prob_cancerous_types = QLabel("nneo: Non-neoplastic\nsusp: Suspicious\ninfl: Inflammation\n")
    prob_cancerous_types.setStyleSheet("font-size: 14px;")

    prob_cancerous_nneo_group = QVBoxLayout()
    nneo_text = QLabel('nneo')
    nneo_image = QLabel()
    nneo_image.setFixedSize(100,100)
    nneo_image.setPixmap(nneo_pixmap)
    prob_cancerous_nneo_group.addWidget(nneo_text)
    prob_cancerous_nneo_group.addWidget(nneo_image)
    prob_cancerous_picture_group.addLayout(prob_cancerous_nneo_group)

    prob_cancerous_susp_group = QVBoxLayout()
    susp_text = QLabel('susp')
    susp_image = QLabel()
    susp_image.setFixedSize(100,100)
    susp_image.setPixmap(susp_pixmap)
    prob_cancerous_susp_group.addWidget(susp_text)
    prob_cancerous_susp_group.addWidget(susp_image)
    prob_cancerous_picture_group.addLayout(prob_cancerous_susp_group)

    prob_cancerous_infl_group = QVBoxLayout()
    infl_text = QLabel('infl')
    infl_image = QLabel()
    infl_image.setFixedSize(100,100)
    infl_image.setPixmap(infl_pixmap)
    prob_cancerous_infl_group.addWidget(infl_text)
    prob_cancerous_infl_group.addWidget(infl_image)
    prob_cancerous_picture_group.addLayout(prob_cancerous_infl_group)
    prob_cancerous_picture_group.addStretch(1)


    prob_cancerous_layout.addWidget(prob_cancerous_label)
    prob_cancerous_layout.addWidget(prob_cancerous_types)
    prob_cancerous_layout.addLayout(prob_cancerous_picture_group)

    #-------------------------------------------------------------

    cancerous_picture_group = QHBoxLayout()

    cancerous_layout = QVBoxLayout()
    cancerous_label = QLabel("Cancerous Types")
    cancerous_label.setStyleSheet("font-size: 14px; font-weight: bold;")
    cancerous_types = QLabel("dcis: Ductal carcinoma in situ\nindc: Invasive ductal carcinoma\n")
    cancerous_types.setStyleSheet("font-size: 14px;")

    cancerous_dcis_group = QVBoxLayout()
    dcis_text = QLabel('dcis')
    dcis_image = QLabel()
    dcis_image.setFixedSize(100,100)
    dcis_image.setPixmap(dcis_pixmap)
    cancerous_dcis_group.addWidget(dcis_text)
    cancerous_dcis_group.addWidget(dcis_image)
    cancerous_picture_group.addLayout(cancerous_dcis_group)

    cancerous_indc_group = QVBoxLayout()
    indc_text = QLabel('indc')
    indc_image = QLabel()
    indc_image.setFixedSize(100,100)
    indc_image.setPixmap(indc_pixmap)
    cancerous_indc_group.addWidget(indc_text)
    cancerous_indc_group.addWidget(indc_image)
    cancerous_picture_group.addLayout(cancerous_indc_group)
    cancerous_picture_group.addStretch(1)


    cancerous_layout.addWidget(cancerous_label)
    cancerous_layout.addWidget(cancerous_types)
    cancerous_layout.addLayout(cancerous_picture_group)

    type_layout.addLayout(non_cancerous_layout)
    type_layout.addSpacing(30)
    type_layout.addLayout(prob_cancerous_layout)
    type_layout.addSpacing(30)
    type_layout.addLayout(cancerous_layout)

    return type_layout

def about_block():

    original_image_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/original_image.png")
    predicted_image_pixmap = QPixmap("/data/isip/exp/pabcc/exp_0001/nedc_mladp_gui/src/functs/nedc_mladp_header_block/example_imgs/example_imgs/predicted_image.png")

    about_layout = QVBoxLayout()  
    about_layout.setContentsMargins(40, 5, 40, 40)  
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
                         
Note*
    ref => annotations
    hyp => predictions
                            """)
    about_label.setStyleSheet("font-size: 14px;")



    picture_group = QHBoxLayout()

    original_image_group = QVBoxLayout()
    original_image_text = QLabel('original image')
    original_image_text.setStyleSheet("font-size: 14px; font-weight: bold;")
    original_image_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
    original_image = QLabel()
    original_image.setFixedSize(500,400)
    original_image.setPixmap(original_image_pixmap.scaled(
        500,
        400,
        Qt.AspectRatioMode.KeepAspectRatio
    ))
    original_image_group.addWidget(original_image_text)
    original_image_group.addWidget(original_image)
    picture_group.addLayout(original_image_group)

    predicted_image_group = QVBoxLayout()
    predicted_image_text = QLabel('predicted image')
    predicted_image_text.setStyleSheet("font-size: 14px; font-weight: bold;")
    predicted_image_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
    predicted_image = QLabel()
    predicted_image.setFixedSize(500,400)
    predicted_image.setPixmap(predicted_image_pixmap.scaled(
        500,
        400,
        Qt.AspectRatioMode.KeepAspectRatio
    ))
    predicted_image_group.addWidget(predicted_image_text)
    predicted_image_group.addWidget(predicted_image)
    picture_group.addLayout(predicted_image_group)

    
    about_layout.addWidget(about_label, 0)
    about_layout.addSpacing(15)
    about_layout.addLayout(picture_group)
    about_layout.addStretch(1)

    return about_layout