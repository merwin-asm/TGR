
# pyTGR3
[![Downloads](https://static.pepy.tech/personalized-badge/pytgr?period=total&units=international_system&left_color=blue&right_color=orange&left_text=Downloads)](https://pepy.tech/project/pytgr)

<p align="right"> <img src="https://komarev.com/ghpvc/?username=meriwn-TGR&label=Project%20views&color=0e75b6&style=flat" alt="darkmash-org" /> </p>
A minimal lib for rendering things on Terminal.


## Installation

Install pyTGR with pip

```bash
  pip install pyTGR
```
    
## Features

- Cross platform (i think).
- Loading animations.
- Print Image / Video  on terminal.
- Key Events
- Terminal Events (like when the terminal is resized and the cursor position changes).
- Print History.
- And some Terminal related functions.
- Examples provided.
## Usage/Examples

```python
import pyTGR
renderer = pyTGR.pyTGR()
```

Terminal Related Functions:
```python
    def set_bg(self, bg):
             """
        For setting the bg color.
        :param bg: rgb color code
        :return: None
        """
    def get_terminal_size(self):
          """
        Returns the terminal size ,[cols , lines]
        :return: Size [ cols , lines ]
        """
    def set_cursor(self, x, y):
          """
        Move the terminal cursor to a given position.
        :param x: x - position.
        :param y: y - position.
        :return: None
        """
    def get_cursor_pos(self):
        """
        Returns the position of the cursor.
        :return: Position
        """
    def clear_terminal(self):
           """
        Used for clearing the terminal.
        :return: None
        """
    def close_terminal(self):
          """
        Used to close the terminal.
        :return: None
        """
```

Printing Related Functions:

```python
    def print(self, data, end="\n"):
        """
        Prints str
        :param data: str , the str to be printed.
        :param end: The end param for printing. By default '\n'
        :return: None
        """
    def text(self, text, fg_, bg_):
        """
        Print Text , with fg and bg color.
        :param text:Text to be printed.
        :param fg_: Foreground color rgb.
        :param bg_: Background color rgb.
        :return: None
        """
    def new_row(self):
        """
        Move to a new row.
        :return: None
        """
    def updating_text(self, txt, color=[255, 255, 255], bg_=[0, 0, 0]):
        """
        A text which can be changed.
        :param txt: Primary text.
        :param color: Foreground color rgb.
        :param bg_: Background color rgb.
        :return: None
        """
    def fixed_text(self, txt, bg_, fg_, x, y):
        """
        Text which can be fixed a position , and doesn't get removed by the clear func.
        :param txt: Test to be saved.
        :param bg_: background color rgb.
        :param fg_: foreground color rgb.
        :param x: x - position.
        :param y: y - position.
        :return: None
        """
    def remove_fixed_text(self, txt):
        """
        To remove a text from fixed texts.
        :param txt: The text which is to be removed.
        :return: None
        """
        ```

Drawing Related Functions:
```python
    def draw_vertical_pixel(self, color):
        """
        Print a pixel , vertically.
        :param color: Color of the pixel , rgb .
        :return: None
        """
    def draw_horizontal_pixel(self, color):
        """
        Print a pixel , horizontally.
        :param color: Color: Color of the pixel , rgb .
        :return: None
        """
    def draw_pixel(self, x, y, color):
        """
        Print a pixel , at a given position.
        :param x: x - position.
        :param y: y - position.
        :param color: Color of the pixel.
        :return: None
        """
    def draw_line(self, x, y, width, color):
        """
        To draw a line.
        :param x: x  - position
        :param y: y - position
        :param width: width of the line.
        :param color: Color of the line , rgb.
        :return: None
        """
    def draw_circle(self, diameter, color):
        """
        To draw a circle.
        :param diameter: The diameter of the circle.
        :param color: color of the circle , rgb.
        :return: None
        """
    def draw_rect(self, x, y, width, height, color, filled=True):
        """
        To draw rectangle.
        :param x: x - position.
        :param y: y - position.
        :param width: width of the rectangle.
        :param height: height of the rectangle.
        :param color: color of the rectangle , rgb.
        :param filled: If the rectangle should be filled. (optional)
        :return: None
        """
```

Event Related Functions:
```python
    def init_terminal_events(self, function):
        """
        To monitor Terminal events.
        Types of events:
            change in size: size
            change in cursor position : cursor
        :param function: A function which will be called on events ,event will be passed as an argument.
        :return: None
        """
    def init_keyboard(self, on_press):
        """
        To monitor Keyboard events.
        :param on_press: The function to be called if a key is pressed ,key will be passed as an argument.
        :return: None
        """
# pyTGR.Key returns the keys
# This can be seen in the example given (square movement)
```

Loading Animations:
```python
    def spinning_animation_bars(self, revolutions, delay, side_text=" Loading...", color=[255, 255, 255]):
        """
        Animation : spinning - 1.
        :param revolutions: Times.
        :param delay: The delay between the change of each symbol.
        :param side_text: The text about the animation.
        :param color: The color of the bars in rgb.
        :return: None
        """
    def spinning_animation(self, delay, revolutions, side_text=" Loading...", color=[255, 255, 255]):
        """
        Animation : spinning - 2.
        :param delay: The delay between the change of each symbol.
        :param revolutions: Times.
        :param side_text: The text about the animation.
        :param color: The color of the symbols in rgb.
        :return: None
        """
    def bar_animation(self, delay, len_, color_1=[47, 152, 237], color_2=[96, 96, 97],
                      finished_text="Finished Loading..."):
        """
        Animation : Bar
        :param delay: Delay between each bar.
        :param len_: Number of bars.
        :param color_1: Color in rgb.
        :param color_2: color in rgb.
        :param finished_text: The text on finishing.
        :return: None
        """
   def strip_animation(self, duration, strips, finished_text="Loaded...", color=[255, 255, 255]):
        """
        Animation - Strip.
        :param duration: delay between each strip.
        :param strips: number of strips.
        :param finished_text: The text on finishing.
        :param color: color of the strips.
        :return: None
        """
    def loading_percentage(self, delay, max_percent=100, color=[255, 255, 255]):
        """
        Animation - progressive.
        :param delay: The delay between each progress.
        :param max_percent: The max. (optional)
        :param color: The color of the loader. (optional)
        :return: None
        """
```

Image/Video Functions:
```python
    def print_img_color(self, file, print_size=2, resize_img=None, print_img=True):
        """
        For printing a img.
        :param file: File name.
        :param print_size: The size of the print. (optional)
        :param resize_img: The size to which the image have to be resized. (optional)
        :param print_img: If you want to print the image. (optional)
        :return: Image_string
        """
    def play_video_color(self, path, frame_delay=0.09, size=None, reduce_by=None):
        """
        Play video.
        :param path: The path of the video.
        :param frame_delay: The delay between each frame, int. (optional)
        :param size: The of the video played. (optional)
        :param reduce_by: The ratio by which the video size should be reduced. (optional)
        :return: None
        """
    def play_video_ascii(self, path, frame_delay=0.09, size=None):
        """
        To play a video in ascii form.
        :param path: The path of the video.
        :param frame_delay: The delay between each frame, int. (optional)
        :param size: The size of the video played. (optional)
        :return: None
        """
    def print_image_ascii(self, path, size=None, print_=True):
        """
        Print an image as ascii.
        :param path: The path of the image.
        :param size: The size of the image to be printed in.(optional)
        :param print_: The printing of image , bool.(optional)
        :return: The ascii image.
        """
```

### Terminal History:
This Feature can be used to get what all have been printed in
the terminal before , delete it , update it with new bg.. 
This will only work if you replace the real print statement with the print
statement provided by the pyTGR class.


```python
    def clear_history(self):
        """
        Clears the History of Terminal.
        :return: None
        """
    def update_from_history(self):
        """
        Refresh the terminal's bg. Uses the data stored in Terminal History.
        :return: None
        """
# pyTGR.term_history , can be used to access the terminal history.
```
## Examples Provided:
Examples are provided in the Examples class.

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@Merwin](https://www.github.com/mastercodermerwin)

