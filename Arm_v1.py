import pyfirmata2 as pyfirmata
import time

PORT = "COM3"
PIN_Shoulder  = 9 
PIN_elbow = 11

Pin_hand = 6

Pin_gripper = 3

current_pos1 = 90
current_pos2 = 180
current_pos3 = 0
current_pos4 = 90


print(f"Connection to the arduino trying port {PORT}")

try:
    board = pyfirmata.Arduino(PORT)
    print("Successfully connecteed!")
except Exception as e:
    print(f"Connection failed, COM port was not correct Error: {e}")
    exit()

servo1 = board.get_pin(f"d:{PIN_Shoulder}:s")
servo2 = board.get_pin(f"d:{PIN_elbow}:s")
servo3 = board.get_pin(f"d:{Pin_hand}:s")
servo4 = board.get_pin(f"d:{Pin_gripper}:s")
"""
try:
    print("Starting servo sweep, Press Ctrl+C to stop")
    while True:

        for angle in range(0, 181, 10):
            servo1.write(angle)
            time.sleep(0.2)

        for angle in range(0, 181, 10):
            servo2.write(angle)
            time.sleep(0.05)
        
        for angle in range(180, -1, -10):
            servo2.write(angle)
            time.sleep(0.05)

        

        for angle in range(180, -1, -10):
            servo1.write(angle)
            time.sleep(0.2)


except KeyboardInterrupt:
    print("Stopping")

    
        

finally:
    board.exit()
    print("Connection closed")

"""

def moveto(target1,target2,target3,target4,speed=0.01):
    global current_pos1, current_pos2, current_pos3, current_pos4

    dist1 = abs(target1 - current_pos1)
    dist2 = abs(target2 - current_pos2)
    dist3 = abs(target3 - current_pos3)
    dist4 = abs(target4 - current_pos4)
    max_dist = max(dist1, dist2, dist3, dist4)

    for i in range(max_dist):
        if current_pos1 < target1:
            current_pos1 += 1
        elif current_pos1 > target1:
            current_pos1 -= 1
        
        if current_pos2 < target2:
            current_pos2 += 1
        elif current_pos2 > target2:
            current_pos2 -= 1

        if current_pos3 < target3:
            current_pos3 += 1
        elif current_pos3 > target3:
            current_pos3 -= 1

        if current_pos4 < target4:
            current_pos4 += 1
        elif current_pos4 > target4:
            current_pos4 -= 1
        
        servo1.write(current_pos1)
        servo2.write(current_pos2)
        servo3.write(current_pos3)
        servo4.write(current_pos4)

        time.sleep(speed)
    


#dance_moves = [[90, 90], [45, 120], [135, 30], [0, 0],[90, 90], [45, 120], [135, 30], [0, 0]]

#for move in dance_moves:
#    moveto(move[0], move[1], 0.02)

#    time.sleep(1)


while True:
    degrees = input("Give Degrees of Shoulder and Elbow example 90,15,45,30:       ")
    
    if degrees.lower() == "q":
        break

    try:
        shoulder, elbow, hand, gripper = map(int, degrees.split(","))

        if 0 <= shoulder <= 180 and 0 <= elbow <= 180 and 0 <= hand <= 180 and 0 <= gripper <= 180:
            moveto(current_pos1, elbow, current_pos3, current_pos4, 0.02)    # Just Elbow
            moveto(current_pos1, current_pos2, current_pos3, gripper, 0.02)  # Just Gripper
            moveto(shoulder, current_pos2, current_pos3, current_pos4, 0.02) # Just Shoulder
            moveto(current_pos1, current_pos2, hand, current_pos4, 0.02)     # Just Hand
        else:
            print("keep angles between 0 and 180")
    except ValueError:
        print("Invalid input, use format: 90,45,45,30")
