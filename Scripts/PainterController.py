import datetime
from PIL import ImageTk

import ClassUtil
from Sketch.SketchBase import SketchBase

class PainterController:
    def __init__(self, view):
        self.View = view
        self.TestModule = None

        # Viewのボタンに処理を紐づけ
        view.SetButtonCommand('Test', self.TestCommand)
        view.SetButtonCommand('Save', self.Save)

    def TestCommand(self):
        cls = ClassUtil.TryGetNamedClass('FF14.FireBall', SketchBase)
        if cls is None:
            print("No SketchBase Class Found")
        else:
            instance = cls()
            self.Image = instance.Draw()
            self.View.SetPreviewImage(ImageTk.PhotoImage(image = self.Image))

    def Save(self):
        self.Image.save(datetime.datetime.now().strftime('../Output/%Y%m%d_%H%M%S.png'))
