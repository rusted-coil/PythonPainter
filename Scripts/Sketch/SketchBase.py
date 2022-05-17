from abc import abstractmethod
from PIL import Image, ImageDraw

class SketchBase:
    def __init__(self, size, color):
        self.Image = Image.new('RGBA', size, color)
        self.Drawer = ImageDraw.Draw(self.Image)

    @abstractmethod
    def Draw(self):
        pass

    # 半透明の四角を描画します。
    def DrawAlphaRectangle(self, rect, color):
        subimage = Image.new('RGBA', self.Image.size, (0, 0, 0, 0))
        subdraw = ImageDraw.Draw(subimage)
        subdraw.rectangle(rect, fill=color)
        self.Image = Image.alpha_composite(self.Image, subimage)
