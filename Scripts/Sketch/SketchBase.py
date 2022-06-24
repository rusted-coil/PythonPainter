from abc import abstractmethod
from PIL import Image, ImageDraw, ImageFont

class SubRect:
    def __init__(self, left, top, right, bottom):
        self.Left = left
        self.Top = top
        self.Right = right
        self.Bottom = bottom

    def Fill(self):
        return (self.Left, self.Top, self.Right, self.Bottom)

    def Point(self, point):
        (x, y) = point
        return (self.Left + (self.Right - self.Left) * x, self.Top + (self.Bottom - self.Top) * y)

    def VectorInt(self, vector):
        (x, y) = vector
        return (int((self.Right - self.Left) * x), int((self.Bottom - self.Top) * y))

    def Rectangle(self, rLeft, rTop, rRight, rBottom):
        return (self.Left + (self.Right - self.Left) * rLeft,
                self.Top + (self.Bottom - self.Top) * rTop,
                self.Left + (self.Right - self.Left) * rRight,
                self.Top + (self.Bottom - self.Top) * rBottom)

class SketchBase:
    def __init__(self, size, color):
        self.Image = Image.new('RGBA', size, color)
        self.Drawer = ImageDraw.Draw(self.Image)
        self.Font = ImageFont.truetype('../Fonts/ZenMaruGothic-Regular.ttf', 30)

    @abstractmethod
    def Draw(self):
        pass

    # サブ領域を生成します。
    def CreateSubArea(self, left, top, right, bottom, color = None, outline=(0, 0, 0), width=0):
        rect = SubRect(left, top, right, bottom)
        if not color is None:
            self.Drawer.rectangle(rect.Fill(), fill=color, outline=outline, width=width)
        return rect

    # 線を描画します。
    def DrawLine(self, start, end, color, width = 0):
        (sx, sy) = start
        (ex, ey) = end
        self.Drawer.line((sx, sy, ex, ey), fill=color, width=width)

    # 半透明の四角を描画します。
    def DrawAlphaRectangle(self, rect, color, outline=(0, 0, 0), width=0):
        subimage = Image.new('RGBA', self.Image.size, (0, 0, 0, 0))
        subdraw = ImageDraw.Draw(subimage)
        subdraw.rectangle(rect, fill=color, outline=outline, width=width)
        self.Image = Image.alpha_composite(self.Image, subimage)
        self.Drawer = ImageDraw.Draw(self.Image)

    # ◯を描画します。
    def DrawCircle(self, center, radius, fill=None, color=None, outline=None, width=0):
        (x, y) = center
        if not outline is None: # アウトライン描画
            self.Drawer.ellipse((x-radius-2, y-radius-2, x+radius+2, y+radius+2), fill=fill, outline=outline, width=width+4)
            self.Drawer.ellipse((x-radius, y-radius, x+radius, y+radius), fill=None, outline=color, width=width)
        else:
            self.Drawer.ellipse((x-radius, y-radius, x+radius, y+radius), fill=fill, outline=color, width=width)

    # 文字を中央揃えして表示します。
    def DrawTextCentering(self, text, position, color):
        (x, y) = position
        (w, h) = self.Drawer.textsize(text, font=self.Font)
        self.Drawer.text((x-w/2.0, y-h/2.0), text, color, font=self.Font)

    # 画像を合成します。
    def DrawImage(self, path, center, size):
        (x, y) = center
        (w, h) = size
        image = Image.open(path)
        image = image.resize(size)
        self.Image.paste(image, (int(x-w/2), int(y-h/2)), mask=image)
