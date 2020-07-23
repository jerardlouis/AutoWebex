'''
This is going to be the scheduler app
Basically turn the open class autowebex file into a function that intakes the class ID and password as parameters
Create a meeting class object that has the elements: times(Dictionary of key days and value times), length of class, ID and password
Store data into a .txt file to be read whenever code is opened
'''
import schedule, time, pyautogui, datetime
wait = 0
def start():
    print('doing stuff now')
    pyautogui.click(1248,1780)
    
    print('Now the good shit starts')
    time.sleep(0.5)
    pyautogui.write('cmd')
    pyautogui.press('enter')
    pyautogui.write('cd C:\\Users\\jguev\\OneDrive\\Documents\\JERARD NJIT\\Summer 2020')
    pyautogui.press('enter')
    pyautogui.write('calc2_class.py')
    pyautogui.press('enter')
    wait = 0

def stop():
    print('Class is over')

schedule.every().monday.at("13:00").do(start)
schedule.every().monday.at("15:00").do(stop)
schedule.every().wednesday.at("13:00").do(start)
schedule.every().wednesday.at("15:00").do(stop)
schedule.every().thursday.at("13:00").do(start)
schedule.every().thursday.at("15:00").do(stop)

while True:
    print('The time is ' + str(datetime.datetime.now()))
    schedule.run_pending()
    if wait == 0:
        print('Process started')
    else:
        print(str(wait) + ' minutes since execution')
    time.sleep(60)


