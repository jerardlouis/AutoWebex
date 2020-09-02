import schedule, time, datetime
from joinClass import join

#Create the class of meeting objects
class meeting():
    def __init__(self, classID, meetingPass, startTime, endTime, days):
        self.classID = classID
        self.meetingPass = meetingPass
        self.startTime = startTime
        self.endTime = endTime
        self.days = days

#List of classes to append class meetings to
classes = [
    #cs241 = meeting('classID','meetingPass','12:30','15:20',['Monday']),
    math333 = meeting('922617121','NULL','12:30','13:50',['Tuesday','Thursday']),
    cs350 = meeting('1202568881','applesauce','14:30','15:50',['Tuesday','Thursday']),
    cs356no1 = meeting('1203126384','w3N9np6Mkix','09:00','10:20',['Tuesday']),
    cs356no2 = meeting('1203126384','w3N9np6Mkix','11:00','12:20',['Wednesday']),
    #eng340 = meeting('94963492346','Gorelick','11:00','12:30',['Tuesday','Thursday']) #Class is on zoom
]
#Run the code to join classes
def main():
    global classes
    #While loop to continuously run and check day
    #If the day has a meeting then check for time and run class during that time
    '''
    SCRATCH THE WHILE LOOP IDEA AND JUST HAVE THE CODE OPEN EVERY MONDAY AT 8AM
    MAKE THE CODE CHECK THE DAY EVERY MORNING AT 8AM
    CHECK FOR CLASSES THAT RUN THAT DAY
    RUN THOSE CLASSES AT THE CURRENT TIME
    THEN WHEN CLASS IS OVER RUN A LOOP EVERY MINUTE TO CHECK WHEN THE NEXT CLASS IS
    IF THE TIME OF A CLASS STARTS THEN OPEN THE CLASS
    '''
    isRunning = False
    while isRunning == False:
        #Do something
        now = datetime.datetime.now()
        if now.strftime("%A") == 'Monday':
            for i in classes:
                if classes[i].days == 'Monday':
                    #Do something 

        if now.strftime("%A") == 'Tuesday':
            #Do something
        if now.strftime("%A") == 'Wednesday':
            #Do something
        if now.strftime("%A") == 'Thursday':
            #Do something
        if now.strftime("%A") == 'Friday':
            #Do something

        time.sleep(30)

