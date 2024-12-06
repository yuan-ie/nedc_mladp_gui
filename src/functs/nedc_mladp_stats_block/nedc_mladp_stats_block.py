from PyQt6.QtWidgets import QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
sys.path.append("/data/isip/exp/tuh_dpath/exp_0289/")
from get_stats import get_stats

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

        rnf_layout = QVBoxLayout()
        rnf_label = QLabel("RNF")
        rnf_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rnf_stats = QLabel()
        rnf_layout.addWidget(rnf_label,0)
        rnf_layout.addWidget(self.rnf_stats,0)
        rnf_layout.addStretch(1)

        cnn_layout = QVBoxLayout()
        cnn_label = QLabel("CNN")
        cnn_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cnn_stats = QLabel()
        cnn_layout.addWidget(cnn_label,0)
        cnn_layout.addWidget(self.cnn_stats,0)
        cnn_layout.addStretch(1)

        # stats_block_layout.addLayout(stats1_layout)
        # stats_block_layout.addLayout(stats2_layout,0)
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
        self.cnn_stats.setText(self.print_numbers(tp,fp,tn,fn, conf_scores, overall_conf))

        tp,fp,tn,fn, conf_scores, overall_conf= get_stats(ref_fname=xml_file, hyp_fname=rnf_file)
        self.rnf_stats.setText(self.print_numbers(tp,fp,tn,fn, conf_scores, overall_conf))

    def print_numbers(self, tp,fp,tn,fn, conf_scores, overall_conf):
        text1 = "True Positives: " + str(tp) + "\nFalse Positives: " + str(fp) + "\nTrue Negatives: " + str(tn) + "\nFalse Negatives: " + str(fn)

        return text1