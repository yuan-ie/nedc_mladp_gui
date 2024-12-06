import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
sys.path.append("/data/isip/exp/tuh_dpath/exp_0289/")
from get_stats import get_stats

from nedc_mladp_histogram import HistogramWidget

class StatsBlockManager:
    def __init__(self):
        self.selected_itemm = None

    def stats_block(self):
        '''
        Method:
            Create the statistics block.
            Contains TP, TN, FP, FN. Can contain more information.
        '''

        stats = QVBoxLayout()

        stats_window = QGroupBox("Model Results")
        stats_window.setStyleSheet("background-color: lightblue;")
        stats_window.setFixedHeight(300)
        stats_window.setAlignment(Qt.AlignmentFlag.AlignCenter)
        stats_window_layout =  QVBoxLayout()

        stats_block_layout = QHBoxLayout()

        # RNF STATS
        rnf_layout = QVBoxLayout()
        rnf_label = QLabel("RNF")
        rnf_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rnf_mini_layout = QHBoxLayout()
        self.rnf_stats = QLabel()
        self.rnf_stats.setFixedWidth(250)
        
        rnf_mini_layout.addWidget(self.rnf_stats)
        self.rnf_histogram = HistogramWidget("RNF Accuracy Histogram")
        rnf_mini_layout.addWidget(self.rnf_histogram,0)
        
        rnf_layout.addWidget(rnf_label,0)
        rnf_layout.addLayout(rnf_mini_layout)
        rnf_layout.addStretch(1)


        # CNN STATS
        cnn_layout = QVBoxLayout()
        cnn_label = QLabel("CNN")
        cnn_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cnn_mini_layout = QHBoxLayout()
        self.cnn_stats = QLabel()
        self.cnn_stats.setFixedWidth(250)
        
        cnn_mini_layout.addWidget(self.cnn_stats)
        self.cnn_histogram = HistogramWidget("CNN Accuracy Histogram")
        cnn_mini_layout.addWidget(self.cnn_histogram,0)
        

        cnn_layout.addWidget(cnn_label,0)
        cnn_layout.addLayout(cnn_mini_layout)
        cnn_layout.addStretch(1)

        stats_block_layout.addLayout(rnf_layout,0)
        stats_block_layout.addLayout(cnn_layout,0)

        stats_window_layout.addLayout(stats_block_layout)
        stats_window.setLayout(stats_window_layout)

        stats.addWidget(stats_window)

        return stats
    
    def display_stats(self, xml_file, cnn_file, rnf_file):
        '''
        method:
            Display the stats of the Machine Learning Model

        args:
            xml_file: original file
            csv_file: predictions file
        '''

        tp,fp,tn,fn, conf_scores, overall_conf = get_stats(ref_fname=xml_file, hyp_fname=cnn_file)
        self.cnn_stats.setText(self.print_numbers(conf_scores, overall_conf))
        self.cnn_histogram.update_data(tp,fp,tn,fn)

        tp,fp,tn,fn, conf_scores, overall_conf= get_stats(ref_fname=xml_file, hyp_fname=rnf_file)
        self.rnf_stats.setText(self.print_numbers(conf_scores, overall_conf))
        self.rnf_histogram.update_data(tp,fp,tn,fn)

    def print_numbers(self, confidence_scores, overall_confidence):
        string = ''
        for label in confidence_scores:
            print(label)
            string += f'{label.upper()}: {confidence_scores[label]:.2f}\n'

        string += f'Overall Confidence: {overall_confidence:.4f}'

        return string
    

    