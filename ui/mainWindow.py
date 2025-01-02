import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFileDialog, QAction,
    QToolBar, QStatusBar, QMessageBox
)
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint
import numpy as np
# import cv2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SAM Interactive Digitizer")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel()
        self.setCentralWidget(self.image_label)

        self.image = None
        self.mask = None
        self.last_point = QPoint()
        self.points = []

        # self.init_ui()

    # def init_ui(self):
    #     # Create Menu Bar
    #     menubar = self.menuBar()
    #     file_menu = menubar.addMenu('File')

    #     # Add Open Action
    #     open_action = QAction('Open Image', self)
    #     open_action.triggered.connect(self.open_image)
    #     file_menu.addAction(open_action)

    #     # Add Save Action
    #     save_action = QAction('Save Mask', self)
    #     save_action.triggered.connect(self.save_mask)
    #     file_menu.addAction(save_action)

    #     # Create Toolbar
    #     toolbar = QToolBar()
    #     self.addToolBar(toolbar)

    #     # Add Actions to Toolbar
    #     toolbar.addAction(open_action)
    #     toolbar.addAction(save_action)

    #     # Create Status Bar
    #     self.statusBar = QStatusBar()
    #     self.setStatusBar(self.statusBar)

    # ... (Additional methods will be added here)
