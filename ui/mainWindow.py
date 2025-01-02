import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFileDialog, QAction,
    QToolBar, QStatusBar, QMessageBox
)
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint
import numpy as np
import cv2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SAM-2 Interactive Digitizer")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel()
        self.setCentralWidget(self.image_label)

        self.image = None
        self.mask = None
        self.last_point = QPoint()
        self.points = []

        self.init_ui()

    def init_ui(self):
        # Create Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # Add Open Action
        open_action = QAction('Open Image', self)
        open_action.triggered.connect(self.open_image)
        file_menu.addAction(open_action)

        # Add Save Action
        save_action = QAction('Save Mask', self)
        save_action.triggered.connect(self.save_mask)
        file_menu.addAction(save_action)

        # Create Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Add Actions to Toolbar
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        # Create Status Bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Images (*.png *.jpg *.bmp *.tif)", options=options)
        if file_name:
            self.image = cv2.imread(file_name)
            self.display_image()
            self.points = []
            self.mask = None
            self.statusBar.showMessage(f"Opened image: {file_name}")

    def save_mask(self):
        if self.mask is None:
            QMessageBox.warning(self, "Warning", "No mask to save.")
            return
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Mask Image", "", "PNG Files (*.png)", options=options)
        if file_name:
            cv2.imwrite(file_name, self.mask)
            self.statusBar.showMessage(f"Saved mask: {file_name}")

