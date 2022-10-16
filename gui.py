import RPi.GPIO as GPIO
import time 
from tkinter import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def rgb(rgb):
    """Convert RGB colour coding to hexadecimal string using this function. 

    Args:
        rgb (int): rgb colour tuple

    Returns:
        string: hexadecimal string representing a colour
    """
    return "#%02x%02x%02x" % rgb

root = Tk()
root.title("LEDS")
root.minsize(width=400, height=150)
root.geometry("400x200")
root.config(bg= rgb((47, 46, 47)))

# A special variable in the tkinter module which we are using to store value of the 
# button which is pressed 
var = StringVar()

def gui():
    """This function will load the main GUI components 
    """
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
    """This function takes the colour of the led as parameter and then turn ons the 
    respective led

    Args:
        colour (string): Colour of the led to turn on
    """
    if colour == "red":
        LEDred()
    elif colour == "blue":
        LEDblue()
    elif colour == "green":
        LEDgreen()

def LEDred():
    """Function to run on red led on and off
    This function will turn on red led and will turn off all other leds
    """
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
    """Function to run on blue led on and off
    This function will turn on blue led and will turn off all other leds
    """
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
    """Function to run on green led on and off
    This function will turn on green led and will turn off all other leds
    """
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
    """This function wiil set pin 10, 12 and 16 to low and 
    then it will set all the pins of raspberry pi to its default state 
    which is input state. After that it will distroy the root instance 
    and it's widgets. 
    """
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()
    root.destroy()

gui()

root.mainloop()
