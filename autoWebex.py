import pyautogui, time, os


'''
*
*
Copy and paste the file directory below between apostrophes
*
*
'''
os.chdir (r'LOCATION OF FILE')
'''
*
*
Update code below: Time must be in military time
*
*
'''
schedule.every().monday.at("TIME").do(start)

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse


#to open cisco webex
#pyautogui.click(1415, 1760)  # Move the mouse to XY coordinates and click it.

pyautogui.click('ciscoIcon.png')
print("opened webex")
time.sleep(3)
#Use this to click on the search bar, find the coordinates

cisco = pyautogui.locateOnScreen('joinMeeting.png')
cisco = pyautogui.center(cisco)
pyautogui.click(cisco.x,cisco.y + 100)

print("opened class")

time.sleep(0.5)
'''
*
*
Enter class ID between apostrophes
*
*
'''
pyautogui.write('ENTER CLASS ID HERE', interval=0.25)  # type with quarter-second pause in between each key
print("entered class ID")

#Press enter
pyautogui.press('enter')
time.sleep(10)
#Find position for the password bar
pyautogui.click('meetingPass.png') 

print('clicked password bar')

time.sleep(3)

#Types the password into the class script
'''
*
*
Enter class password between apostrophes
*
*
'''
pyautogui.write('ENTER PASSWORD HERE', interval=0.25)  # type with quarter-second pause in between each key
print('typed password')
#Press enter
pyautogui.press('enter')
print('entered class')
if(pyautogui.locateOnScreen('join.png')):
    pyautogui.click('join.png')
    print('You are now in class')
else:
    pyautogui.hotkey('alt','f4')
    print('Class has not started yet')
#This code is to close out the window when class ends
'''
*
*
Update code below:
Enter the amount of seconds that your class will take place:
Hours * 60 * 60 + Minutes * 60
*
*
'''
time.sleep('time')

#leave class
pyautogui.hotkey('alt','f4')
print('left class')

