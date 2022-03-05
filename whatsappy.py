import pyautogui
import time
import win32api
import webbrowser as web
import keyboard

def action():
    win32api.MessageBox(0, 'partenza programma, clicca ok e attendere la fine (15s circa)', 'attenzione', 0x00001000)   #alert message before start
    web.open("https://web.whatsapp.com")  #open whatsapp
    time.sleep(15)  #15s waiting the page to be opened (with a good connection it is possible to lower this time)
    pyautogui.click(400, 290)   #automove to the search bar of whatsapp web
    time.sleep(1)
    pyautogui.typewrite('SoBig')   #autodigit in search bar the name of the recipient of the message. can be private or group
    time.sleep(1)
    pyautogui.click(400, 500)  # autoselect the first search result
    time.sleep(1)
    pyautogui.click(1000, 950) # automove to textarea
    time.sleep(1)
    pyautogui.typewrite('Bot-->🤖 Ricordatevi di segnare la presenza')   #autowrite the message to be sent
    time.sleep(1)
    keyboard.press_and_release('enter')  #autosend
    return None

#main
inp = input("numero di turni: ")
counter = 0
if inp == '1':   #if it's a single message
    action()
    print("ok, per ora mi spengo. alla prox")
else:
    action()
    while True:
        time.sleep(3605)  # define the interval of time between messages, e.g. 3605s
        counter += 1
        if counter == 2:  #define the number of messages to be sent
            action()
            print("ok, per ora mi spengo. alla prox")
            break
        print("Un'ora è andata!")
