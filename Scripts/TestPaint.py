from PIL import Image
from Sketch.SketchBase import SketchBase

class Test(SketchBase):
    NAME = 'Test'

    def Draw(self):
        # Imageを作成
        image = Image.new('RGB', (600, 600), (255, 255, 255))
        return image
