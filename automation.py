from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def WhatsAppmsg(name,message):
    startfile("https://web.whatsapp.com/")
    sleep(20)

    click(x=1662, y=147)
    sleep(10)
    write(name)
    sleep(2)
    click(x=1573, y=268)
    sleep(5)
    click(x=1914, y=690)
    sleep(2)
    write(message)
    press('enter')


    

