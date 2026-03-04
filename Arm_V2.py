import pyfirmata2 as pyfirmata
import time
import keyboard as key

PORT = "COM3"
PIN_Shoulder  = 9 
PIN_elbow = 11

Pin_hand = 6

Pin_gripper = 3

current_pos1 = 90
current_pos2 = 120
current_pos3 = 100 #IDKKKKK
current_pos4 = 180 # IDKKKKK


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

print("Syncing servo positions to safe positions")
servo1.write(current_pos1)
servo2.write(current_pos2)
servo3.write(current_pos3)
servo4.write(current_pos4)


def moveto(target1,target2,target3,target4,speed):
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

#cords = [[90,120,100,150], [60,80,0,0], [90,120,100,150], [180,70,30,20], [90,120,100,150],[90,120,100,150], [60,80,0,0], [90,120,100,150], [180,70,30,20], [90,120,100,150]]

def follow_path(cords):
    for cord in cords:
        M_shouler, M_elbow, M_hand, M_gripper = cord[0], cord[1], cord[2], cord[3]

        moveto(M_shouler, M_elbow, M_hand, M_gripper, 0.01)      # Just Elbow
   #     moveto(M_shouler, current_pos2, current_pos3, current_pos4, 0.01)    # Just Shoulder

   #     moveto(current_pos1, current_pos2, M_hand, current_pos4, 0.01)       # Just Hand
        
        
  #      moveto(current_pos1, current_pos2, current_pos3, M_gripper, 0.01)    # Just Gripper

        time.sleep(0.5)


saved_path = []


while True:
    degrees = input("Give Degrees of Shoulder and Elbow example 90,15,45,30:        OR P for Path:  Or S for save:   Or D for Drive:      ")
    
    if degrees.lower() == "q":
        break


    if degrees.lower() == "s":
        saved_path.append([current_pos1, current_pos2, current_pos3, current_pos4])
        print("Path saved!")
        continue

    if degrees.lower() == "p":
        print("Following path...")
        follow_path(saved_path)
        print("Done with path, sheeeesh")
        continue


    if degrees.lower() == "d":
        print("DRIVE mode: A/D for Shoulder, W/S for for Elbow, R/F for Hand, T/G for Gripper, q to quit")
        while True:

            s, e, h, g = current_pos1, current_pos2, current_pos3, current_pos4
            moved = False
            if key.is_pressed("a"): s += 2; moved = True
            elif key.is_pressed("d"): s -= 2; moved = True
            elif key.is_pressed("w"): e -= 2; moved = True
            elif key.is_pressed("s"): e += 2; moved = True
            elif key.is_pressed("r"): h -= 2; moved = True
            elif key.is_pressed("f"): h += 2; moved = True
            elif key.is_pressed("t"): g -= 2; moved = True
            elif key.is_pressed("g"): g += 2; moved = True

            if key.is_pressed("z"):
                saved_path.append([current_pos1, current_pos2, current_pos3, current_pos4])
                print("Path saved!")
                time.sleep(0.5) 

            
            if key.is_pressed("esc"): 
                print("Exiting DRIVE mode")
                break

            if moved:
                if 0 <= s <= 180 and 0 <= e <= 180 and 0 <= h <= 180 and 0 <= g <= 180:
                    moveto(s, e, h, g, 0.01)
                else:
                    print("keep angles between 0 and 180")

            time.sleep(0.02)  


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
