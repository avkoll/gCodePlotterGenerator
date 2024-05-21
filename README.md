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
    - list dependencies
    - fix curves from vpype
        - starting
        - optimize travel between curves

## vpype Shid:
Alt profile for monoprice maker select V2:

[gwrite.gcode_maker_select]
document_start = "G20\nG17\nG90\nG28 X0 Y0\n"
segment_first = "G00 X{x:.4f} Y{y:.4f}\n"
segment = "G01 X{x:.4f} Y{y:.4f}\n"
document_end = "G28 X0 Y0\nM2\n"
unit = "in"
vertical_flip = true
info= "This gcode profile is correctly inverted across the y-axis"


