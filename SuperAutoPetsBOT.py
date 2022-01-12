import keyboard
import pyautogui
import random
import win32api, win32con
import keyboard
import time
#Beetle (2,171,71)
#^Pos 830 680

##False

foundx = 100
foundy = 100
Pox = 0
Poy = 0

ss = pyautogui.screenshot(region = (470,245,700,280))
ss.save(r"C:\Users\jason\OneDrive\Desktop\Programming\Python Code\BOTS\SuperAutoPets\saved.png")


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def FindEmpty():
    pyautogui.locateCenterOnScreen('Hollo.png', confidence=.4)
    print("The Empty Slot is at " + str(pyautogui.locateCenterOnScreen('Hollo.png', confidence=.8)))
    Hollox, Holloy = pyautogui.locateCenterOnScreen('Hollo.png', confidence=.4) 
    if(Holloy >= 530):
        return False
    else:
        print("This will find the empty thing now")
        return True


def CrickTeamCheck(stc):
    soness = pyautogui.screenshot(region = (500,600,130,140))
    soness.save(r"C:\Users\jason\OneDrive\Desktop\Programming\Python Code\BOTS\SuperAutoPets\ssslot1.png")
    stwoss = pyautogui.screenshot(region = (630,600,130,140))
    stwoss.save(r"C:\Users\jason\OneDrive\Desktop\Programming\Python Code\BOTS\SuperAutoPets\ssslot2.png")
    sthreess = pyautogui.screenshot(region = (760,600,130,140))
    sthreess.save(r"C:\Users\jason\OneDrive\Desktop\Programming\Python Code\BOTS\SuperAutoPets\ssslot3.png")
    if(stc==3):
        if(pyautogui.locateCenterOnScreen('ssslot3.png', confidence=.4) != None):
            
            foundx, foundy = pyautogui.locateCenterOnScreen('ssslot3.png', confidence=.4) 
            if(foundy >= 552):
                FindEmpty()
                return False
            print("Found It")
            print(pyautogui.locateCenterOnScreen('ssslot3.png', confidence=.4))
            print(foundx)
            print(foundy)
            return True
        else:
            print(pyautogui.locateCenterOnScreen('ssslot3.png', confidence=.4))
            return False
    elif(stc==2):
        if(pyautogui.locateCenterOnScreen('ssslot2.png', confidence=.4) != None):
            
            foundx, foundy = pyautogui.locateCenterOnScreen('ssslot2.png', confidence=.4) 
            if(foundy >= 552):
                FindEmpty()
                return False
            print("Found It")
            print(pyautogui.locateCenterOnScreen('ssslot2.png', confidence=.4))
            print(foundx)
            print(foundy)
            return True
    elif(stc==1):
        if(pyautogui.locateCenterOnScreen('ssslot1.png', confidence=.6) != None):
            
            foundx, foundy = pyautogui.locateCenterOnScreen('ssslot1.png', confidence=.6) 
            if(foundy >= 552):
                FindEmpty()
                return False
            print("Found It")
            print(pyautogui.locateCenterOnScreen('ssslot1.png', confidence=.6))
            print(foundx)
            print(foundy)
            return True
        else:
            print(pyautogui.locateCenterOnScreen('ssslot1.png', confidence=.6))
            return False
    

def roll(times = None):
    rtimes = times
    if times == None:
        rtimes = 1
    for i in range(rtimes):
      click(237,924)
      


def BUYslot(slot):
    if slot == 1:
        click(830, 680)
        time.sleep(.3)
        if CrickTeamCheck(3) == True:
            foundx, foundy = pyautogui.locateCenterOnScreen('ssslot3.png', confidence=.4) 
            click(foundx, foundy) 
        elif CrickTeamCheck(3) == False and FindEmpty() == True:
            print("No MATCH PLACING IN EMPTY")
            foundx, foundy = pyautogui.locateCenterOnScreen('Hollo.png', confidence=.5) 
            click(foundx, foundy)
    elif slot == 2:
        click(694,680)
        time.sleep(.2)
        if CrickTeamCheck(2) == True:
            foundx, foundy = pyautogui.locateCenterOnScreen('ssslot2.png', confidence=.4) 
            click(foundx, foundy) 
        elif CrickTeamCheck(2) == False and FindEmpty() == True:
            print("No MATCH PLACING IN EMPTY")
            foundx, foundy = pyautogui.locateCenterOnScreen('Hollo.png', confidence=.5) 
            click(foundx, foundy)
    elif slot == 3:
        click(558,696)
        time.sleep(.5)
        if CrickTeamCheck(1) == True:
            foundx, foundy = pyautogui.locateCenterOnScreen('ssslot1.png', confidence=.4) 
            click(foundx, foundy) 
        elif CrickTeamCheck(1) == False and FindEmpty() == True:
            print("No MATCH PLACING IN EMPTY")
            foundx, foundy = pyautogui.locateCenterOnScreen('Hollo.png', confidence=.5) 
            click(foundx, foundy) 


def ENDturn():  
    c = False
    click(1668,930)
    time.sleep(2)
    click(1300,599)
    while c == False:
        if(pyautogui.locateCenterOnScreen('EndClick.png', confidence=.7) != None):
            print("Havrnt found")
            c = True
    time.sleep(2)
    pyautogui.click()
    print("Founf")
    time.sleep(2)
    click(500,500)


def Turn1():
    print("Turn1")

Turn1()