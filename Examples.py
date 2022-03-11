from pyTGR3 import pyTGR


class Examples:
    def __init__(self):
        pass
    def Video_Image(self):
        """
        A video and Image viewer made in pyTGR3.
        :return: None
        """
        term = pyTGR()
        term.print("Photo and Video on Terminal...")
        term.print("Stop to end the program...")
        cmd = ""
        while True:
            cmd = input("Command (stop,image,video) > ").lower()
            if cmd == "stop":
                break
            try:
                if cmd == "image":
                    f = input("File name : ")
                    t = input("color or ascii : ").lower()
                    if t == "color":
                        term.print_img_color(f, resize_img=(100, 100))
                    else:
                        term.print_image_ascii(f, size=(100, 100))
                else:
                    f = input("File name : ")
                    t = input("color or ascii : ").lower()
                    if t == "color":
                        term.play_video_color(f, size=(100, 100))
                    else:
                        term.play_video_ascii(f, size=(100, 100))
            except:
                term.print("Some Error Occurred..")
    def Square_movement(self):
        """
        Moving a square on terminal using keys...
        :return: None
        """
        self.term = pyTGR()

        self.x = 0
        self.y = 0


        self.term.clear_terminal()
        self.term.init_keyboard(on_press=self.on_event)
        self.term.draw_rect(x, y, 10, 5, [250, 250, 60])

        while True:
            pass

    def on_event(self,key):
        """
        Used as a part of Square movement example.
        :return: None
        """
        if key == self.term.Key.up:
            self.y -= 1
            self.term.clear_terminal()
            self.term.draw_rect(self.x, self.y, 10, 5, [250, 250, 60])
        elif key == self.term.Key.down:
            self.y += 1
            self.term.clear_terminal()
            self.term.draw_rect(self.x, self.y, 10, 5, [250, 250, 60])
        elif key == self.term.Key.right:
            self.x += 2
            self.term.clear_terminal()
            self.term.draw_rect(self.x, self.y, 10, 5, [250, 250, 60])
        elif key == self.term.Key.left:
            self.x -= 2
            self.term.clear_terminal()
            self.term.draw_rect(self.x, self.y, 10, 5, [250, 250, 60])
