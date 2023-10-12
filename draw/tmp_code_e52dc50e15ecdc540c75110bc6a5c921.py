from tkinter import *
from PIL import Image, ImageDraw

class ImageDrawn:
    def __init__(self, master):
        self.master = master
        self.color = "black"
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.draw = ImageDraw.Draw(image)

        self.canvas = Canvas(self.master, width=500, height=500, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.button = Button(text="save", command=self.save)
        self.button.pack()

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.penwidth, fill=self.color,
                                    capstyle=ROUND, smooth=True)

            self.draw.line([self.old_x, self.old_y, event.x, event.y],
                           fill=self.color, width=self.penwidth)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def save(self):
        filename = "image.png"
        image.save(filename)

if __name__ == "__main__":
    root = Tk()
    image = Image.new("RGB", (500, 500), "white")
    ImageDrawn(root)
    root.mainloop()