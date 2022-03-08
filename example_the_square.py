import main_v2

term = main_v2.TGR()

x = 0
y = 0

def on_event(key):
    global x, y
    if key == term.Key.up:
        print(".")
        y-=1
        term.clear_terminal()
        term.draw_rect(x, y, 10, 5, [250, 250, 60])
    elif key == term.Key.down:
        y+=1
        term.clear_terminal()
        term.draw_rect(x, y, 10, 5, [250, 250, 60])
    elif key == term.Key.right:
        x+=2
        term.clear_terminal()
        term.draw_rect(x, y, 10, 5, [250, 250, 60])
    elif key == term.Key.left:
        x-=2
        term.clear_terminal()
        term.draw_rect(x, y, 10, 5, [250, 250, 60])


term.clear_terminal()
term.init_keyboard(on_press=on_event)
term.draw_rect(x, y, 10, 5, [250, 250, 60])

while True:
    pass
