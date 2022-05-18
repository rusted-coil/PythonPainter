from Sketch.SketchBase import SketchBase

# 長さ1x1の矩形をwidth,height個ずつに分割した状態を表すクラスです。
class GridBox():
    def __init__(self, width, height):
        self.Width = width
        self.Height = height

    # 左上のグリッドを(0,0)とした時のグリッド(x,y)の中心座標を返します。
    def GridCenter(self, x, y):
        return ((x + 0.5)/self.Width, (y+0.5)/self.Height)

class FireBall(SketchBase):
    NAME = '火球フェーズ'

    def __init__(self):
        super().__init__((650, 700), (255, 255, 255))

    def Draw(self):
        field = self.CreateSubArea(75, 75, 575, 575, (200, 200, 200), (100, 100, 100), 2)
        box = GridBox(3, 3)

        # 火球
        ballSize = field.VectorInt((0.25, 0.25))
        self.DrawImage('FF14/fire.png', field.Point(box.GridCenter(0, 0)), ballSize)
#        self.DrawImage('FF14/fire.png', field.Point(box.GridCenter(1, 1)), ballSize)
        self.DrawImage('FF14/fire.png', field.Point(box.GridCenter(2, 2)), ballSize)
#        self.DrawAlphaRectangle(field.Rectangle(1/3, 0, 2/3, 1), (255, 128, 0, 128))
#        self.DrawAlphaRectangle(field.Rectangle(0, 1/3, 1, 2/3), (255, 128, 0, 128))
#        self.DrawAlphaRectangle(field.Rectangle(0, 0, 1, 1/3), (255, 128, 0, 128))
#        self.DrawAlphaRectangle(field.Rectangle(0, 0, 1/3, 1), (255, 128, 0, 128))
        self.DrawAlphaRectangle(field.Rectangle(2/3, 0, 1, 1), (255, 128, 0, 128))
        self.DrawAlphaRectangle(field.Rectangle(0, 2/3, 1, 1), (255, 128, 0, 128))
#        self.DrawTextCentering("①", field.Point(box.GridCenter(1, 1)), (0, 0, 0)) # 1
        self.DrawTextCentering("②", field.Point(box.GridCenter(2, 2)), (0, 0, 0)) # 2
        self.DrawTextCentering("③", field.Point(box.GridCenter(0, 0)), (0, 0, 0)) # 3

        # カータ
        cauterIndex = 2
#        self.DrawAlphaRectangle(field.Rectangle(cauterIndex / 3.0, -0.1, (cauterIndex + 1) / 3.0, 1.1), (0, 0, 255, 128))

        # 安地
#        if cauterIndex == 0:
#            self.DrawCircle((540, 60), 50, fill=None, color=(255, 0, 0), outline=(255, 255, 255), width=4)
#            self.DrawCircle((540, 540), 50, fill=None, color=(255, 0, 0), outline=(255, 255, 255), width=4)
#        else:
#            self.DrawCircle((60, 60), 50, fill=None, color=(255, 0, 0), outline=(255, 255, 255), width=4)
#            self.DrawCircle((60, 540), 50, fill=None, color=(255, 0, 0), outline=(255, 255, 255), width=4)

        # アク・モーン
        self.DrawCircle((95, 95), 75, fill=(255, 150, 150), color=(255, 100, 100), width=6)
        self.DrawCircle((190, 95), 75, fill=(255, 150, 150), color=(255, 100, 100), width=6)
        self.DrawCircle((285, 95), 75, fill=(255, 150, 150), color=(255, 100, 100), width=6)
        self.DrawCircle((285, 190), 75, fill=(255, 150, 150), color=(255, 100, 100), width=6)
#        self.DrawCircle((285, 530), 75, fill=(255, 150, 150), color=(255, 100, 100), width=6)
#        self.DrawCircle((285, 435), 75, fill=(255, 150, 150), color=(255, 100, 100), width=6)

        # 説明
        caption = ["カータライズ【西】", "カータライズ【中】", "カータライズ【東】"]
#        self.DrawTextCentering(caption[cauterIndex], (300, 620), (0, 0, 0))

        return self.Image
