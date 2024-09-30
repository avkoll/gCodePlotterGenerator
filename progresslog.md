# Daily Progress Log
# Template:
## 2024-00-00
- **Tasks Completed**:
  - Done
- **Challenges**:
  - Done
- **Next Steps**:
  - Done
- **Notes**:
  -

## 2024-06-11
- **Tasks Completed**:
  - robit now moves with the correct units and whatnot.
  - web interface with UGS is a lifesaver
  - the web interface and UGS run on startup
- **Challenges**:
  - need to change how the gcode for shapes is generated.
  - ~~arduino only has around 400 bytes of memory, maybe that is causing the problems~~
- **Next Steps**:
  - make table lol
  - change gcode generator
  - test gcode from the generator
  - ~~Figure out how to use the UGS API and integrate with the flask server, sending the files directly wont work reliably~~
  - tune the offsets
  - clean repo
  - create a backup of the raspberry pi sd card so I can just plug in if it fails
- **Notes**:
  - the updated grbl settings in this repo work at a ratio of 2.54 : 1. moving to position 100 moves it ~254mm instead of 100mm
  - Fixed the problem above ^ I had the grbl settings wrong...
  - the size of the file is not the problem.
  it is still giving error 9 when I only include the first ten lines of the snowflake file so it is something with the commands
  - I am going to try multiplying each value by 0.9 so it fits within the margins
  - Universal Gcode Sender has a web pendant built into the app so I no longer need the flask server
  - I need to redo alot of dependencies and clean up the repo
  - 

## 2024-06-10
- **Tasks Completed**:
  - Done
- **Challenges**:
  - test.gcode just homes and then moves quickly and stops
- **Next Steps**:
  - Done
- **Notes**:
  - I don't think this will be done by the 18th
  - trying to figure out right grbl settings
  - Steps/mm = (Steps per Revolution)*(Microsteps) / (mm per Revolution)
1) Steps per Revolution = 200 Typical - This is the number of steps required
for your stepper motor to make 1 complete revolution.
   - I am going to go with 200 since that is typical 
   - 1.8 deg/step
2) Microsteps - 1,2,4,8,16 - Is a setting on your stepper motor driver. A higher
value means lower torque but higher accuracy.
   - I think I am on 32 microsteps
3) mm per Revolution - Determined by your machine setup. (lead screw pitch)

## 2024-06-08
- **Tasks Completed**:
  - Server setup
  - I am able to execute gcode files by accessing the flask server
- **Challenges**:
  - Need to get steps and units corrected
  - CNC only executes homing and the first G0 command then sits there. 
- **Next Steps**:
  - Start on table
  - Have it start server and home when the table is turned on so it is ready to execute files on demand
- **Notes**:
  - Setting up flask server to execute python commands on local network to control machine
  - flask server setup in a venv in ~/flask_app
  - remember to copy over the grbl settings into this repo
  - dependencies are increasing.. 



## 2024-06-07
- **Tasks Completed**:
  - Connected to raspberry pi via vnc 
  - basic Gcode works
- **Challenges**:
  - need to configure and recompile grbl to only home the x and y axis
  - So many problems with grbl, I need to set how many steps per mm and whatnot, I cannot get it to home for the life of me
- **Next Steps**:
  - Figure out how to get GRBL to home
  - cut out square for dropout
- **Notes**:
  - I will setup a webserver on the pi that you can connect to when on the same wifi to select which file you want to be drawn
  - I need to get a beefier power supply for the pi, it is on 2.4 amps and it recommends 5 or something
  - Got old power supply working 
  - EDIT THE CONFIG FILE THAT WILL BE USED TO COMPILE!!!!
  - 

## 2024-06-05
- **Tasks Completed**:
  - None
- **Challenges**:
  - None
- **Next Steps**:
  - program micro controller 
  - start on actual table part
- **Notes**:
  - Raspberry pi will control arduino which has a cnc shield and the two tmc2208 motor drivers on it.
  - I don't know how we will tell the table to make each drawing yet 
  
## 2024-06-04
- **Tasks Completed**:
  - Prototype complete
  - Lowered overall height by 30mm
  - the motors are set up in the right direction
  - Strengthened y-axis pulley mount
  - mounting screws are now in channels so it can be moved on base
- **Challenges**:
  - Blew power supply, tested with a car battery charger...
- **Next Steps**:
  - program micro controller 
  - start on actual table part
- **Notes**:
  - Completed working prototype yesterday, I am waiting on cnc shield and motor drivers to come in the mail.
  - Going to lower height by 30mm 
  - The robot will be mounted upside down under a board, no need for a large box under the table anymore.
## 2024-06-02
- **Tasks Completed**:
  - Prototype made, need to tweak some tolerances and whatnot but the general layout works
- **Challenges**:
  - NA
- **Next Steps**:
  - tweak tolerances
  - design magnet holder
  - redesign control board
  - attach belts and test
- **Notes**:
  - Redesigning robot to replace the 3d printer
  - I did various changes to each part but I have everything except for the belts now I think

## 2024-06-01
- **Tasks Completed**:
  - Done
- **Challenges**:
  - Silent printer board was a problem, could not get it to start up without all the printer components.
  - 
- **Next Steps**:
  - develop arduino to control motors with cnc shield and tmc2208 motor drivers. 
- **Notes**:
  - Bars, sand and wheels came in today I will start designing the mk2 of the plotter.
  - 
## 2024-05-30
- **Tasks Completed**:
  - Adjusted motor current (reduced by 10%)
  - Tested feed rates (still too noisy)
- **Challenges**:
  - Noise reduction was minimal
  - Need to explore new motor drivers
- **Next Steps**:
  - Research TMC2209 motor drivers
  - See how easy it will be to redesign the rail system
  - Flash Firmware to new board
- **Notes**:
  - I think I am going to need to redesign the entire thing... I can reduce the footprint of the 'bot' if I don't use the 
  printer base. 
  - Micro center sells a board with TMC2209 for the creality Ender, I think this is the way to go. 
    - Creality E3 Free-runs TMC2209 32-bit Open Source Silent Motherboard
      - I need to flash firmware onto it
  - Buying new board and redesigning whole plotter using aluminum square extrusions

