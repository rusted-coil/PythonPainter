import tkinter as tk
import tkinter.ttk as ttk

class PainterView:
    def __init__(self, master):
        mainFrame = ttk.Frame(master)
        mainFrame.pack(expand='true', fill='both', side='top')

        # コマンド領域
        commandFrame = ttk.Frame(mainFrame, width=320)
        commandFrame.pack(anchor=tk.NW, side=tk.LEFT, fill=tk.Y)
#        commandFrame.propagate(0)

        self.Buttons = {}
        
        testButton = ttk.Button(commandFrame, text='Reload')
        testButton.pack()
        self.Buttons['Test'] = testButton

        saveButton = ttk.Button(commandFrame, text='Save')
        saveButton.pack()
        self.Buttons['Save'] = saveButton

        # Preview領域
        self.Preview = ttk.Label(mainFrame, padding=10)
        self.Preview.pack(anchor=tk.NW, side=tk.LEFT, ipadx=0)

    # ボタンを押した時の挙動を設定
    def SetButtonCommand(self, id, command):
        self.Buttons[id]['command'] = command

    # Previewにイメージをセット
    def SetPreviewImage(self, image):
        self.PreviewImage = image
        self.Preview['image'] = self.PreviewImage
