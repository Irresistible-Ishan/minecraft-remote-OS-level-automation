import pyautogui as p
import pydirectinput as pd
import time , keyboard , random
import discord
from discord import app_commands
from PIL import Image

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def tl90():
    p.move(-600,0)
def tr90():
    p.move(600,0)
def tu90():
    p.move(0,-600)
def td90():
    p.move(0,600)
def tl45():
    p.move(-300,0)
def tr45():
    p.move(300,0)
def tu45():
    p.move(0,-300)
def td45():
    p.move(0,300)
    
def mine():
    p.press('8')
    p.mouseDown(button = "left")
    time.sleep(0.6)
    p.mouseUp(button = "left")

def walk(x,y):
    x = x.lower()
    if x in ['w', 'a', 's', 'd']:
        if x == "w":
            dire = "forward"
            for i in range(y):
                p.keyDown("w")
                time.sleep(0.2)
                p.keyUp("w")
        elif x == "a":
            dire = "leftwards"
            tl90()
            p.keyDown("w")
            for i in range(y):
                time.sleep(0.2)
            p.keyUp("w")
        elif x == "s":
            dire = "backwards"
            tl90()
            tl90()
            p.keyDown("w")
            for i in range(y):
                time.sleep(0.2)
            p.keyUp("w")
        elif x == "d":
            dire = "rightwards"
            tr90()
            p.keyDown("w")
            for i in range(y):
                time.sleep(0.2)
            p.keyUp("w")
    else:
        pass

def jump(x):
    for i in range(x):
        p.keyDown('space')
        p.keyUp('space')

def crouch(x):
   for i in range(x):
      p.keyDown("left shift")
      p.keyUp('left shift')

def pic(x,y):
    p.screenshot(x)
    ss = Image.open(x)
    crop = ss.crop(y)
    crop.save(x)

def interact():
    p.mouseDown(button="right")
    p.mouseUp(button="right")

def hit():
    p.press('9')
    p.click(button="left")
    
@client.event
async def on_message(message):
 if message.author.id == 598553232570187802 or message.author.id == 750672235680890880:
    if message.content.startswith('.pos'):
        p.press('f1')
        p.screenshot("positionCODE7X.png")
        ss = Image.open("positionCODE7X.png")
        crop = ss.crop((0,24,1365,725))
        crop.save("positionCODE7X.png")
        await message.reply(file=discord.File("positionCODE7X.png"))
        p.press('f1')
        p.press('f3')
        p.screenshot("coordinatesCODE7X.png")
        ss = Image.open("coordinatesCODE7X.png")
        crop = ss.crop((0, 187, 358, 205))
        crop.save("coordinatesCODE7X.png")
        await message.reply(file=discord.File("coordinatesCODE7X.png"))
        p.press('f3')

    if message.content.startswith(".blockahead"):
        p.press("f3")
        pic("block.png",(1154, 262 ,1362, 277))
        gaga = await message.reply(file=discord.File("block.png"))
        p.press("f3")
        p.press("f1")
        pic("blockpic.png", (624, 324 ,754, 433))
        await gaga.reply(file= discord.File("blockpic.png"))
        p.press("f1")
        
    if message.content.startswith(".run"):
        script = message.content.split()[1:]
        for i in script:
            if i[0] in ['w', 'a', 's', 'd']:
                walk(i[0], int(i[1:]))
            elif i[0] == "j":
                jump(int(i[1:]))
            elif i[0] == "c":
                crouch(int(i[1:]))
            elif i[0] == "m":
                p.press("f1")
                pic("blockpic.png", (624, 324 ,754, 433))
                await message.reply(file= discord.File("blockpic.png"))
                p.press("f1")
                mine()
            elif i[0:] == "tl90":
                tl90()
            elif i[0:] == "tr90":
                tr90()
            elif i[0:] == "tu90":
                tu90()
            elif i[0:] == "td90":
                td90()
            elif i[0:] == "tl45":
                tl45()
            elif i[0:] == "tr45":
                tr45()
            elif i[0:] == "tu45":
                tu45()
            elif i[0:] == "td45":
                td45()
            elif i[0] == "i":
                interact()
            elif i[0] == "h":
                hit()
        p.press('f1')
        p.screenshot("positionCODE7X.png")
        ss = Image.open("positionCODE7X.png")
        crop = ss.crop((0,24,1365,725))
        crop.save("positionCODE7X.png")
        await message.reply(file=discord.File("positionCODE7X.png"))
        p.press('f1')
        p.press('f3')
        p.screenshot("coordinatesCODE7X.png")
        ss = Image.open("coordinatesCODE7X.png")
        crop = ss.crop((0, 187, 358, 205))
        crop.save("coordinatesCODE7X.png")
        cor = await message.reply(file=discord.File("coordinatesCODE7X.png"))
        p.press('f3')
        


client.run('MTExMTYzNjQ2MDQ3NTUyMzEzMg.GhwOUa.AMf2mPpvPokmmyX120gBrivZodHK2gTlDjOC1E')

