DARKAR: 4-DOF Robotic Arm evolution 

A project documenting the journey from a basic concept to a stable robotic arm

Phase 1:
The primary objective of version 1 was to validate the 4-DOF robotic arm concept. This was was focued on learning 3D modeling using Fusion 360 and understand basics of servos.

Design and Assembly:
Initially the arm was constructed using simple linkages. The servo arm connected using custom designed segments with ressesed mountes for the servo horns

Figure 1: Early prototype showcasing how the servo were connected.
<img width="1062" height="710" alt="image" src="https://github.com/user-attachments/assets/3237c38d-d7f8-4359-8d42-89b9d8d8f301" />


As the design was progressing, a small baseplate was added to provide support during movement.

Figure 2: Intergration of baseplate and initial wiriing setup for the Arduino controll.
![6D2CCFA8-EE3D-498F-8A35-35B2A703CFE9_4_5005_c](https://github.com/user-attachments/assets/77c63343-70b7-4589-acda-80f9e679d235)

Grupper Development:
For the end-effector, i developed a gear-driven gripper system to allow the arm to grip physical objects. 

After this a gear given gripper shown in Figure 3 and Figure 4.

Figure 3:
<img width="560" height="560" alt="image" src="https://github.com/user-attachments/assets/4ce066b6-c98a-4119-9737-eff502a4e8b2" />

Figure 4:
<img width="1115" height="680" alt="image" src="https://github.com/user-attachments/assets/58f2885d-c245-42bd-bd72-abb8e1afd3a0" />


Technical Challenges and Knon issues (V1) 
Version 1 was able to move, it highlighted several critical engineering challenges, that was essential to solve for V2

Mechanical instability: The arm "wobbled" during both idle states and active movement, due to low structural rigidity.

Tolerance issues: The 3d-printed mounts for the servoes has loose fits, leading to imprecies positioning in the joints. 

Mechanical stress: The gripper was lacking software limits, causing it to attempt to move beyond physical constraints leading to self destruction. 

Power limitation: The attempt to power mulitple servos using just the arduinoes 5V output was insufficient. When more than one servo moved at a time the current draw caused volate drops and unstable behavior. 


