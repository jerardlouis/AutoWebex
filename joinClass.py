import pyautogui, time,schedule, os

os.chdir (r'C:\Users\jguev\OneDrive\Documents\JERARD NJIT\Summer 2020')

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse
def join(classID, meetingPass, startTime, endTime):

    #to open cisco webex
    pyautogui.click(1312, 1790)  # Move the mouse to XY coordinates and click it.

    print("opened webex")
    time.sleep(2)

    cisco = pyautogui.locateOnScreen('joinMeeting.png')
    cisco = pyautogui.doubleClick(cisco.x,cisco.y + 100)

    print("opened class")
    time.sleep(0.5)

    #Types the class name into the search bar
    pyautogui.write(classID, interval=0.05)  # type with quarter-second pause in between each key
    print("entered class ID")
    pyautogui.press('enter')
    time.sleep(10)
    if meetingPass != 'NULL':
        pyautogui.click('meetingPass.png') 

        print('clicked password bar')

        time.sleep(2)

        #Types the password into the class script

        pyautogui.write(meetingPass, interbal =0.05)
        print('typed password')
    #Press enter
    pyautogui.press('enter')
    print('entered class')
    time.sleep(2)
    pyautogui.press('enter')
    print('entered class')
    t = time.localtime()
    currentTime = time.strftime("%H:%M",t)


