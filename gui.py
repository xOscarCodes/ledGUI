import RPi.GPIO as GPIO
from tkinter import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def rgb(rgb):
    return "#%02x%02x%02x" % rgb

root = Tk()
root.title("LEDS")
root.minsize(width=400, height=150)
root.geometry("400x200")
root.config(bg= rgb((47, 46, 47)))

var = StringVar()

def gui():
    global redLEDbutton, greenLEDbutton, blueLEDbutton
    lable = Label(root, text= "PRESS BUTTON TO TURN ON LED", font=('Courier', 12, "bold"),fg= "white", bg= rgb((47, 46, 47)))
    lable.place(relx=0.11, rely=0.15, relwidth= 0.8, relheight= 0.1)

    redLEDbutton = Radiobutton(root, text="RED ON", bg= rgb((241, 0, 0)), variable=var, value= "red",command=lambda: turnOnLed(var.get()))
    redLEDbutton.place(relx= 0.08, rely=0.38, relwidth=0.25, relheight=0.2)

    blueLEDbutton = Radiobutton(root, text="BLUE ON", bg= rgb((115, 194, 251)), variable=var, value= "blue",command=lambda: turnOnLed(var.get()))
    blueLEDbutton.place(relx= 0.37 ,rely=0.38, relwidth=0.25, relheight=0.2)

    greenLEDbutton = Radiobutton(root, text="GREEN ON", bg= rgb((0, 255, 0)), variable=var, value= "green",command=lambda: turnOnLed(var.get()))
    greenLEDbutton.place(relx= 0.66 ,rely=0.38, relwidth=0.25, relheight=0.2)

    exitButton = Button(root, text="Exit", command= exit)
    exitButton.place(relx= 0.398, rely= 0.67, relwidth= 0.20, relheight= 0.2)

def turnOnLed(colour):
    if colour == "red":
        LEDred()
    elif colour == "blue":
        LEDblue()
    elif colour == "green":
        LEDgreen()

def LEDred():
    if redLEDbutton["text"] == "RED OFF":
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        redLEDbutton["text"] = "RED ON"
    elif redLEDbutton["text"] == "RED ON":
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        redLEDbutton["text"] = "RED OFF"
        blueLEDbutton["text"] = "BLUE ON"
        greenLEDbutton["text"] = "GREEN ON"

def LEDblue():
    if blueLEDbutton["text"] == "BLUE OFF":
        GPIO.output(12, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        blueLEDbutton["text"] = "BLUE ON"
    elif blueLEDbutton["text"] == "BLUE ON":
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        blueLEDbutton["text"] = "BLUE OFF"
        redLEDbutton["text"] = "RED ON"
        greenLEDbutton["text"] = "GREEN ON"

def LEDgreen():
    if greenLEDbutton["text"] == "GREEN OFF":
        GPIO.output(16, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        greenLEDbutton["text"] = "GREEN ON"
    elif greenLEDbutton["text"] == "GREEN ON":
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
        greenLEDbutton["text"] = "GREEN OFF"    
        redLEDbutton["text"] = "RED ON"
        blueLEDbutton["text"] = "BLUE ON"

def exit():
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()
    root.destroy()

gui()


root.mainloop()
