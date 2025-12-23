import pyautogui as p
import keyboard , time
var = 1
def plusvar():
    global var
    var += 1
    print("var : " + str(var))
def resetvar():
    global var
    var = 1
    print("var : " + str(var))

def tl90():
    p.move(-600,0)
def tr90():
    p.move(600,0)
def tu90():
    for i in range(2):
        tu45()
def td90():
    for i in range(2):
        td45()
def tl45():
    p.move(-300,0)
def tr45():
    p.move(300,0)
def tu45():
    p.move(0,-300)
def td45():
    p.move(0,300)

def jump():
    p.keyDown('space')
    p.keyUp('space')
def walk():
    p.keyDown('w')
    time.sleep(0.15)
    p.keyUp('w')
def s():
    p.keyDown('s')
    time.sleep(0.15)
    p.keyUp('s')
def a():
    p.keyDown('a')
    time.sleep(0.15)
    p.keyUp('a')
def d():
    p.keyDown('d')
    time.sleep(0.15)
    p.keyUp('d')
def jumpnxt():
    p.keyDown("space")
    p.keyDown("w")
    p.keyUp("space")
    time.sleep(0.18)
    p.keyUp("w")
def mine():
    p.press('7')
    p.mouseDown(button = "left")
    time.sleep(0.4)
    p.mouseUp(button = "left")

def delay():
    time.sleep(0.7)

def leaf():
    p.press('5')
    p.mouseDown(button = "left")
    time.sleep(0.5)
    p.mouseUp(button = "left")
    
def chop():
    p.press('8')
    p.mouseDown(button = "left")
    time.sleep(0.7)
    p.mouseUp(button = "left")

def tree():
    ls = [tu90, leaf,td90 , chop , tu45 , chop , td45 , jumpnxt , tu90 , chop , chop , chop , chop , chop ,td90 , td90 , chop]
    for c in ls:
        c()
        
def m1x3x1():
    ls = [mine, td45, mine , tu45, tu45, mine , td45]
    for c in ls:
        c()
        
def dirt():
    p.mouseDown(button="left")
    time.sleep(0.4)
    p.mouseUp(button="left")

def s5():
    for i in range(var):
        ls = [dirt, walk ,dirt , walk , dirt, walk ,dirt , walk ,dirt , walk ,dirt , walk ,]
        for c in ls:
            c()
def s25():
    for i in range(var):
       ls = [s5 , tl90 , dirt, walk , tl90 ,s5 , tr90 , dirt , walk , tr90, s5 , tl90 , dirt , walk , tl90 ,s5 , tr90 , dirt , walk , tr90,s5]
       for c in ls:
           c()
def continue25():
    for i in range(var):
       ls = [tl90 , tl90 , walk , walk , walk ,walk , walk , tr90 , dirt , walk , tr90]
       for c in ls:
           c()
def mwall():
    for i in range(var):
        ls = [m1x3x1, a , m1x3x1 , a , m1x3x1 , a , m1x3x1 , a , m1x3x1 , walk , d, d, d, d]
        for c in ls:
            c()
keyboard.add_hotkey('f4', mwall)
keyboard.add_hotkey('f6', mine)
keyboard.add_hotkey('f7', s25)
keyboard.add_hotkey('f8', continue25)
keyboard.add_hotkey('f9', plusvar)
keyboard.add_hotkey('f10', resetvar)
keyboard.wait('esc')
'''
600 pixel to move 90 degree
STONE PICKAXE:
1 sec to mine stone
diamond axe :
0.5 sec to chop wood
diamond pickaxe :
0.6 sec to mine stone
'''
