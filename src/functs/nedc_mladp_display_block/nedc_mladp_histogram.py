import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PyQt6.QtGui import QColor

class HistogramWidget(QWidget):
    def __init__(self, label):
        super().__init__()
        # self.setWindowTitle("")
        # self.resize(400,500)

        # categories
        self.categories = ["TP", "FP", "TN", "FN"]

        # Initialize histogram data
        self.counts = [0,0,0,0]
        # self.counts = [5,10,70,100]

        bar_set = QBarSet("")
        bar_set.append(self.counts)

        self.bar_series = QBarSeries()
        self.bar_series.append(bar_set)
        # self.bar_series.setVisible(False)

        self.chart = QChart()
        self.chart.addSeries(self.bar_series)
        self.chart.setTitle(label)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.axis_x.setTitleText("Accuracy")

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("Measure")
        self.axis_y.setRange(0, 100)

        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.chart.legend().setVisible(False)

        # Attach the axes to the bar series
        self.bar_series.attachAxis(self.axis_x)
        self.bar_series.attachAxis(self.axis_y)
        
        # Create a QChartView to display the chart and set it as the central widget
        self.chart_view = QChartView(self.chart)
        self.chart_view.setFixedSize(450, 250)

        # Set up layout for the widget
        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)  # Add chart to layout
        self.setLayout(layout)

    def update_data(self, tp, fp, tn, fn):

        self.counts = [tp, fp, tn, fn]
        bar_set = QBarSet("")
        bar_set.append(self.counts)
        bar_set.setColor(QColor(230, 161, 187))  # Red for the first bar

        self.bar_series.clear()
        self.bar_series.append(bar_set)
        # self.bar_series.setVisible(False)

        # Refresh the chart
        self.chart.update()

        self.chart_view.repaint()