import pyautogui as p
import pydirectinput as pd
import time , keyboard
import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def mine_block():
    x , y = p.position()
    p.moveTo(x,y)
    p.mouseDown(button='left')
    time.sleep(0.7) 
    p.mouseUp(button='left')
def pos():
    print(p.position())

def walk(x,y):
    y = y.lower()
    if y in ['w', 'a', 's', 'd']:
        if y == "w":
            dire = "forward"
        elif y == "a":
            dire = "leftwards"
        elif y == "s":
            dire = "backwards"
        elif y == "d":
            dire = "rightwards"
        yield f"walking.. {dire} for {x} seconds"
        p.keyDown(y)
        time.sleep(x)
        p.keyUp(y)
    else:
        yield "Invalid direction"
    
@client.event
async def on_message(message):
    if ".walk" in message.content:
        await message.reply('\n'.join(walk(float(message.content.split()[1]), message.content[5])))
    if message.content.startswith('.pos'):
        await message.reply(pd.position())

client.run('YOUR DISCORD BOT TOKEN')

