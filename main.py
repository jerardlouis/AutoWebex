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

'''
class meeting:
    times = {}
    classID = ''
    password = ''
    classLength = 0
    def __init__(self):
        print('Enter the class meeting ID:\n')
        self.classID = input()
        print('Enter the password to your class:\n')
        self.password = input()
        print('How many times a week does your class meet?\n')
        x = input()
        print('The code will now prompt you to enter the days in which your classes meet\n')
        for i in range(x+1):
            print('Day ' + str(i+1) + ' of your class meetings in lowercase:\n')
            day = input()
            print('Enter the time of your class in military time\n')
            print('ex: 1:00pm = 13:00')
            time = input()
            self.times.update({day:time})
            print('Enter the amount of minutes your class takes\n')
            print('Ex: 2 hours and 15 minutes is 135 minutes')
            self.classLength = input()

class classes:
    def __init__(self):
        print('How many classes are you enrolled in?')
        x = input()

'''
