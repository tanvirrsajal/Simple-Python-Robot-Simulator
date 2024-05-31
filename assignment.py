from __future__ import print_function
import time
from sr.robot import *


a_th = 2.0  #float: Threshold for the control of the orientation
d_th = 0.4  #float: Threshold for the control of the linear distance

R = Robot()  #instance of the class Robot
GrabbedBox = list()    #Creating a list to store the information of the boxes that the robot has already grabbed
numberOfBoxes = 4
with open('Readings.txt', 'a+') as myfile:
        myfile.writelines(['Number of boxes:' + str(numberOfBoxes) + '\n'])


def drive(speed, seconds):

    """ Function for setting a linear velocity
    	Args: speed (int): the speed of the wheels
        seconds (int): the time interval """
        
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    
    """ Function for setting an angular velocity
    	Args: speed (int): the speed of the wheels
        seconds (int): the time interval  """
    
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
def FindBox():
    
    """ Function for the robot to find the nearest box
    	Returns:
        	dist (float): distance of the closest token (If no box is detected it will return -1)
        	rot_y (float): angle between the robot and box (If no box is detected it will return -1)
        	Info (int): The information of the nearest box (If no box is detected it will return -1)  """
    # print(GrabbedBox)

    dist = 100
    for Box in R.see():
       
        if Box.dist < dist and Box.info.marker_type == MARKER_TOKEN_GOLD and (Box.info.code not in GrabbedBox):
            #print(Box.info.code, Box.dist, GrabbedBox)
            dist = Box.dist
            rot_y = Box.rot_y
            Info = Box.info.code
    if dist == 100:
        return -1, -1, -1
    else:
        return dist, rot_y, Info
    
    

def GrabBox():
    """Function for the robot to grab boxes"""

    loop = 1
    while loop:
        dist, rot_y, Info = FindBox()  # The robot search for boxes
        if dist <= d_th:  
            print("Found a box!")
            loop = 0    # The loop stops if the robot is close to the box so that it can grab the box
        elif -a_th <= rot_y <= a_th:  # If the robot is well aligned with the box, it needs to go forward and if it is not well aligned it needs to go left or right to grab the box
            print("Ah, that'll do!")
            drive(40, 0.25)
        elif rot_y < -a_th:
            print("A bit left...")
            turn(-5, 0.2)
        elif rot_y > a_th:
            print("A bit right...")
            turn(5, 0.2)  
    return Info
            
def FindDropLocation():
    
    """ Function for the robot to find the nearest box from the boxes that were previously grabbed and put the currently grabbed box next to it.
    	Returns:
        	dist (float): distance of the closest box ((If no box is detected it will return -1)
        	rot_y (float): angle between the robot and the box (If no box is detected it will return -1)
        	Info (int): The information of the closest box (If no box is detected it will return -1) """
        	
    dist = 100
    for Box in R.see():
        if Box.dist < dist and Box.info.marker_type == MARKER_TOKEN_GOLD and Box.info.code in GrabbedBox:
            dist = Box.dist
            rot_y = Box.rot_y
            Info = Box.info.code
    if dist == 100:
        return -1, -1, -1
    else:
        return dist, rot_y, Info      
            
def ReleaseBox():
    """ Function for the robot to go to the nearest box which was previously grabbed"""
    
    loop = 1
    while loop:
        dist, rot_y, Info = FindDropLocation()  # The robot searches for the nearest box which was previously dropped
        if dist < d_th + 0.1:  # A small value is added so that the robot doesn't push away the previous box
            print("Drop Location located!")
            loop = 0 # if the robot is close to the drop location the loop is stopped for the robot to drop the box
        elif -a_th <= rot_y <= a_th:  #if the robot is well aligned with the box, it needs to go forward and if it is not well aligned it needs to go left or right to grab the box
            print("Ah, that'll do!")
            drive(40, 0.25)
        elif rot_y < -a_th:
            print("A bit left...")
            turn(-5, 0.2)
        elif rot_y > a_th:
            print("A bit right...")
            turn(5, 0.2)
            
import time
start_time = time.time() 

"The robot searches for the nearest box and grabs it"
dist, rot_y, Info = FindBox()
print("Scanning for a box")
Info = GrabBox()
R.grab()
print("Grabbed the box!")

"Robot turns and goes to the drop location (the center) and releases the box "
turn(-15, .8)
drive(40, 5)
R.release()
print("Box Delivered!")

"The robot goes behind so that it does not collide with the box it has just dropped"
drive(-70, 1)
turn(30, 1)

GrabbedBox.append(Info)  # The Information of the box that was just dropped is added to the GrabbedBox list



while len(GrabbedBox) < numberOfBoxes:   #A loop is created to grab and drop all the box
    start_time2 = time.time() 
    dist, rot_y, Info = FindBox()
    while dist == -1:
        print("Scanning for more boxes!")
        turn(20, .5)
        dist, rot_y, Info = FindBox()
    end_time2 = time.time() 
    print('Time for finding box:', end_time2 - start_time2)
    with open('Readings.txt', 'a+') as myfile:
        myfile.writelines(['Time for finding box:' + str(end_time2 - start_time2) + '\n'])
    Info = GrabBox()
    R.grab()
    print("Grabbed the box!")
    start_time1 = time.time()



    Ldist, Lrot_y, LInfo = FindDropLocation()
    while Ldist == -1:
        print("Searching for a Drop Location!")
        turn(20, .5)
        Ldist, Lrot_y, LInfo = FindDropLocation() # The robot searches for the boxes it has previously dropped from the GrabbedBox list to drop the box that it is grabbing
    ReleaseBox()
        
    R.release()    # The robot drops the box to the nearest box from the GrabbedBox list
    print("Box Delivered!")
    end_time1 = time.time()
    
    print('Time to deliver box:', end_time1 - start_time1)

    #print('Time taken to grab the box and release:', end_time - start_time)
    with open('Readings.txt', 'a+') as myfile:
        myfile.writelines(['Time to deliver box:' + str(end_time1 - start_time1) + '\n'])

    drive(-40, 1)
    turn(20, .6)

    GrabbedBox.append(Info) # The Information of the box that was just dropped is added to the GrabbedBox list
end_time = time.time()
print('execution time:', end_time - start_time)
with open('Readings.txt', 'a+') as myfile:
    myfile.writelines(['execution time:' + str(end_time - start_time) + '\n'])