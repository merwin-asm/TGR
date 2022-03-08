import main_v2


term = main_v2.TGR()

print("Photo and Video on Terminal...")
print("Stop to end the program...")

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
                term.print_img_color(f,resize_img=(100,100))
            else:
                term.print_image_ascii(f,size=(100,100))
        else:
            f = input("File name : ")
            t = input("color or ascii : ").lower()
            if t == "color":
                term.play_video_color(f, size=(100, 100))
            else:
                term.play_video_ascii(f, size=(100, 100))
    except:
        print("Some Error Occurred..")
