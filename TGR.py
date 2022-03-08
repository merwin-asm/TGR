"""
TGR 2.0.0
Author : Merwin
A module for doing minimal graphic rendering in the terminal.
"""


import time
import os
import cv2
from pynput import keyboard
from subprocess import call
from sty import fg , bg

class TGR:
    def __init__(self):
        self.Key = keyboard.Key
    def draw_vertical_pixel(self,color,):
        print(f"{fg(color[0],color[1],color[2])} {fg.rs}")
    def draw_horizontal_pixel(self,color):
        print(f"{fg(color[0],color[1],color[2])} {fg.rs}",end="")
    def draw_pixel(self,x,y,color):
        pos = "\033[%d;%dH" % (y, x)
        print(pos,end="")
        print(f"{bg(color[0],color[1],color[2])} {bg.rs}",end="")
    def set_cursor(self,x,y):
        pos = "\033[%d;%dH" % (y, x)
        print(f"{pos}",end="")
    def spinning_animation_bars(self,revolutions,delay,side_text=" Loading...",color=[255,255,255]):
        rev = 0
        while rev != revolutions:
            print(f'\r{fg(color[0],color[1],color[2])}\\ {side_text}{fg.rs}',end="")
            time.sleep(delay)
            print(f'\r{fg(color[0],color[1],color[2])}| {side_text}{fg.rs}', end="")
            time.sleep(delay)
            print(f'\r{fg(color[0],color[1],color[2])}/ {side_text}{fg.rs}',end="")
            time.sleep(delay)
            print(f'\r{fg(color[0],color[1],color[2])}| {side_text}{fg.rs}', end="")
            time.sleep(delay)
            rev+=1
    def spinning_animation(self,delay,revolutions,side_text=" Loading...",color=[255,255,255]):
        rev = 0
        while rev != revolutions:
            print(f'\r{fg(color[0],color[1],color[2])}^ {side_text}{fg.rs}', end="")
            time.sleep(delay)
            print(f'\r{fg(color[0],color[1],color[2])}< {side_text}{fg.rs}', end="")
            time.sleep(delay)
            print(f'\r{fg(color[0],color[1],color[2])}> {side_text}{fg.rs}', end="")
            time.sleep(delay)
            print(f'\r{fg(color[0],color[1],color[2])}_ {side_text}{fg.rs}', end="")
            time.sleep(delay)
            rev += 1
    def loading_animation(self,delay,len_,color_1=[47, 152, 237],color_2=[96, 96, 97],finished_text="Finished Loading..."):
        c = 0
        print(f"{bg(color_2[0],color_2[1],color_2[2])} {bg.rs}", end="")
        while c != len_:
            if c%2 == 0:
                print(f"{bg(color_1[0],color_1[1],color_1[2])}  {bg.rs}", end="")
            else:
                print(f"{bg(color_2[0],color_2[1],color_2[2])} {bg.rs}", end="")
            c+=1
            time.sleep(delay)
        if len_%2 != 0:
            print(f"{color_2} ", end="")
        print(f" {finished_text}",end="")
    def strip_animation(self,duration,strips,finished_text="Loaded...",color=[255,255,255]):
        c = 0
        while strips != c:
            print(f"{fg(color[0],color[1],color[2])}|{fg.rs}",end="")
            time.sleep(duration)
            c+=1
        print(f" {finished_text}", end="")
    def new_row(self):
        print("\n")
    def updating_text(self,txt,color=[255,255,255]):
        print(f"\r{fg(color[0],color[1],color[2])} {txt}{fg.rs}",end="")
    def print_image_ascii(self,path,size=None):
        value_dict = {8: '@', 7: '#', 6: 'B', 5: '%', 4: '/', 3: 'a', 2: '-', 1: '.'}
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Making it greyscale
        if  size != None:
            img = cv2.resize(img, size)  # Resizing it
        s = ''
        for row in img:
            for p in row:
                n = 0
                if p < 30:
                    n = 1
                elif p < 50:
                    n = 2
                elif p < 90:
                    n = 3
                elif p < 110:
                    n = 4
                elif p < 150:
                    n = 5
                elif p < 180:
                    n = 6
                elif p < 220:
                    n = 7
                else:
                    n = 8
                s += value_dict[n]
            s += ' \n'
        print(s)
    def play_video_ascii(self,path,frame_delay=0.09,size=None):
        cam = cv2.VideoCapture(path)
        value_dict = {8: '@', 7: '#', 6: 'B', 5: '%', 4: '/', 3: 'a', 2: '-', 1: '.'}
        frame_list = []
        while True:
            res, img = cam.read()
            if res != True:
                break
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Making it greyscale
            if size != None:
                img = cv2.resize(img, size)  # Resizing it
            s = ''
            for row in img:
                for p in row:
                    if p < 30:
                        n = 1
                    elif p < 50:
                        n = 2
                    elif p < 90:
                        n = 3
                    elif p < 110:
                        n = 4
                    elif p < 150:
                        n = 5
                    elif p < 180:
                        n = 6
                    elif p < 220:
                        n = 7
                    else:
                        n = 8
                    s += value_dict[n]
                s += ' \n'
            frame_list.append(s)
        cam.release()

        for e in frame_list:
            print(e)
            time.sleep(frame_delay)
            self.clear_terminal()
    def play_video_color(self,path,frame_delay,size,reduce_by=None):
        frames = self.load_video(path,size,reduce_by)
        for e in frames:
            print(e)
            time.sleep(frame_delay)
            self.clear_terminal()
    def load_video(self,file, size,reduce_by=None):
        frames = []
        cam = cv2.VideoCapture(file)
        while True:
            res, frame = cam.read()
            if res != True:
                break
            if reduce_by != None:
                frame = cv2.resize(frame,(int(frame.shape[0]*reduce_by),int(frame.shape[1]*reduce_by)))
            frames.append(self.print_frame_color(frame, 1, resize_img=size,print_img=False))
        return frames
    def print_frame_color(self,img,print_size=2,resize_img=None,print_img=True,):
        txt = " " * print_size
        file = img
        if resize_img != None:
            file = cv2.resize(file, resize_img)
        final_text = ""
        for y in file:
            for x in y:
                if list(x) != [0, 0, 0]:
                    final_text += f"{bg(x[2], x[1], x[0])}{txt}{bg.rs}"
                else:
                    final_text += txt
            final_text += "\n"
        if print_img:
            print(final_text)
        return final_text
    def loading_percentage(self,delay,max_percent=100,color=[255,255,255]):
        c = 0
        while c != max_percent+1:
            print(f"\r{fg(color[0],color[1],color[2])}[{c}]{self.find_number_of_repetition('0',str(max_percent))*' '}{fg.rs}",end="")
            time.sleep(delay)
            c+=1
    def find_number_of_repetition(self,chr,string):
        c = 0
        for each in string:
            if each == chr:
                c+=1
        return c
    def draw_line(self,x,y,width,color):
        t = 0
        while t != width :
            self.draw_pixel(x,y,color)
            t+=1
            x+=1

    def draw_circle(self,diameter,color):
        radius = diameter / 2 - .5
        r = (radius + .25) ** 2 + 1

        result = ''

        for i in range(diameter):
            y = (i - radius) ** 2
            for j in range(diameter):
                x = (j - radius) ** 2
                if x + y <= r:
                    result = result + f'{bg(color[0], color[1], color[2])}   {bg.rs}'
                else:
                    result = result + '   '
            result = result + '\n'
        print(result)
    def draw_rect(self,x,y,width,height,color,filled=True):
        if filled:
            t = 0
            while height != t:
                self.draw_line(x,y,width,color)
                y+=1
                t+=1
        else:
            t = 0
            while t != height:
                if t == 0:
                    self.draw_line(x,y,width,color)
                elif t == height-1:
                    self.draw_line(x,y,width,color)
                else:
                    self.draw_pixel(x,y,color)
                    self.draw_pixel(x+width-1,y,color)
                y+=1
                t+=1
        print("")
    def print_img_color(self,file, print_size=2, resize_img=None,print_img=True):
        txt = " " * print_size
        file = cv2.imread(file)
        if resize_img != None:
            file = cv2.resize(file, resize_img)
        final_text = ""
        for y in file:
            for x in y:
                if list(x) != [0, 0, 0]:
                    final_text += f"{bg(x[2], x[1], x[0])}{txt}{bg.rs}"
                else:
                    final_text += txt
            final_text += "\n"
        if print_img:
            print(final_text)
        return final_text
    def init_keyboard(self,on_press,):
        listener = keyboard.Listener(
            on_press=on_press,)
        listener.start()
    def clear_terminal(self):
        _ = call('clear' if os.name == 'posix' else 'cls')
    def close_terminal(self):
        _ = call('exit')
x = 2
y = 2
def pressed_2(key):
    global x,y
    if key == key.up:
        y-=1
    elif key == key.down:
        y+=1
    elif key == key.right:
        x+=1
    elif key == key.left:
        x-=1
if __name__ == '__main__':
    renderer = TGR()
    # renderer.loading_animation(0.05,20)
    # renderer.spinning_animation_bars(10,0.09,"  Loading...")
    # renderer.spinning_animation(0.1,10)
    # renderer.strip_animation(0.01,100)
    # renderer.loading_percentage(0.1,max_percent=50)
    # renderer.clear_terminal()
    # renderer.set_cursor(50,5)
    # renderer.draw_pixel(10,10,color=[255,0,0])
    # renderer.draw_line(10,10,60,color=[0,244,11])
    # renderer.draw_rect(10,10,20,20,color=[0,244,11])

    # drawing a pattern
    # renderer.draw_rect(10,10,10,10,color=[0,244,11],filled=False)
    # time.sleep(3)
    # renderer.clear_terminal()
    # renderer.draw_rect(1,1,10,10,color=[0,244,11])
    # time.sleep(3)
    # renderer.set_cursor(30,30)
    # renderer.new_row()
    # renderer.loading_animation(0.05,20,)
    # renderer.clear_terminal()
    # renderer.draw_circle(10,[100,100,100])
    # time.sleep(5)
    # renderer.clear_terminal()


    # keyboad events
    # def on_event(key):
        # print(key)
    # renderer.init_keyboard(on_press=on_event)
    # renderer.loading_percentage(0.5)

    # print image ascii
    # renderer.print_image_ascii("python3.jpg")
    # time.sleep(5)
    # renderer.clear_terminal()

    #print image color
    # renderer.print_img_color("python3.jpg",print_size=1,resize_img=(100,100))
    # time.sleep(5)
    # renderer.clear_terminal()


    # play video ascii
    # renderer.play_video_ascii("test_video.mp4",size=(100,100))

    # play video color
    # renderer.play_video_color("test_video.mp4",frame_delay=0.09 ,size=(50,50), reduce_by=1/2)

    # renderer.close_terminal()
