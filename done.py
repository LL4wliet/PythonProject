import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
from functools import partial
import threading
import imutils

flag = False

def play(speed):
    video = cv2.VideoCapture("catch2.mp4")
    global flag
    print(f"Speed is:{speed}")


    frame = video.get(cv2.CAP_PROP_POS_FRAMES)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)

    waste, frame = video.read()
    if not waste:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.text(134, 26, fill="red", font="Times 26 bold", text="Decision Pending")
    flag = not flag

def play1(speed):
    video = cv2.VideoCapture("trim.mp4")
    global flag
    print(f"Speed is:{speed}")


    frame = video.get(cv2.CAP_PROP_POS_FRAMES)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)

    waste, frame = video.read()
    if not waste:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.text(150, 35, fill="red", font="italic 26 bold", text="Decision Pending")
    flag = not flag

def play2(speed):
        video = cv2.VideoCapture("trim2.mp4")
        global flag
        print(f"Speed is: {speed}")

        frame = video.get(cv2.CAP_PROP_POS_FRAMES)
        video.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)
        waste, frame = video.read()
        if not waste:
            exit()
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
        if flag:
            canvas.create_text(134, 26, fill="red", font="Times 26 bold", text="Decision Pending")
        flag = not flag

def play3(speed):
    video = cv2.VideoCapture("stump.mp4")
    global flag
    print(f"Speed is:{speed}")


    frame = video.get(cv2.CAP_PROP_POS_FRAMES)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)

    waste, frame = video.read()
    if not waste:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.text(150, 35, fill="red", font="italic 26 bold", text="Decision Pending")
    flag = not flag

def play4(speed):
    video = cv2.VideoCapture("edge.mp4")
    global flag
    print(f"Speed is:{speed}")


    frame = video.get(cv2.CAP_PROP_POS_FRAMES)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)

    waste, frame = video.read()
    if not waste:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.text(150, 35, fill="red", font="italic 26 bold", text="Decision Pending")
    flag = not flag

def play5(speed):
    video = cv2.VideoCapture("bcheck.mp4")
    global flag
    print(f"Speed is:{speed}")


    frame = video.get(cv2.CAP_PROP_POS_FRAMES)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)

    waste, frame = video.read()
    if not waste:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.text(150, 35, fill="red", font="italic 26 bold", text="Decision Pending")
    flag = not flag

def pending(decision):

    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    if decision == 'out':
        decisionImg = "outimage.jpg"

    elif decision == 'not out':
        decisionImg = "notoutimage.jpg"
    else:
        decisionImg = "noball.jpg"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def noball1():
    thread = threading.Thread(target=pending, args=("noball",))
    thread.daemon = 1
    thread.start()
    print("NO ball")

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


window = tkinter.Tk()
window.title("Third Umpire Decision")
SET_WIDTH = 600
SET_HEIGHT = 350
cimg = cv2.cvtColor(cv2.imread("drs.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cimg))
canvas_image = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

def catch():
    cat = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -55))
    cat.pack()

    cat = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -10))
    cat.pack()

    cat = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 10))
    cat.pack()

    cat = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play, 55))
    cat.pack()

    cat = tkinter.Button(window, text="Give Out", width=50, command=out)
    cat.pack()

    cat = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
    cat.pack()
    window.mainloop()

def runout():
    run = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play1, -55))
    run.pack()

    run = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play1, -10))
    run.pack()

    run = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play1, 30))
    run.pack()

    run = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play1, 105))
    run.pack()

    run = tkinter.Button(window, text="Give Out", width=50, command=out)
    run.pack()

    run = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
    run.pack()
    window.mainloop()
def noball():

    nb = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play2, -25))
    nb.pack()

    nb = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play2, -2))
    nb.pack()

    nb = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play2, 2))
    nb.pack()

    nb = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play2, 25))
    nb.pack()

    nb = tkinter.Button(window, text="no ball", width=50, command=noball1)
    nb.pack()

    window.mainloop()
def stumping():
    stump = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play3, -55))
    stump.pack()

    stump = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play3, -10))
    stump.pack()

    stump = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play3, 30))
    stump.pack()

    stump = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play3, 105))
    stump.pack()

    stump = tkinter.Button(window, text="Give Out", width=50, command=out)
    stump.pack()

    stump = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
    stump.pack()
    window.mainloop()

def edge():
    ed = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play4, -55))
    ed.pack()

    ed = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play4, -10))
    ed.pack()

    ed = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play4, 30))
    ed.pack()

    ed = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play4, 105))
    ed.pack()

    ed = tkinter.Button(window, text="Give Out", width=50, command=out)
    ed.pack()

    ed = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
    ed.pack()
    window.mainloop()

def boundarycheck():
    check = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play5, -55))
    check.pack()

    check = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play5, -10))
    check.pack()

    check = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play5, 30))
    check.pack()

    check = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play5, 105))
    check.pack()

    check = tkinter.Button(window, text="SAVE", width=50, command=out)
    check.pack()

    check = tkinter.Button(window, text="Boundary", width=50, command=not_out)
    check.pack()
    window.mainloop()

tkwnd = tkinter.Tk()
tkwnd.title("decision review system")
SET_WIDTH = 700
SET_HEIGHT = 400

button1 = tkinter.Button(tkwnd, text=" catch", width=80,command=catch)
button1.pack()
button1 = tkinter.Button(tkwnd, text="no-ball", width=80,command=noball)
button1.pack()
button1 = tkinter.Button(tkwnd, text="run-out", width=80,command=runout)
button1.pack()
button1 = tkinter.Button(tkwnd, text="stumping", width=80,command=stumping)
button1.pack()
button1 = tkinter.Button(tkwnd, text="edge", width=80,command=edge)
button1.pack()
button1 = tkinter.Button(tkwnd, text="boundarycheck", width=80,command=boundarycheck)
button1.pack()
tkwnd.mainloop()