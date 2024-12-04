import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QWheelEvent, QMouseEvent
from PyQt6.QtCore import Qt, QRectF

class ImageZoomManager(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Create a scene and add empty pixmap
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Enable transformations
        # self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        # self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

        self.image_item = None

        # Variables for zoom
        self.zoom_factor = 1.2
        self.current_zoom = 1.0

    def update_image(self, image_path):
        '''
        Method:
            Update the image on the graphics scene to allow zoom capability.
        '''
        pixmap = QPixmap(image_path)
        self.scene.clear()
        self.image_item = self.scene.addPixmap(pixmap.scaled(
            600,
            500,
            Qt.AspectRatioMode.KeepAspectRatio
        ))
        self.setSceneRect(self.image_item.boundingRect())

        self.reset_zoom()

    def reset_zoom(self):
        self.resetTransform()
        self.current_zoom = 1.0
        self.centerOn(self.image_item)

    def ensure_bounds(self):
        """
        Ensures the image doesn't go out of bounds.
        """
        if not self.image_item:
            return

        # Get the visible rectangle in scene coordinates
        view_rect = self.mapToScene(self.viewport().rect()).boundingRect()
        scene_rect = self.sceneRect()

        # Calculate the offset needed to stay within bounds
        x_offset = 0
        y_offset = 0

        if view_rect.left() < scene_rect.left():
            x_offset = scene_rect.left() - view_rect.left()
        elif view_rect.right() > scene_rect.right():
            x_offset = scene_rect.right() - view_rect.right()

        if view_rect.top() < scene_rect.top():
            y_offset = scene_rect.top() - view_rect.top()
        elif view_rect.bottom() > scene_rect.bottom():
            y_offset = scene_rect.bottom() - view_rect.bottom()

        # Adjust the view to correct the bounds
        if x_offset != 0 or y_offset != 0:
            self.translate(x_offset, y_offset)

    def wheelEvent(self, event:QWheelEvent):
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def zoom_in(self):
        if self.current_zoom < 10.0:
            self.scale(self.zoom_factor, self.zoom_factor)
            self.current_zoom *= self.zoom_factor
            self.ensure_bounds()  # Ensure bounds after zoom

    def zoom_out(self):
        if self.current_zoom > 0.1:
            self.scale(self.zoom_factor, self.zoom_factor)
            self.current_zoom /= self.zoom_factor
            self.ensure_bounds()  # Ensure bounds after zoom

    def mouseReleaseEvent(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)
        self.ensure_bounds()