

# 2D Plotter Table Project

## Overview
- I want to make a table with a 2d plotter inside that will be used to roll a marble through sand like a japanese garden Sisyphus industries 
made one that I am basing my design off of.

## Current Status
- Prototype created
  - only the robit part has been made, tabletop and legs still need to be made
    - Add pictures here
- Code is basically completed just needs some optimization

## Tasks
- [ ] Build Table
- [ ] Build Bot
  - [x] ProtoType
  - [ ] Write Gcode Generator
  - [ ] make bot quiet
    - [ ] Replace controller
    - [ ] Remake rails?
  - [ ]
- [ ] Add Bot to table
- [ ] Completed Task

## Log
### 2024-05-30
- Started working on motor calibration
- Encountered noise issues with motors

### 2024-05-19
- Implemented vpype library
- Removed deprecated scripts (main.py, svgConverter.py)

## Resources
- [vpype-gcode](https://pypi.org/project/vpype-gcode/)

## Future Plans
- Implement custom functions in main.py
- Improve motor noise reduction
- Replace motor driver
- Make bot with higher quality plywood
- Optimize vpype script



## Dependencies
- Raspberry pi:
  - flask
  - venv
  - python
  - grbl
  - UGS

flask server is accessible from here:
http://raspberrypi.local:5000

Notes Pre reformatting:
---

# Printer: Monoprice Maker Select V2

## Overview
- **X and Y Axis Plotter**: 250mm each

## Firmware
- **Type**: Marlin G-code
- **SD Card**: Must be FAT32 formatted

## Current Workflow
- **drawing.gcode**: Used as a buffer due to library limitations (returning an array)
- **Library to Explore**: [vpype-gcode](https://pypi.org/project/vpype-gcode/)

### File Usage
- **main.py** and **svgConverter.py**: No longer in use
- **vpype.py**: Utilizes the vpype library for current functionalities
  - Future Use of **main.py**: Writing custom functions callable at any time during the program

## General Flow of main.py
1. Zero
2. Flatten sand
3. Pick up marble
   - Choose marble size
4. Start drawing at the closest point to the curve from the marble parking spot
5. Draw
6. Finish drawing
   - Options:
     - Flatten sand
       - Return marble
       - Do whatever flattens sand
     - Continue another drawing over it
     - Park marble

## TODOS
- **Motors Loud as Hell**
  - ~~Adjust current (lowered 10%)~~
  - ~~Adjust feed rate (none worked)~~
    - ~~300 too quick~~
    - ~~100 too quick~~
    - ~~10 too slow~~
  - Replace control board with something better
- **List Dependencies**
  - Track correct files from vpype library
- **Fix Curves from vpype**
  - Starting
  - Optimize travel between curves

## Trying to Make Motors Quiet
- **Board**: Melzi Hybrid A4988 V3.5 (embedded A4988 motor drivers)
  - Adjusting current: if unsuccessful, explore using an Arduino with robust motor controllers
  - Potential controllers: TMC2208 for smoother movements, R100 Resistors
- **Motors**: C17HD40102-01N BiPolar
  - 1.8 degrees per step
  - 1.02A
  - 0.62NM

### Tuning Drivers for Noise Reduction (DID NOT WORK)
- Following this guide: [Adjusting stepper motor current on Melzi Board](https://3dprinterwiki.info/setting-the-stepper-current-on-the-melzi-board/)
  - **Target**: 90% max current
  - **Formula**: VREF = Current(A) * 8 * SenseResistor(RS)
    - 0.82 = 1.02 * 8 * 0.1
    - 0.74 = 90% power
  - Initial values for each potentiometer: 0.67 (lower than max)
  - Reduced to 0.60 (by 10%) to see if it helps
  - **Result**: Noise reduction was minimal; further steps needed

---