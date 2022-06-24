from Sketch.SketchBase import SketchBase
import math

# 長さ1x1の矩形をwidth,height個ずつに分割した状態を表すクラスです。
class GridBox():
    def __init__(self, width, height):
        self.Width = width
        self.Height = height

    # 左上のグリッドを(0,0)とした時のグリッド(x,y)の中心座標を返します。
    def GridCenter(self, x, y):
        return ((x + 0.5)/self.Width, (y+0.5)/self.Height)

def PointPolar(center, radius, angleDegrees):
    theta = math.radians(angleDegrees)
    (cx, cy) = center
    return (cx + radius * math.cos(theta), cy - radius * math.sin(theta))
        

class FireBall(SketchBase):
    NAME = '死刻フェーズ'

    def __init__(self):
        super().__init__((650, 650), (255, 255, 255))

    def Draw(self):
        field = self.CreateSubArea(75, 75, 575, 575)

        center = field.Point((0.5, 0.5))
        self.DrawCircle(center, 250, (200, 200, 200), (100, 100, 100), None, 4)
        self.DrawCircle(center, 175, None, (100, 100, 100), None, 3)

        for i in range(48):
            start = PointPolar(center, 175, i * 7.5)
            end = PointPolar(center, 250, i * 7.5)
            self.DrawLine(start, end, (100, 100, 100), 2)

        # フィールドマーカー
        self.DrawImage('FF14/FieldMarker/ce_target_a.png', PointPolar(center, 175, 90), (40, 40))
        self.DrawImage('FF14/FieldMarker/ce_target_1.png', PointPolar(center, 175, 45), (40, 40))
        self.DrawImage('FF14/FieldMarker/ce_target_b.png', PointPolar(center, 175,  0), (40, 40))
        self.DrawImage('FF14/FieldMarker/ce_target_2.png', PointPolar(center, 175, 315), (40, 40))
        self.DrawImage('FF14/FieldMarker/ce_target_c.png', PointPolar(center, 175, 270), (40, 40))
        self.DrawImage('FF14/FieldMarker/ce_target_3.png', PointPolar(center, 175, 225), (40, 40))
        self.DrawImage('FF14/FieldMarker/ce_target_d.png', PointPolar(center, 175, 180), (40, 40))
        self.DrawImage('FF14/FieldMarker/ce_target_4.png', PointPolar(center, 175, 135), (40, 40))

        # サルベ
        self.DrawCircle(PointPolar(center, 230, 180 - 7.5), 40, fill=(255, 255, 255), color=(220, 220, 220), width=4)
        self.DrawCircle(PointPolar(center, 230, 135 - 7.5), 40, fill=(255, 255, 255), color=(220, 220, 220), width=4)
        self.DrawCircle(PointPolar(center, 230,  45 + 7.5), 40, fill=(255, 255, 255), color=(220, 220, 220), width=4)
        self.DrawCircle(PointPolar(center, 230,   0 + 7.5), 40, fill=(255, 255, 255), color=(220, 220, 220), width=4)

        # 散開図
        """
        self.DrawImage('FF14/JobIcon/Gunbreaker.png', PointPolar(center, 230, 180 - 7.5), (40, 40))
        self.DrawImage('FF14/JobIcon/DarkKnight.png', PointPolar(center, 230, 180 + 7.5), (40, 40))
        self.DrawImage('FF14/JobIcon/Astrologian.png', PointPolar(center, 230, 135 - 7.5), (40, 40))
        self.DrawImage('FF14/JobIcon/Scholar.png', PointPolar(center, 230, 225 + 7.5), (40, 40))
        self.DrawImage('FF14/JobIcon/Samurai.png', PointPolar(center, 230, 45 + 7.5), (40, 40))
        self.DrawImage('FF14/JobIcon/Dragoon.png', PointPolar(center, 230, 315 - 7.5), (40, 40))
        self.DrawImage('FF14/JobIcon/Dancer.png', PointPolar(center, 230, 0 + 7.5), (40, 40))
        self.DrawImage('FF14/JobIcon/Summoner.png', PointPolar(center, 230, 0 - 7.5), (40, 40))
        """

        # プレステ
        self.DrawLine(PointPolar(center, 230, 45 + 7.5), PointPolar(center, 230, 225), (255, 128, 0), 3)
        self.DrawLine(PointPolar(center, 230, 135 - 7.5), PointPolar(center, 230, 315), (255, 128, 0), 3)
        self.DrawLine(PointPolar(center, 230, 90), PointPolar(center, 230, 270), (255, 128, 0), 3)
        self.DrawLine(PointPolar(center, 230, 180 - 7.5), PointPolar(center, 230, 0 + 7.5), (255, 128, 0), 3)
        self.DrawImage('FF14/ps_triangle.png', PointPolar(center, 230, 45 + 7.5), (40, 40))
        self.DrawImage('FF14/ps_triangle.png', PointPolar(center, 230, 225), (40, 40))
        self.DrawImage('FF14/ps_square.png', PointPolar(center, 230, 135 - 7.5), (40, 40))
        self.DrawImage('FF14/ps_square.png', PointPolar(center, 230, 315), (40, 40))
        self.DrawImage('FF14/ps_cross.png', PointPolar(center, 230, 90), (40, 40))
        self.DrawImage('FF14/ps_cross.png', PointPolar(center, 230, 270), (40, 40))
        self.DrawImage('FF14/ps_circle.png', PointPolar(center, 230, 180 - 7.5), (40, 40))
        self.DrawImage('FF14/ps_circle.png', PointPolar(center, 230, 0 + 7.5), (40, 40))

        return self.Image
