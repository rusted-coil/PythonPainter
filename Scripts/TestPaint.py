from PIL import Image, ImageDraw
from Sketch.SketchBase import SketchBase

class SubRect:
    def __init__(self, left, top, right, bottom):
        self.Left = left
        self.Top = top
        self.Right = right
        self.Bottom = bottom

    def Fill(self):
        return (self.Left, self.Top, self.Right, self.Bottom)

    def Rectangle(self, rLeft, rTop, rRight, rBottom):
        return (self.Left + (self.Right - self.Left) * rLeft,
                self.Top + (self.Bottom - self.Top) * rTop,
                self.Left + (self.Right - self.Left) * rRight,
                self.Top + (self.Bottom - self.Top) * rBottom)

class Test(SketchBase):
    NAME = 'Test'

    def __init__(self):
        super().__init__((600, 600), (255, 255, 255))

    def Draw(self):
        battleRect = SubRect(50, 50, 550, 550)
        self.Drawer.rectangle(battleRect.Fill(), fill=(200, 200, 200, 255))

        # カータ
        cauterIndex = 1
        self.DrawAlphaRectangle(battleRect.Rectangle(cauterIndex / 3.0, -0.1, (cauterIndex + 1) / 3.0, 1.1), (0, 0, 255, 128))

        return self.Image
