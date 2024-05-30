Printer Monoprice maker select V2

x and y axis plotter. 250mm each?

**Firmware**
Marlin Gcode
SD card needs to be fat32

drawing.gcode is being used as a buffer because I don't know how to make this library return an array.

look into: https://pypi.org/project/vpype-gcode/

main.py and svgConverter.py are no longer in use
vpype.py uses the vpype library and does everything that I need it to do for now,\n
I think I want main.py to be used later for writing custom functions that can be\n
called at anytime during the program. 

# Main.py general flow
    - zero
    - flatten sand
    - pickup marble
        - choose marble size
    - start drawing at closest point to curve from marble parking spot
    - draw
    - finish drawing
        choose:
            - flatten sand
                - return marble
                - do whatever flattens sand
            - continue another drawing over it
            - park marble
    - 

TODOS:
    
    - motors loud as hell
    - list dependencies
        - track correct files from vpype lib
    - fix curves from vpype
        - starting
        - optimize travel between curves
    
## Trying to make motors quiet
    Board is a Melzi Hybrid A4988 V3.5
        -has embedded a4988 motor drivers in it, I am going to try to adjust the current.
        if that doesn't work then I am going to explore using an arduino to control the system 
        with some more robust motor controllers. 
        TMC2208 for smoother movements


